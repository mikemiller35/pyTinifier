import unittest
from math import floor
from string import ascii_lowercase, ascii_uppercase, digits


class TestEdoder(unittest.TestCase):

    def test_to_base_62(self):
        print("Start to_base_62 test\n")
        num = 101
        b = 62
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
        print("The encoded value should be " + res)
        self.assertEqual(res, '1D')

    def test_to_base_10(self):
        print("Start to_base_10 test\n")
        num = '1D'
        b = 62
        base = digits + ascii_lowercase + ascii_uppercase
        limit = len(num)
        res = 0
        for i in range(limit):
            res = b * res + base.find(num[i])
        print("The dencoded value should be " + str(res))
        self.assertEqual(res, 101)


if __name__ == '__main__':
    unittest.main()
