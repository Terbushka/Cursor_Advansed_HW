import unittest
from unittest.mock import patch
from employee import Employee


class MockResponseTrue:
    status_code = 200
    elapsed = 100
    text = "response.ok = True"
    ok = True

    def __init__(self, *args, **kwargs):
        pass

class MockResponseFalse:
    status_code = 404
    elapsed = 100
    text = "response.ok = False"
    ok = False

    def __init__(self, *args, **kwargs):
        pass


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.classTest = Employee("Yuriy", "Bandura", 15000)

    def test_email(self):
        self.assertEqual(self.classTest.email, "yurabandura@email.com")

    def test_fullname(self):
        self.assertEqual(self.classTest.fullname, "Yuriy Bandura")

    def test_apply_raise(self):
        self.classTest.apply_raise()
        self.assertEqual(self.classTest.pay, 15750)

    @patch("employee.requests.get")
    def test_monthly_schedule(self, mocker):
        # mocker.return_value.status_code = 404
        mocker.side_effect = MockResponseTrue
        print(self.classTest.monthly_schedule('april'))
        self.assertEqual(self.classTest.monthly_schedule('april'), "response.ok = True")
        mocker.side_effect = MockResponseFalse
        print(self.classTest.monthly_schedule('april'))
        self.assertEqual(self.classTest.monthly_schedule('april'), "Bad Response!")