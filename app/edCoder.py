from math import floor
from string import ascii_lowercase, ascii_uppercase, digits


# Base62 Encoder and Decoder
def toBase62(num, b=62):
    if b <= 0 or b > 62:
        return 0
    base = digits + ascii_lowercase + ascii_uppercase
    r = num % b
    res = base[r]
    q = floor(num / b)
    while q:
        r = q % b
        q = floor(q / b)
        res = base[int(r)] + res
    return res


def toBase10(num, b=62):
    base = digits + ascii_lowercase + ascii_uppercase
    limit = len(num)
    res = 0
    for i in range(limit):
        res = b * res + base.find(num[i])
    return res
