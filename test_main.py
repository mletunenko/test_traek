from main import piecewise_func
from main import Func


def test_create_func_one_point():
    F = piecewise_func(0, 100)
    assert F.points == [(0, 100)]


def test_create_func_three_point():
    F = piecewise_func(0, 100)(10, 122)(30, 0)
    assert F.points == [(0, 100), (10, 122), (30, 0)]


def test_add_one_point():
    F = piecewise_func(0, 100)
    F = F(10, 122)
    assert F.points == [(0, 100), (10, 122)]


def test_get_y():
    F = piecewise_func(0, 100)(10, 122)
    assert F.y(5) == 111


def test_get_y_inf():
    F = piecewise_func(0, 100)(0, 0)
    assert F.y(0) == 'Y is infinite'


def test_get_y_not_exist():
    F = piecewise_func(0, 100)(0, 0)
    assert F.y(5) == 'Function does not exist'


def test_get_y_max_border():
    F = piecewise_func(0, 5)(3, 2)(6, 2)
    assert F.y(8) == 2


def test_get_y_min_border():
    F = piecewise_func(0, 5)(3, 2)(6, 2)
    assert F.y(-5) == 10
