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
        # open the connection socket, close upon termination
        with socket(AF_INET, SOCK_STREAM) as sock:
            sock.connect((self._server_host, self._server_port))
            print("Connected to:", self._server_host.decode(), "on port:", self._server_port, end="\n\n")
            interface = MessagingInterface(sock)
            # send the first message
            print("Send a message, or type /q to quit.")
            send_message = input(">")
            interface.send(send_message)
            # continuously receive and reply until termination symbol is encountered
            while interface.is_open():
                received_msg = interface.receive()
                if interface.is_open():
                    print(received_msg)
                    send_message = input(">")
                    interface.send(send_message)


if __name__ == '__main__':
    port = 51125
    client = ChatClient(port)
    client.run()
