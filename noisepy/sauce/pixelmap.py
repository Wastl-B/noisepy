import numpy as np
from scipy import misc as sp
from time import strftime
from os import path, mkdir
from scipy.ndimage import zoom


class PixelMap:

    def __init__(self, width, height, _map):
        self.pixel_map = np.zeros((height, width, 3), dtype=np.uint8)
        self.options = {0: [0, 0, 0], 1: [255, 255, 255]}
        self._map = _map

        for y in range(height):
            for x in range(width):
                self.pixel_map[y, x] = self.options[self._map[y][x]]

        # self.image = sp.toimage(self.pixel_map)

    def show(self):
        sp.imshow(self.pixel_map)
        # self.image.show()

    def resize(self, factor):
        sp.toimage(sp.imresize(self.image, factor)).show()

    def save(self):
        _path = path.join(path.expanduser('~'), 'NoisePy')

        if not path.isdir(_path):
            mkdir(_path)

        name = strftime("%Y-%m-%d_%H-%M-%S") + '.png'
        filename = path.join(_path, name)
        sp.imsave(filename, self.pixel_map)

        print('file saved to ' + filename)
