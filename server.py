from socket import socket, AF_INET, SOCK_STREAM
from messaging_interface import MessagingInterface

# USED: https://docs.python.org/3/library/socket.html
# FOR: learning the socket API library functions (modified from)
# DATE: 3/07/2022

class ChatServer:
    def __init__(self, listening_port: int) -> None:
        self._port = listening_port

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

    @staticmethod
    def _begin_chat(sock: socket):
        # open the connection socket, close upon termination
        with sock:
            interface = MessagingInterface(sock)
            # read and print the message
            print("Waiting for message...")
            print(interface.receive())
            print("Enter message to send or type /q to quit:")
            # get the first input
            message = input(">")
            while message != "/q":
                # TODO - implement handling of connection closure by client
                interface.send(message)
                print(interface.receive())
                message = input(">")


if __name__ == '__main__':
    port = 51119
    server = ChatServer(port)
    server.run()
