import time
from client import Client
from command import Command
from controller import Controller


class AppController:
    controller = Controller()
    client = Client()

    def __init__(self):
        pass

    def run(self):
        while True:
            params = self.controller.get_all_params()
            self.controller.get_lstick_coord(params)
            rt_coord = self.controller.get_lstick_coord(params)
            norm = self.controller.get_dir_norm(rt_coord)
            speed = self.controller.get_speed_percentage(params)
            command = Command(b'{}')
            # TODO
            # set speed here
            command.speed = speed
            command.direction = norm
            command.mode = 'normal'
            self.client.send_command(command)
            # TODO
            # let it be smarter than this :)
            time.sleep(0.05)


appController = AppController()
appController.run()
