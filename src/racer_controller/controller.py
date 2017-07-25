from math import sqrt
import pygame
import numpy as np

pygame.init()
joy = pygame.joystick.Joystick(0)
joy.init()
print('Initialized Joystick : %s' % joy.get_name())


class Controller:
    def __init__(self):
        pass

    def get_all_params(self):
        out = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        it = 0  # iterator
        pygame.event.pump()
        # Read input from the two joysticks
        for i in range(0, joy.get_numaxes()):
            out[it] = joy.get_axis(i)
            it += 1
        # Read input from buttons
        for i in range(0, joy.get_numbuttons()):
            out[it] = joy.get_button(i)
            it += 1
        return out

    def get_lstick_coord(self, params):
        coords = params[0:2]
        return coords

    def get_rt(self, params):
        return params[11]

    def get_lt(self, params):
        # TODO
        pass

    def get_dir_norm(self, v1):
        v2 = [-1, 0]

        """ Returns the angle in radians between vectors 'v1' and 'v2'::
            angle_between((1, 0, 0), (0, 1, 0))
            1.5707963267948966
            angle_between((1, 0, 0), (1, 0, 0))
            0.0
            angle_between((1, 0, 0), (-1, 0, 0))
            3.141592653589793
        """
        v1_u = self.unit_vector(v1)
        v2_u = self.unit_vector(v2)
        angle = np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))

        if np.isnan(angle):
            return 0.5
        else:
            return angle/np.pi

    def get_speed_percentage(self, params):
        coords = params[2:4]
        length = sqrt(coords[0]**2 + coords[1]**2)
        percentage_speed = length

        return percentage_speed

    def unit_vector(self, vector):
        """ Returns the unit vector of the vector.  """
        return vector / np.linalg.norm(vector)


if __name__ == '__main__':
    controller = Controller()
    while True:
        params = controller.get_all_params()
        controller.get_lstick_coord(params)
        rt_coord = controller.get_lstick_coord(params)

        print(controller.get_dir_norm(rt_coord))
