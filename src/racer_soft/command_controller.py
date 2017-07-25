from subprocess import call


MIN_SPEED = 1400
MAX_SPEED = 2000
SPEED_PIN = 4

MIN_DIRECTION = 1000
MAX_DIRECTION = 2000
DIRECTION_PIN = 12


class CommandController:
    current_speed = None
    current_direction = None
    current_mode = None

    def __init__(self):
        pass

    def handle(self, command):
        # TODO
        # normalize parameters of commands by mode here

        self.current_speed = command.speed
        self.current_direction = command.direction
        self.current_mode = command.mode

        self.run_command(command)

    def run_command(self, normalized_command):
        print('Run command: %s' % normalized_command)

        if self.current_speed != normalized_command.speed:
            cur_value = MIN_SPEED + normalized_command.speed * \
                (MAX_SPEED - MIN_SPEED)
            cur_value = int(cur_value)

            call("pigs s %s %s" % (SPEED_PIN, cur_value), shell=True)
            self.current_speed = cur_value

        if self.current_direction != normalized_command.direction:
            cur_value = MIN_SPEED + normalized_command.direction * \
                (MAX_DIRECTION - MIN_DIRECTION)
            cur_value = int(cur_value)

            call("pigs s %s %s" % (DIRECTION_PIN, cur_value), shell=True)
            self.current_direction = cur_value
