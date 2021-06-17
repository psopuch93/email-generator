import functions

name = functions.random_name()
lastname = functions.random_lastname()
date_of_birth = f"{functions.random_birth_day()}/" \
                f"{functions.random_birth_month()}/" \
                f"{functions.random_birth_year()}"
login = functions.random_login()
password = functions.random_password()
gender = functions.random_gender()
login_list = functions.login_list(login)
password_list = functions.password_list(password)
validator = functions.login_password_validator(login_list,password_list)

print(f"Name: {name}\n"
      f"Lastname: {lastname}\n"
      f"Date of birth: {date_of_birth}\n"
      f"Login: {login}\n"
      f"Login list: {login_list}\n"
      f"Password: {password}\n"
      f"Password list: {password_list}\n"
      f"Gender: {gender}\n"
      f"Validator: {validator}\n")