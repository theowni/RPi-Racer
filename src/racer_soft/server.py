import queue
import asyncore
import socket
from command import Command
from command_controller import CommandController

commandController = CommandController()


class CommandHandler(asyncore.dispatcher_with_send):
    def handle_read(self):
        data = self.recv(8192)
        if data:
            # print(data)
            command = Command(data)
            # print(command)
            commandController.handle(command)


class Server(asyncore.dispatcher):
    commandQueue = queue.Queue()

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)

    def handle_accept(self):
        pair = self.accept()
        if pair is not None:
            sock, addr = pair
            # print('Incoming connection from %s' % repr(addr))
            CommandHandler(sock)


if __name__ == '__main__':
    server = Server('0.0.0.0', 6534)
    asyncore.loop()
