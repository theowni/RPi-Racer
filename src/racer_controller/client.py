import socket
from command import Command

HOST = '192.168.254.1'
PORT = 6534


class Client:
    def __init__(self):
        pass

    def send_command(self, command):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            raw_command = command.to_raw()
            s.sendall(raw_command)


if __name__ == '__main__':
    client = Client()
    command = Command(b'{}')
    command.speed = 0
    command.direction = 0.5
    command.mode = 'TURBO'
    client.send_command(command)
