from rocketmq.client import Producer, Message

topic = "TopicTest"
def create_message():
    msg = Message(topic)
    msg.set_keys("imoc")
    msg.set_tags("bobby")
    msg.set_delay_time_level(3)
    msg.set_property("name", "jjj")
    msg.set_body("hello 你好")
    return msg


def send_message_sync(count):
    producer = Producer("test")
    producer.set_name_server_address("172.20.0.204:9876")

    # start producer
    producer.start()
    for n in range(count):
        msg = create_message()
        ret = producer.send_sync(msg)
        print(f"send status:{ret.status}, messageId:{ret.msg_id}")

    print("send done!")
    producer.shutdown()


if __name__ == "__main__":

    send_message_sync(5)