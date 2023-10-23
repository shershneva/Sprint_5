import random
import secrets
import string

def random_name():
    letters = string.ascii_letters
    name = ''.join(random.choice(letters) for i in range(10))
    return name

def random_login():
    username = ''.join(random.choice(string.ascii_lowercase) for i in range(8))
    host = random.choice(['yahoo.com', 'gmail.com', 'yandex.ru', 'mail.ru'])
    return f"{username}@{host}"

def random_password():
    s = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(s) for i in range(12))
    return password


