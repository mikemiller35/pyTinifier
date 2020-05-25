import unittest
import re

class TestValidator(unittest.TestCase):
    """Tests"""

    def test_is_valid_input0(self):
        url = "https://google.com"
        print("The URL being tested is " + url)
        regex = re.compile(
            r"^(?:http|ftp|s3)s?://"  # http:// or https://
            r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"
            r"localhost|"  # localhost...
            r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"  # ...or ip
            r"(?::\d+)?"  # optional port
            r"(?:/?|[/?]\S+)$", re.IGNORECASE
        )
        result = re.match(regex, url)
        self.assertIsNotNone(result)


    def test_is_valid_input1(self):
        url = "http://127.0.0.1:8080"
        print("The URL being tested is " + url)
        regex = re.compile(
            r"^(?:http|ftp|s3)s?://"  # http:// or https://
            r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"
            r"localhost|"  # localhost...
            r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"  # ...or ip
            r"(?::\d+)?"  # optional port
            r"(?:/?|[/?]\S+)$", re.IGNORECASE
        )
        result = re.match(regex, url)
        self.assertIsNotNone(result)


    def test_is_valid_input2(self):
        url = "s3://s3.foo.bar"
        print("The URL being tested is " + url)
        regex = re.compile(
            r"^(?:http|ftp|s3)s?://"  # http:// or https://
            r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"
            r"localhost|"  # localhost...
            r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"  # ...or ip
            r"(?::\d+)?"  # optional port
            r"(?:/?|[/?]\S+)$", re.IGNORECASE
        )
        result = re.match(regex, url)
        self.assertIsNotNone(result)


    def test_is_valid_input_bad0(self):
        url = "google.com"
        print("The URL being tested is " + url)
        regex = re.compile(
            r"^(?:http|ftp|s3)s?://"  # http:// or https://
            r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"
            r"localhost|"  # localhost...
            r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"  # ...or ip
            r"(?::\d+)?"  # optional port
            r"(?:/?|[/?]\S+)$", re.IGNORECASE
        )
        result = re.match(regex, url)
        self.assertIsNone(result)


    def test_is_valid_input_bad1(self):
        url = "http://google"
        print("The URL being tested is " + url)
        regex = re.compile(
            r"^(?:http|ftp|s3)s?://"  # http:// or https://
            r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"
            r"localhost|"  # localhost...
            r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"  # ...or ip
            r"(?::\d+)?"  # optional port
            r"(?:/?|[/?]\S+)$", re.IGNORECASE
        )
        result = re.match(regex, url)
        self.assertIsNone(result)


    def test_is_valid_input_bad2(self):
        url = "http://\"; SELECT TRUE;\""
        print("The URL being tested is " + url)
        regex = re.compile(
            r"^(?:http|ftp|s3)s?://"  # http:// or https://
            r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"
            r"localhost|"  # localhost...
            r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"  # ...or ip
            r"(?::\d+)?"  # optional port
            r"(?:/?|[/?]\S+)$", re.IGNORECASE
        )
        result = re.match(regex, url)
        self.assertIsNone(result)
        