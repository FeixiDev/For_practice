import pytest

def func(x):
    return x + 1

def a():
    return 'zane'


def test_answer():
    assert func(3) == 4

# 基本用法
def test_base():
	assert ("zane", a())

def test_in():
	assert 'a' in 'happy ending'

def test_str():
	assert 'zane' == 'zane'

def test_small():
	assert 3 < 5

def test_big():
	assert 5 > 3

# if __name__ == "__main__" :
# 	print("a")