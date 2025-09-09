#!/usr/bin/env python3

from pyre import pyre
from pyre import zhelper
import zmq
import uuid
import json

def get_peer_node(username):
    n = pyre(username)
    #n.set_header("chat_header1","example header1")
    #n.set_header("chat_header1","example header1")
    n.start()
    return n

def join_group(node, group):
    node.join(group)
    print(f"joined group: {group}")

    def chat_task(ctx, pipe, n, group):
        poller = zmq.Poller()
        poller.register(pipe, zmq.POLLIN)
        # print(n.socket(), items)
        poller.register(n.socket(), zmq.POLLIN)
        # print(n.socket(), items)
        while(True):
            items = dict(poller.poll())
            # print(n.socket(), items)
            if pipe in items and items[pipe] == zmq.POLLIN:
                message = pipe.recv()
                # message to quit
                if message.decode('utf-8') =="$$STOP":
                    break

                    pip
                    install
                    zeromq - pyre






