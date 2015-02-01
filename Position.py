__author__ = 'spier_000'


class Position:
    """"This class represent the Position of an object"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.coordinate = [x, y]

    def get_position(self):
        return self.coordinate

    def set_position(self, x, y):
        self.coordinate = [x, y]