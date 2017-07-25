import json


class Command:
    speed = None
    direction = None
    mode = None

    def __init__(self, binary_data):
        data_dict = self.from_raw(binary_data)
        self.speed = data_dict.get('speed', None)
        self.direction = data_dict.get('direction', None)
        self.mode = data_dict.get('mode', None)

    def to_raw(self):
        dict_to_bin = {
            'speed': self.speed,
            'direction': self.direction,
            'mode': self.mode
        }

        return json.dumps(dict_to_bin).encode('utf-8')

    def from_raw(self, binary_data):
        data_dict = json.loads(binary_data.decode('utf-8'))

        return data_dict

    def __str__(self):
        return 'speed: %s, direction: %s, mode: %s' \
            % (self.speed, self.direction, self.mode)


if __name__ == '__main__':
    command = Command('{}')
    command.speed = 20
    command.direction = 30
    command.mode = 'TURBO'

    bin_com = command.to_raw()
    print(bin_com)

    from_bin = Command(bin_com)
    print(from_bin)
