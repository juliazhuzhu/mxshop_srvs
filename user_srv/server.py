import os.path
import signal
import sys
import os
import grpc
from concurrent import futures
import argparse

BASE_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
print(BASE_DIR)
sys.path.insert(0,BASE_DIR)

from user_srv.proto import user_pb2_grpc
from user_srv.handler.user import UserServicer

from loguru import logger



def on_exit(sigo, frame):
    logger.info("进程中断")
    sys.exit(0)

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
                        default=50051,
                        help="the listening port")

    args = parser.parse_args()
    print(args)

    logger.add("logs/user_srv_{time:YYYY-MM-DD_HH:mm:ss}.log", rotation="10 MB")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServicer_to_server(UserServicer(),server)
    server.add_insecure_port(f'{args.ip}:{args.port}')
    logger.info(f"启动服务 {args.ip}:{args.port}")
    '''
        SIGINT ctrl+c
        SIGTERM kill 发出的软件终止命令
    '''
    signal.signal(signal.SIGINT,on_exit)
    signal.signal(signal.SIGTERM, on_exit)
    server.start()
    server.wait_for_termination()


@logger.catch
def my_function(x, y, z):
    return 1/(x+y+z)

if __name__ == '__main__':
    # my_function(0,0,0)
    serve()
