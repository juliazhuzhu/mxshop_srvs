import os.path
import signal
import sys
import os
import uuid

import grpc
from concurrent import futures
import argparse
import socket

BASE_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
print(BASE_DIR)
sys.path.insert(0, BASE_DIR)

from user_srv.proto import user_pb2_grpc
from user_srv.handler.user import UserServicer
from common.grpc_health.v1 import health_pb2, health_pb2_grpc
from common.grpc_health.v1 import health
from loguru import logger
from common.register import consul
from user_srv.settings import settings
from functools import partial

def on_exit(sigo, frame, service_id):
    logger.info(f"注销{service_id}服务")
    register = consul.ConsulRegister(settings.CONSUL_HOST, settings.CONSUL_PORT)
    register.deregister(service_id)
    logger.info("注销成功")
    sys.exit(0)


def get_free_tcp_port():
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.bind(("",0))
    addr, port = tcp.getsockname()
    tcp.close()
    return port


def serve():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ip',
                        nargs="?",
                        type=str,
                        default="127.0.0.1",
                        help="binding ip")
    parser.add_argument('--port',
                        nargs="?",
                        type=int,
                        default=0,
                        help="the listening port")

    args = parser.parse_args()
    print(args)

    if args.port == 0:
        args.port = get_free_tcp_port()

    logger.add("logs/user_srv_{time:YYYY-MM-DD_HH:mm:ss}.log", rotation="10 MB")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # 注册用户服务
    user_pb2_grpc.add_UserServicer_to_server(UserServicer(), server)

    # 注册健康检查
    health_pb2_grpc.add_HealthServicer_to_server(health.HealthServicer(), server)

    server.add_insecure_port(f'{args.ip}:{args.port}')
    logger.info(f"启动服务 {args.ip}:{args.port}")
    service_id = str(uuid.uuid1())
    '''
        SIGINT ctrl+c
        SIGTERM kill 发出的软件终止命令
    '''
    signal.signal(signal.SIGINT, partial(on_exit,service_id=service_id))
    signal.signal(signal.SIGTERM, partial(on_exit,service_id=service_id))
    server.start()

    logger.info(f"服务注册开始")

    register = consul.ConsulRegister(settings.CONSUL_HOST, settings.CONSUL_PORT)

    if not register.register(name=settings.SERVICE_NAME, id=service_id, address=args.ip, port=args.port,
                             tags=settings.SERVICE_TAGS, check=None):
        logger.warning(f"服务注册失败")
        sys.exit(0)
    logger.info(f"服务注册成功")
    server.wait_for_termination()


@logger.catch
def my_function(x, y, z):
    return 1 / (x + y + z)



if __name__ == '__main__':
    # my_function(0,0,0)
    settings.client.add_config_watcher(settings.NACOS["DataId"],settings.NACOS["DataId"],settings.update_cfg)
    serve()
