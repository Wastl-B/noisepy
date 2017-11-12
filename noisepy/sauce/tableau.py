from secrets import choice as randcho


class Tableau:

    def __init__(self, width, height, p_black, p_tolerance):
        self.width = width
        self.height = height
        self.p_black = p_black
        self.p_tolerance = p_tolerance
        self.table = [[0 for _ in range(width)] for _ in range(height)]
        self.options = {0: self.zero, 1: self.one}
        self.row_count = [0, 0]
        self.t_count = [0, 0]
        self.choices = []
        for i in range(100):
            if i <= p_black * 100:
                self.choices.append(0)
            else:
                self.choices.append(1)

        self.gen_table()

        print(self.table)
        print(self.t_count[0] / (self.width * self.height))

    def gen_table(self):
        while self.check_p():
            for y in range(0, self.height):
                self.gen_row(y)
                print(self.row_count)

    def gen_row(self, y):
        self.rowc_reset()
        for x in range(0, self.width):
            r = randcho(self.choices)
            self.options[r](x, y)
        if self.row_count[0] is 0 or self.row_count[1] is 0:
            self.gen_row(y)

    def zero(self, x, y):
        self.row_count[0] += 1
        self.t_count[0] += 1
        self.table[y][x] = 0

    def one(self, x, y):
        self.row_count[1] += 1
        self.t_count[1] += 1
        self.table[y][x] = 1

    def rowc_reset(self):
        self.row_count[0] = 0
        self.row_count[1] = 0

    def check_p(self):
        _p = self.t_count[0] / (self.width * self.height)
        if _p <= self.p_black - self.p_tolerance or _p >= self.p_black + self.p_tolerance:
            return True
        else:
            return False

    def get_map(self):
        return self.table
