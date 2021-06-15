import random, string


def random_name():
    name = ''
    i = 0
    while i<6:
        name += random.choice(string.ascii_letters)
        i+=1
    lastname = ''
    i = 0
    while i<6:
        lastname += random.choice(string.ascii_letters)
        i+=1
    genders = ["male", "female", "other"]
    gender = random.choice(genders)
    fullname = name + ' ' + lastname + ' Gender: ' + gender
    return fullname


def random_password():
    password = ''
    i = 0
    while i<6:
        password += random.choice(string.ascii_letters)
        i+=1
    password += random.choice(string.punctuation)
    return password