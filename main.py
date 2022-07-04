# Средняя сложность алгоритма функции y() - (n+1)*log(n)

def piecewise_func(x, y):
    return Func(x, y)


class Func:
    def __init__(self, x: int, y: int):
        self.points = [(x, y)]

    def __call__(self, x, y):
        self.points.append((x, y))
        return self

    @staticmethod
    def get_koef(p1, p2):
        try:
            a = (p1[1] - p2[1]) / (p1[0] - p2[0])
        except ZeroDivisionError:
            return 0, p1[0]
        b = p1[1] - a * p1[0]
        return a, b

    def y(self, x):
        self.points = sorted(list(self.points), key=lambda x: x[0])
        if x <= self.points[0][0]:
            a, b = self.get_koef(self.points[0], self.points[1])
        elif x >= self.points[-1][0]:
            a, b = self.get_koef(self.points[-2], self.points[-1])
        else:
            for i in range(len(self.points)):
                if x <= self.points[i][0]:
                    a, b = self.get_koef(self.points[i], self.points[i - 1])
                    break
        if not a:
            if b:
                return b
            else:
                if x == b:
                    return ('Y is infinite')
                else:
                    return ('Function does not exist')
        return a * x + b

    def table(self):
        self.points = sorted(list(self.points), key=lambda x: x[0])
        print('-----------------------')
        print('| x1 | x2 |  a  |  b  |')
        print('-----------------------')
        for i in range(len(self.points) - 1):
            a, b = self.get_koef(self.points[i], self.points[i + 1])
            # if not a:
            #     a = '-'
            #     b = '-'
            print(f'| {self.points[i][0]} | {self.points[i + 1][0]} |  {a}  |  {b}  |')
        print('-----------------------')
