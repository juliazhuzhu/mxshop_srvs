from playhouse.pool import PooledMySQLDatabase
from playhouse.shortcuts import ReconnectMixin
import nacos
import json
from loguru import logger
import redis

##to remove my sql gone away issue


class ReconnectMysqlDatabase(ReconnectMixin, PooledMySQLDatabase):
    # pyrthon mro
    pass


NACOS = {
    "Host": "172.20.0.204",
    "Port": 8848,
    "NameSpace": "d34395ae-80c6-440e-a174-af66e53ac664",
    "User": "nacos",
    "Password": "nacos",
    "DataId": "order-srv",
    "Group": "DEV"
}

client = nacos.NacosClient(f'{NACOS["Host"]}:{NACOS["Port"]}', namespace=NACOS["NameSpace"],
                           username=NACOS["User"],
                           password=NACOS["Password"])

data = client.get_config(NACOS["DataId"], NACOS["Group"])
data = json.loads(data)
logger.info(data)

# MYSQL_DB = "mxshop_user_srv"
# MYSQL_HOST = "127.0.0.1"
# MYSQL_PORT = 3306
# MYSQL_USER = "root"
# MYSQL_PASSWORD = "123456"
#
#consul的配置
CONSUL_HOST = data["consul"]["host"]
CONSUL_PORT = data["consul"]["port"]
#
# #服务相关的配置
SERVICE_NAME = data["name"]
SERVICE_TAGS = data["tags"]

REDIS_HOST = data["redis"]["host"]
REDIS_PORT = data["redis"]["port"]
REDIS_DB = data["redis"]["db"]

GOODS_SRV_NAME = data["goods_srv"]["name"]
INVENTORY_SRV_NAME = data["inventory_srv"]["name"]
#配置一个连接池
pool = redis.ConnectionPool(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
REDIS_CLIENT = redis.StrictRedis(connection_pool=pool)

DB = ReconnectMysqlDatabase(data["mysql"]["db"], host=data["mysql"]["host"], port=data["mysql"]["port"],
                            user=data["mysql"]["user"], password=data["mysql"]["password"])


def update_cfg(args):
    logger.info("配置产生变化")
    update_data = json.loads(args)
    logger.info(update_data)

