import random
import string


def random_name():
    name = ''
    i = 0
    while i < 6:
        name += random.choice(string.ascii_letters)
        i += 1
    return name


def random_lastname():
    lastname = ''
    i = 0
    while i < 6:
        lastname += random.choice(string.ascii_letters)
        i += 1
    return lastname


def random_gender():
    genders = ["male", "female", "other"]
    gender = random.choice(genders)
    return gender


def random_password():
    password = ''
    i = 0
    while i < 8:
        password += random.choice(string.ascii_letters)
        i += 1
    password += random.choice(string.punctuation)
    return password


def random_login():
    login = ''
    i = 0
    while i < 10:
        login += random.choice(string.ascii_letters)
        i += 1
    return login


def login_list(login):
    login_list = []
    for i in login:
        login_list.append(i)
    return login_list


def password_list(password):
    password_list = []
    for i in password:
        password_list.append(i)
    return password_list


def login_password_validator(login_list, password_list):
    counter = 0
    for i in login_list:
        for n in password_list:
            if i == n:
                counter += 1
    if counter > 2:
        return False
    else:
        return True
