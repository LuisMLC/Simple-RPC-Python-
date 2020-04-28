"""
 Simple JSON-RPC Server

"""

import socket
import functions
import json

class JSONRPCServer:
    """The JSON-RPC server."""

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.funcs = {}

    def start(self):
        """Starts the server."""
        sock = socket.socket()
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((self.host, self.port))
        sock.listen(1)
        print('Listening on port %s ...' % self.port)

        # # Map functions
        # funcs = {
        #     'hello': functions.hello,
        #     'hello2': functions.hello2,
        #     'greet': functions.greet,
        #     'add': functions.add,
        # }

        while True:
            # Accept client
            conn, _ = sock.accept()

            # Receive message
            msg = conn.recv(1024).decode()
            print('Received:', msg)

            # Convert to dict
            msg = json.loads(msg)
            method = msg['method']
            params = msg['params']

            # Response
            res = {}

            # Send response
            # LVL3
            # if msg.lower() == 'hello':
            #     res = functions.hello()
            # elif msg.lower() == 'hello2':
            #     res = functions.hello2()
            # elif msg.lower().startswith('greet'):
            #     values = msg.split()
            #     name = values[1]
            #     res = functions.greet(name)
            # elif msg.lower().startswith('add'):
            #     values = msg.split()
            #     a = eval(values[1])
            #     b = eval(values[2])
            #     res = str(functions.add(a, b))
            # else:
            #     res = 'Error'
            # conn.send(res.encode())

            # if method == 'hello':
            #     res['result'] = functions.hello()
            # elif method == 'hello2':
            #     res['result'] = functions.hello2()
            # elif method == 'greet':
            #     name = params[0]
            #     res['result'] = functions.greet(name)
            # elif method.startswith('add'):
            #     a = params[0]
            #     b = params[1]
            #     res['result'] = str(functions.add(a, b))
            # else:
            #     res['error'] = 'Method not found'

            # if method == 'hello':
            #     res['result'] = functions.hello()
            # elif method == 'hello2':
            #     res['result'] = functions.hello2()
            # elif method == 'greet':
            #     name = params[0]
            #     res['result'] = functions.greet(*params)
            # elif method.startswith('add'):
            #     a = params[0]
            #     b = params[1]
            #     res['result'] = str(functions.add(*params))
            # else:
            #     res['error'] = 'Method not found'

            try:
                func = self.funcs[method]
                res['result'] = func(*params)
            except KeyError:
                res = 'Error'

            # Send response
            res = json.dumps(res)
            conn.send(res.encode())

            # Close client connection
            conn.close()


    def register(self, method, func):
        self.funcs[method] = func

if __name__ == "__main__":

    # Test the JSONRPCServer class
    server = JSONRPCServer('0.0.0.0', 8000)
    server.register('add', functions.add)  # LVL 7.4
    server.register('hello', functions.hello)
    server.register('hello2', functions.hello2)
    server.register('greet', functions.greet)
    server.register('sub', functions.sub)
    server.register('mul', functions.mul)
    server.register('div', functions.div)
    server.start()
