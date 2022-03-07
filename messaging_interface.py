from socket import socket
from string import digits

class MessagingInterfaceException(BaseException):
    pass

class MessagingInterface:
    _TERMINATION_SYMBOL = "/q"

    def __init__(self, sock: socket):
        """
        Constructs an interface to interact with the socket; use the methods receive() and send()
        :param sock: the socket that messages are being sent to and received from
        """
        self._sock: socket = sock
        self._is_open = True

    def receive(self) -> str:
        """Receives the byte stream from the socket and returns the message"""
        # get the length of the message - contained in the first four bytes
        length = self._sock.recv(4)
        try:
            length = int.from_bytes(length, byteorder="big")
        except ValueError:
            raise MessagingInterfaceException("Length was an invalid number.")
        # receive the message with that given length
        raw_message = bytearray()
        received_count = 0
        while received_count < length:
            chunk_size = min(4096, length - received_count)
            chunk = self._sock.recv(chunk_size)
            raw_message.extend(chunk)
            received_count += len(chunk)
        message = raw_message.decode("UTF-8")
        if message == self._TERMINATION_SYMBOL:
            self._is_open = False
        return message

    def send(self, message: str) -> None:
        """Given a message, sends it into the socket"""
        if type(message) != str:
            raise MessagingInterfaceException("Message must be a str data type.")
        if message == self._TERMINATION_SYMBOL:
            self._is_open = False
        # construct message, which is a 4-byte header of length + the raw message data as bytes
        raw_message = message.encode("UTF-8")
        length = len(raw_message).to_bytes(4, byteorder="big")
        self._sock.sendall(length)
        self._sock.sendall(raw_message)

    def is_open(self):
        return self._is_open
