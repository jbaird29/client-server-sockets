from socket import socket, AF_INET, SOCK_STREAM
from messaging_interface import MessagingInterface

# USED: https://docs.python.org/3/library/socket.html
# FOR: learning the socket API library functions (adapted from)
# DATE: 3/07/2022

class ChatClient:
    def __init__(self, server_port: int, server_host: bytes = b"localhost") -> None:
        self._server_port = server_port
        self._server_host = server_host

    def run(self) -> None:
        with socket(AF_INET, SOCK_STREAM) as sock:
            sock.connect((self._server_host, self._server_port))
            print("Connected to:", self._server_host, "on port:", self._server_port)
            interface = MessagingInterface(sock)
            print("Type /q to quit")
            print("Enter message to send...")
            message = input(">")
            while message != "/q":
                # TODO - implement handling of connection closure by client
                interface.send(message)
                print(interface.receive())
                message = input(">")


if __name__ == '__main__':
    port = 51119
    client = ChatClient(port)
    client.run()
