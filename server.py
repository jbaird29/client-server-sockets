from socket import socket, AF_INET, SOCK_STREAM

# USED: https://docs.python.org/3/library/socket.html
# FOR: learning the socket API library functions (modified from)
# DATE: 3/07/2022

class HTTPServer:
    def __init__(self, port: int) -> None:
        self._port = port

    def run(self) -> None:
        # open a listening socket, close upon termination
        with socket(AF_INET, SOCK_STREAM) as s:
            print(f"Server listening localhost on port {self._port}")
            s.bind(('', port))
            s.listen(1)
            # continuously accept new connections until program termination
            while True:
                conn, addr = s.accept()
                print(f"Connected by {addr}")
                print()
                self._begin_chat_socket(conn)

    def _begin_chat_socket(self, sock: socket):
        # open the connection socket, close upon termination
        with sock:
            # read and print the message
            print("Waiting for message...")
            req_data = sock.recv(4096)
            print(req_data)
            print("Enter message to send or type /q to quit:")
            # get the first input
            response = input(">")
            while response != "/q":
                # send the response
                sock.sendall(response)
                # get another reply
                req_data = sock.recv(4096)
                print(req_data)
                response = input(">")
                # TODO - implement handling of connection closure by client
                # TODO - add message length header (implement as a class?)


if __name__ == '__main__':
    port = 51119
    server = HTTPServer(port)
    server.run()
