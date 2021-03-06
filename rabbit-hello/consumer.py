#!/usr/bin/env python3
# Extracted from: https://www.rabbitmq.com/tutorials/tutorial-one-python.html

import pika


def callback(ch, method, properties, body):
    print("[x] Received: %r" % body.decode("UTF-8"))


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_consume(callback, queue='hello', no_ack=True)

print("[*] Waiting for messages. press Ctrl+C to exit")
channel.start_consuming()
