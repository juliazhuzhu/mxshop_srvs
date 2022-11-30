import time
from rocketmq.client import TransactionMQProducer, Message, TransactionStatus

topic = "TopicTest"
def create_message():
    msg = Message(topic)
    msg.set_keys("imoc")
    msg.set_tags("bobby")
    msg.set_property("name", "jjj")
    msg.set_body("hello 你好")
    return msg

def check_msg(msg):
    #消息回查
    print(f"事务消息回查 :{msg.set_body.decode('utf-8')}")
    return TransactionStatus.COMMIT

def local_execute(msg, userArgs):
    #这里执行业逻辑，订单插入，清空购物车
    print("执行本地事务逻辑")
    return TransactionStatus.COMMIT

#发送事务消息
def send_transaction_msg(count):
    producer = TransactionMQProducer("test",check_msg)
    producer.set_name_server_address("172.20.0.204:9876")

    # start producer
    producer.start()
    for n in range(count):
        msg = create_message()
        ret = producer.send_message_in_transaction(msg,local_execute,None)
        print(f"send status:{ret.status}, messageId:{ret.msg_id}")

    print("send done!")
    while True:
        time.sleep(3600)


if __name__ == "__main__":
    #发送事务消息
    send_transaction_msg(1)