from socket import socket, AF_INET, SOCK_STREAM

# USED: https://docs.python.org/3/library/socket.html
# FOR: learning the socket API library functions (adapted from)
# DATE: 1/11/2022

class ChatClient:
    def __init__(self, server_port: int, server_host: bytes = b"localhost") -> None:
        self._server_port = server_port
        self._server_host = server_host

    def run(self) -> None:
        with socket(AF_INET, SOCK_STREAM) as s:
            s.connect((self._server_host, self._server_port))
            print("Connected to:", self._server_host, "on port:", self._server_port)
            print("Type /q to quit")
            print("Enter message to send...")
            message = input(">")
            while message != "/q":
                # send the message
                s.sendall(message.encode("UTF-8"))
                # receive response, 4096 bytes at a time, until there is no data left
                # TODO - implement handling of connection closure by client
                # TODO - add message length header (implement as a class?)
                data = bytearray()
                response = s.recv(4096)
                while len(response) > 0:
                    data.extend(response)
                    response = s.recv(4096)
                print(data.decode())
                # get a new message
                message = input(">")


if __name__ == '__main__':
    port = 51119
    client = ChatClient(port)
    client.run()
