import unittest, functions, string


class FunctionsTest(unittest.TestCase):

    def test_IsName(self):
        result = len(functions.random_name())
        self.assertGreater(result, 0)

    def test_IsLenghtNonZero(self):
        result = len(functions.random_name())
        self.assertNotEqual(result, 0)

    def test_IsGender(self):
        result = functions.random_name()
        self.assertIn('Gender', result)

    def test_NoNone(self):
        result = functions.random_name()
        self.assertIsNotNone(result)

    def test_HasWhitespace(self):
        result = functions.random_name()
        self.assertIn(' ', result)

    def test_PasswordLenght(self):
        result = len(functions.random_password())
        self.assertGreater(result, 6)

    def test_PasswordSpecialChars(self):
        result = functions.random_password()
        for i in result:
            if i == string.punctuation:
                pass
        self.assertIn(i, result)


if __name__ == '__main__':
        unittest.main()
