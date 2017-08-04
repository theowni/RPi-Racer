from subprocess import call


MIN_SPEED = 1400
MAX_SPEED = 1600  # technically max is 2000
SPEED_PIN = 4

MIN_DIRECTION = 1000
MAX_DIRECTION = 2000
DIRECTION_PIN = 12


class CommandController:
    def __init__(self):
        self.current_speed = None
        self.current_direction = None
        self.current_mode = None
        self.reverse_speed = False

    def handle(self, command):
        # TODO
        # normalize parameters of commands by mode here

        self.current_speed = command.speed
        self.current_direction = command.direction
        self.current_mode = command.mode

        self.run_command(command)

    def run_command(self, normalized_command):
        print('Run command: %s' % normalized_command)

        if normalized_command.speed > 0:
            self.reverse_speed = False
            cur_value = MIN_SPEED + normalized_command.speed * \
                (MAX_SPEED - MIN_SPEED)
            cur_value = int(cur_value)

            call("pigs s %s %s" % (SPEED_PIN, cur_value), shell=True)
            self.current_speed = cur_value
        elif normalized_command.speed < 0:
            if not self.reverse_speed:
                call("pigs s %s 500" % (SPEED_PIN,), shell=True)
                call("pigs s %s 1400" % (SPEED_PIN,), shell=True)
                self.reverse_speed = True
            call("pigs s %s 1250" % (SPEED_PIN,), shell=True)
        else:
            self.reverse_speed = False
            call("pigs s %s 1400" % (SPEED_PIN,), shell=True)

        cur_value = MIN_DIRECTION + normalized_command.direction * \
            (MAX_DIRECTION - MIN_DIRECTION)
        cur_value = int(cur_value)

        call("pigs s %s %s" % (DIRECTION_PIN, cur_value), shell=True)
        self.current_direction = cur_value
