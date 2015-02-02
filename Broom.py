__author__ = 'spier_000'

import math

init_position = [0, 0]

class Position:
    """"This class represent the Position of an object"""
    def __init__(self, position):
        self.position = position

    def get_position(self):
        return self.position

    def set_position(self, x, y):
        self.position = [x, y]


class Broom(Position):
    def __init__(self, heading, old_position=init_position):
        self.heading = heading
        self.pos1 = old_position
        super(Broom, self).__init__(old_position)
        self.velocity = 0
        self.pos2 = [0, 0]

    def calc_velocity(self):
        pass

    def calc_position(self, pos_a, pos_b, pos_c, angle_a, angle_b, angle_c):
        x1 = pos_a[0]
        y1 = pos_a[1]
        x2 = pos_b[0]
        y2 = pos_b[1]
        x3 = pos_c[0]
        y3 = pos_c[1]
        alpha1 = angle_a
        alpha2 = angle_b
        alpha3 = angle_c

        # STEP 1: Compute the modified beacon coordinates
        xmod1 = x1 - x2
        ymod1 = y1 - y2
        xmod3 = x3 - x2
        ymod3 = y3 - y2

        # STEP 2: Compute the three cot(.). Remember: cot(alpha) = 1 / tan (alpha)
        t12 = 1 / math.tan(alpha2-alpha1)
        t23 = 1 / math.tan(alpha3-alpha2)
        t31 = (1 - t12*t23)/(t12+t23)

        # STEP 3:
        xmod12 = xmod1 + t12*ymod1
        ymod12 = ymod1 - t12*xmod1
        xmod23 = xmod3 - t23*ymod3
        ymod23 = ymod3 + t23*xmod3
        xmod31 = (xmod3 + xmod1) + t31*(ymod3 - ymod1)
        ymod31 = (ymod3 + ymod1) - t31*(xmod3 - xmod1)

        # STEP 4:
        kmod31 = xmod1*xmod3 + ymod1*ymod3 + t31*(xmod1*ymod3 - xmod3*ymod1)

        # STEP 5:
        d = (xmod12 - xmod23)*(ymod23 - ymod31) - (ymod12 - ymod23)*(xmod23 - xmod31)

        # STEP 6: Compute broom position {x, y} and return
        self.position = [x2 + (kmod31*(ymod12 - ymod23))/d, y2 + (kmod31*(xmod23 - xmod12))/d]
        return self.position

    def run(self):
        pass

class Beacon(Position):
    def __init__(self, position, signals):
        super(Beacon, self).__init__(position)
        self.signals = signals

if __name__ == "__main__":
    starting_position = [5, 5]
    starting_heading = [0, -1]
    beacon1_pos = [10, 0]
    beacon2_pos = [10, 10]
    beacon3_pos = [0, 10]
    b = Broom(starting_heading, starting_position)

    b1 = Beacon(beacon1_pos, [40, 40, 40, 40, 40, 40, 40])
    b2 = Beacon(beacon2_pos, [135, 135, 135, 135, 135, 135, 135])
    b3 = Beacon(beacon3_pos, [225, 225, 225, 225, 225, 225, 225])

    for t in range(0, 7, 1):
        print(b.pos2)
        b.pos2 = b.calc_position(b1.position, b2.position, b3.position, b1.signals[t], b2.signals[t], b3.signals[t])
        print(b1.signals[t])
        print(b.pos2)

