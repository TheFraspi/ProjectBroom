__author__ = 'spier_000'


class Position:
    """"This class represent the Position of an object"""
    def __init__(self, position):
        self.position = position

    def get_position(self):
        return self.position

    def set_position(self, x, y):
        self.position = [x, y]