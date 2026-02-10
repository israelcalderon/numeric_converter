from collections import deque
from math import remainder

from numeric_converter.base_character import base_map


class BaseNotSupported(Exception):
    pass


def base_character(number: int) -> str:
    """
    Returns the character assigned to the providen number in Base R
    
    :param number: Number to be "converted" to base R
    :type number: int
    :return: converted number
    :rtype: str
    """
    if number < 10:
        return str(number)

    if number > len(base_map) + 9:
        raise BaseNotSupported(f'Base {number} is not suported')

    return chr(base_map[number])


def base_10_to_r_int(number: int, base: int) -> str:
    """
    Converts number in base 10 to base (R)
    Note: only integer part
    
    :param number: Number to be converted
    :type number: int
    :param base: Base to convert number, eg: bin = 2, hex = 16
    :type base: int
    :return: the number converted to base requested
    :rtype: str
    """
    result = deque()
    quotient = int(number)

    if quotient == 0:
        return '0'

    while quotient != 0:
        remainder = quotient % base
        quotient = quotient // base
        result.appendleft(base_character(remainder))

    return ''.join(result)


def base_10_to_r_dec(number: float, base: int) -> str:
    """
    Converts number in base 10 to base (R)
    Note: only for the number decimal part
    
    :param number: Number to be converted
    :type number: float
    :param base: Base to convert number, eg: bin = 2, hex = 16
    :type base: int
    :return: the number converted to base requested
    :rtype: str
    """
    result = []
    fraction = number

    while fraction != 0:
        product = fraction * base
        integer = int(product)
        fraction = product - integer
        result.append(base_character(integer))

    return ''.join(result)


def base_10_to_r(number: float, base: int) -> str:
    integer_num = int(number)
    fractionary_part = number - integer_num
    return f"{base_10_to_r_int(int(number), base)}.{base_10_to_r_dec(fractionary_part, base)}"
