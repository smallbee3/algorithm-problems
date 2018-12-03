
"""
핑퐁 게임
(반드시 Python으로 작성할 것)

일련의 숫자가 있고, 이 숫자는 1씩 증가, 또는 감소한다.
n번째의 숫자가 있을 시에, 이 숫자가 7의 배수(7, 14, 21,...)거나
7이란 숫자를 포함할 시에 (7, 17, 27,...) 방향을 바꾼다.

즉, 1, 2, 3, 4, 5, 6, [7], 6, 5, 4, 3, 2, 1, [0], 1, 2, [3], 2, 1, 0, [-1], 0, 1
과 같이 숫자는 진행한다. (첫 번째 7은 7번째, 두 번째 0은 14번째, 세 번째 3은 17번째, 네 번째 -1은 21번째)

다음의 제약 하에 pingpong(x)의 함수를 작성하라. 예시의 인풋과 아웃풋은 다음과 같다.

pingpong(8) = 6
pingpong(22) = 0
pingpong(68) = 2
pingpong(100) = 2

For Loop 또는 Array를 쓰지 말 것.
Assignment를 쓰지 말 것. 즉, 변수 할당을 하지 말 것.
String을 쓰지 말것.


def pingpong(x):

    return num

"""


# 1, 2, 3, 4, 5, 6, [7], 6, 5, 4, 3, 2, 1, [0], 1, 2, [3], 2, 1, 0, [-1], 0, 1  2  3  4  5  4  5
# 1  2  3  4  5  6   7   8  9  10 11 12 13  14  15 16  17  18 19 20  21   22 23 24 25 26 27 28 29

# 7 14 21 28 35 42 49 56 63 70 77 84 91

# 7
# 17
# 27
# 37
# 47
# 57
# 67
# 70 71 72 ... 79
# 87
# 97
# 107
# 117
# 127
# ...
# 170, 171, 172, 173, 174 ... 179
# ...
# 701, 702, 703, 704, 705, 706, 707, ... , 712,


# 1)
# def pingpong(x):
#     num = 0
#     nth = x
#     if x % 7 == 0:
#         pass
#     seven_nummber = x // 7
#     return num


# 2) dict
# adict = {}
# def pingpong(x):
#   if not adict.get(x):
#         adict[x] = 1


"""
2018.12.03

Time : 78 minutes

Learning
    1. recursion + recursion
    2. the usage of *args

"""

# 3) recursion with *args


def does_x_contain_seven(x):

    if (x - 7) % 10 == 0:
        return True

    if x < 10:
        return False

    return does_x_contain_seven(x // 10)


def pingpong(x, *args):

    if not args:
        if x == 1:
            return 1
        return pingpong(x, 2, 2, 1)

    if args[0] == x:
        return args[1]

    # multiple of seven
    if args[0] % 7 == 0:
        return pingpong(x, args[0] + 1, args[1] - args[2], -args[2])

    # with seven
    if does_x_contain_seven(args[0]):
        return pingpong(x, args[0] + 1, args[1] - args[2], -args[2])

    return pingpong(x, args[0] + 1, args[1] + args[2], args[2])


if __name__ == '__main__':

    result = pingpong(1)
    print(f'expected: 1 | result: {result}')

    result = pingpong(7)
    print(f'expected: 7 | result: {result}')

    result = pingpong(8)
    print(f'expected: 6 | result: {result}')

    result = pingpong(14)
    print(f'expected: 0 | result: {result}')

    result = pingpong(17)
    print(f'expected: 3 | result: {result}')

    result = pingpong(21)
    print(f'expected: -1 | result: {result}')

    result = pingpong(22)
    print(f'expected: 0 | result: {result}')

    result = pingpong(68)
    print(f'expected: 2 | result: {result}')

    result = pingpong(100)
    print(f'expected: 2 | result: {result}')
