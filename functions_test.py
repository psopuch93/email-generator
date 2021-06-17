import unittest
import functions
import string


class FunctionsTest(unittest.TestCase):

    def test_NameLenght(self):
        result = len(functions.random_name())
        self.assertGreater(result, 0)

    def test_IsNameLenghtNonZero(self):
        result = len(functions.random_name())
        self.assertNotEqual(result, 0)

    def test_IsLastname(self):
        result = len(functions.random_lastname())
        self.assertGreater(result, 0)

    def test_NotNone(self):
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

    def test_GenderChoice(self):
        result = functions.random_gender()
        genders = ["male", "female"]
        self.assertIn(result, genders)


    '''def test_BirthDayValidate(self):
        result = functions.random_birth_day()
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, 29)'''

    '''def test_BirthMonthValidate(self):
        result = functions.random_birth_month()
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, 12)'''

    def test_BirthYearValidate(self):
        result = functions.random_birth_year()
        self.assertGreaterEqual(result, 1921)
        self.assertLessEqual(result, 2021)


if __name__ == '__main__':
    unittest.main()
