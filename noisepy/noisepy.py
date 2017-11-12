from noisepy.sauce.pixelmap import PixelMap
from noisepy.sauce.tableau import Tableau

width = int
height = int
p_black = float
p_tolerance = 0.02  # float
table = None
data_map = None


def get_input():
    global width, height, p_black, p_tolerance
    width = int(input("table width: "))
    height = int(input("table height: "))
    p_black = float(input("%black in 0.x: "))
    # p_tolerance = float(input("%tolerance: "))


def get_table():
    global table
    table = Tableau(width, height, p_black, p_tolerance)


def get_map():
    global data_map, table
    data_map = PixelMap(table.width, table.height, table.get_map())


def noisey():
    get_input()
    get_table()
    get_map()
    data_map.show()
