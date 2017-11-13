from noisepy.sauce import Tableau, PixelMap
from optparse import OptionParser


parser = OptionParser("usage: python3 -m noisepy [options] arg1 arg2 arg3", version="%prog 0.1.4.2")
parser.add_option("-r", "--rows", dest="height", type=int, help="set height of image", metavar="HEIGHT")
parser.add_option("-c", "--columns", dest="width", type=int, help="set width of image", metavar="WIDTH")
parser.add_option("-b", "--black", dest="black", type=float, help="set black ration", metavar="RATIO")

(options, args) = parser.parse_args()


width = int
height = int
p_black = None
table = None
data_map = None


def get_input():
    global width, height, p_black, parser
    if options.height is None:
        height = int(input("image height(pixel): "))
    else:
        height = options.height
    if options.width is None:
        width = int(input("image width(pixel): "))
    else:
        height = options.height
    if options.black is None:
        p_black = float(input("black ratio(0.X): "))
        if p_black == 0:
            p_black = None
    else:
        p_black = options.black


def get_table():
    global table
    table = Tableau(width, height, p_black)


def get_map():
    global data_map, table
    data_map = PixelMap(table.width, table.height, table.get_map())


def main():
    get_input()
    get_table()
    get_map()
    data_map.show()
    # data_map.resize(2.0)


if __name__ == "__main__":

    main()
