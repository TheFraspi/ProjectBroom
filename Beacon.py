__author__ = 'spier_000'

import Position


class Beacon(Position):
    """Beacon is a class that inherits from Position class"""
    def __init__(self, name):
        self.name = name

    def transmit(self):

