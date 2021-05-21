# -*- coding: utf-8 -*-
INTEGER = ["零", "一", "二", "三", "四", "五", "六", "七", "八", "九", "十"]
LING = "零"
TEN = "十"
HUNDRED = "百"
THOUSAND = "千"
WAN = "万"
BILL = "亿"
NEGATIVE = "负"
YI = "一"

def get_digit(num: int, index: int):
    """ 
    >>> get_digit(12345, 5)
    1
    >>> get_digit(12345, 6)
    -1
    >>> get_digit(10345, 4)
    0
    """
    target = str(num)
    if index > len(target):
        return -1
    return int(target[-index])

def power_of_ten(power):
    """
    >>> power_of_ten(5)
    10000
    >>> 12345 % power_of_ten(5)
    2345
    >>> 10234 % power_of_ten(5)
    234
    """
    if power <= 0:
        return 0
    return 10 ** (power - 1)

def count_digit(num: int):
    """
    >>> count_digit(12345)
    5
    >>> count_digit(0)
    0
    >>> count_digit(-12345)
    5
    """
    if num == 0:
        return 0
    if num < 0:
        num = -1 *num
    return len(str(num))

def number_intepreter(num: int):
    """ """
    if num == 0:
        return INTEGER[0]
    alpha = simple_number_convert(num // power_of_ten(9))
    beta = simple_number_convert((num % power_of_ten(9)) // power_of_ten(5))
    simple = simple_number_convert(num % power_of_ten(5))
    return ((alpha + BILL) if alpha != INTEGER[0] else "") + ((beta + WAN) if beta != INTEGER[0] else "") + (LING if beta == LING and simple != LING else "") + (simple if simple != INTEGER[0] else "")

def simple_number_convert(num):
    """ 
    prerequest: 0 <= abs(num) < 9999
    >>> simple_number_convert(1000)
    '一千'
    >>> simple_number_convert(1113)
    '一千一百一十三'
    >>> simple_number_convert(1013)
    '一千零十三'
    """
    if not isinstance(num, int):
        raise TypeError(f"{num} is not a integer")
    if not (0 <= abs(num) <= 9999):
        raise ValueError(f"{num} out of range")

    if num < 0:
        return NEGATIVE + simple_number_convert(-1 * num)

    if 0 <= num <= 10:
        return INTEGER[num]
    elif 10 < num <= 99:
        return (INTEGER[get_digit(num, 2)] if get_digit(num, 2) != 1 else "") + TEN + (INTEGER[get_digit(num, 1)] if get_digit(num, 1) != 0 else "")
    elif 100 <= num <= 999:
        rest = simple_number_convert(num % power_of_ten(3))
        return INTEGER[get_digit(num, 3)] + HUNDRED + (LING if get_digit(num, 2) == 0 else "")+ (YI if get_digit(num, 2) == 1 else "") + (rest if rest != INTEGER[0] else "")
    elif 1000 <= num <= 9999:
        rest = simple_number_convert(num % power_of_ten(4))
        return INTEGER[get_digit(num, 4)] + THOUSAND + (LING if get_digit(num, 3) == 0 and rest != INTEGER[0] else "") + (rest if rest != INTEGER[0] else "")
    else:
        raise Exception("should not be here")



if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
    # for i in range(-99, 100):
    #     print(simple_number_convert(i))
    print(number_intepreter(0))
    # print(power_of_ten(9))















