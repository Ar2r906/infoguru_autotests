import string
from faker import Faker
import random
import uuid

faker = Faker("ru_RU")

# генерация имени
def generate_f_name():
    return faker.first_name()

# генерация фамилии
def generate_s_name():
    return faker.last_name()

# генерация отчества
def generate_p_name():
    return faker.middle_name()

# генерация почты
def generate_email():
    return f'user_{uuid.uuid4().hex[:6]}@example.com'

# генерация возраста
def generate_age(min_age=10, max_age=18):
    return random.randint(min_age, max_age)

# генерация школы
def generate_school():
    number = random.randint(1, 300)
    return f'Школа {number}'

# генерация класса
def generate_user_class():
    grade = random.randint(5, 11)
    letter = random.choice(['А', 'Б', 'В', 'Г'])
    return f'{grade}{letter}'

# генерация пароля
def generate_password(min_length=8):
    return faker.password(length=min_length, special_chars=True, digits=True, upper_case=True, lower_case=True)

def generate_string(min_length, max_length):
    return ''.join(random.sample(string.ascii_letters + string.digits, random.randint(min_length, max_length)))

def generate_number():
    return random.randint(1, 100)