from socket import socket
from string import digits

class MessagingInterfaceException(BaseException):
    pass

class MessagingInterface:
    def __init__(self, sock: socket):
        """
        Constructs an interface to interact with the socket; use the methods receive() and send()
        :param sock: the socket that messages are being sent to and received from
        """
        self.sock: socket = sock

    def receive(self) -> str:
        """Receives the byte stream from the socket and returns the message"""
        # get the length of the message - contained in the first four bytes
        length = self.sock.recv(4)
        try:
            length = int.from_bytes(length, byteorder="big")
        except ValueError:
            raise MessagingInterfaceException("Length was an invalid number.")
        # receive the message with that given length
        raw_message = bytearray()
        received_count = 0
        while received_count < length:
            chunk_size = min(4096, length - received_count)  # TODO - test this with a small power of 2 (eg 8)
            chunk = self.sock.recv(chunk_size)
            raw_message.extend(chunk)
            received_count += len(chunk)
        message = raw_message.decode("UTF-8")
        return message

    def send(self, message: str) -> None:
        """Given a message, sends it into the socket"""
        if type(message) != str:
            raise MessagingInterfaceException("Message must be a str data type.")
        # construct message, which is a 4-byte header of length + the raw message data as bytes
        raw_message = message.encode("UTF-8")
        length = len(raw_message).to_bytes(4, byteorder="big")
        self.sock.sendall(length)
        self.sock.sendall(raw_message)
