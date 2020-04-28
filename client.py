"""
 Simple JSON-RPC Client

"""

import socket
import json


def invoke(method, params):
    req = {
        'method': method,
        'params': params
    }
    if json.dumps(req) == 'Error':
        raise AttributeError('Remote method unavailable')
    else:
        return json.dumps(req)


class JSONRPCClient:
    """The JSON-RPC client."""

    def __init__(self, host, port):
        self.sock = socket.socket()
        self.sock.connect((host, port))

    def send(self, msg):
        """Sends a message to the server."""
        self.sock.sendall(msg.encode())
        return self.sock.recv(1024).decode()

    # def add(self, a, b):
    #     return self.send(invoke('add', [a, b]))

    def __getattr__(self, name):
        """Invokes a generic function."""
        def inner(*params):
            return self.send(invoke(name, params))
        return inner


if __name__ == "__main__":

    #while True:
        # Test the JSONRPCClient class
        client = JSONRPCClient('127.0.0.1', 8000)
        #msg = input('> ')
        #res = client.send('{"method": "add", "params": [2, 3]}')
        #res = client.send('{"method": "hello", "params": []}')
        #res = client.send('{"method": "greet", "params": ["Manuel"]}')
        #res = client.send('{"method": "qwe", "params": [2, 3]}')
        #res = client.send('{"method": "mul", "params": [2, 3]}')
        #res = client.send(invoke('add', [2, 3]))
        res = client.add(2, 3)
        print(res)
