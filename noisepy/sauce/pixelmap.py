import numpy as np
from scipy import misc as sp


class PixelMap:

    def __init__(self, width, height, _map):
        self.pixel_map = np.zeros((height, width, 3), dtype=np.uint8)
        self.options = {0: [0, 0, 0], 1: [255, 255, 255]}
        self._map = _map

        for y in range(height):
            for x in range(width):
                self.pixel_map[y, x] = self.options[self._map[y][x]]

        self.image = sp.toimage(self.pixel_map)

    def show(self):
        self.image.show()
