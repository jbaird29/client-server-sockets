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
            # accept only a single connection, terminate server when that connection terminates
            conn, addr = s.accept()
            print(f"Connected by {addr}", end="\n\n")
            self._begin_chat(conn)

    @staticmethod
    def _begin_chat(sock: socket) -> None:
        # open the connection socket, close upon termination
        with sock:
            interface = MessagingInterface(sock)
            print("When prompted for a message, type /q to quit.")
            print("Waiting for message...")
            # continuously receive and reply until termination symbol is encountered
            while interface.is_open():
                received_msg = interface.receive()
                if interface.is_open():
                    print(received_msg)
                    send_message = input(">")
                    interface.send(send_message)
            return


if __name__ == '__main__':
    port = 51125
    server = ChatServer(port)
    server.run()
