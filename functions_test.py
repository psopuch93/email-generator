import unittest
import functions
import string


class FunctionsTest(unittest.TestCase):

    def test_IsName(self):
        result = len(functions.random_name())
        self.assertGreater(result, 0)

    def test_IsNameLenghtNonZero(self):
        result = len(functions.random_name())
        self.assertNotEqual(result, 0)

    def test_IsLastname(self):
        result = len(functions.random_lastname())
        self.assertGreater(result, 0)

    def test_NoNone(self):
        result = functions.random_name()
        self.assertIsNotNone(result)

    def test_PasswordLenght(self):
        result = len(functions.random_password())
        self.assertGreater(result, 8)

    def test_PasswordSpecialChars(self):
        result = functions.random_password()
        for i in result:
            if i == string.punctuation:
                pass
        self.assertIn(i, result)

    def test_LoginLenght(self):
        result = len(functions.random_login())
        self.assertEqual(result, 10)

    def test_LoginListLenght(self):
        login = functions.random_login()
        variable_result = len(functions.random_login())
        list_result = len(functions.login_list(login))
        self.assertEqual(variable_result, list_result)


if __name__ == '__main__':
    unittest.main()
