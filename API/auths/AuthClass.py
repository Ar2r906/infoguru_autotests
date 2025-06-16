import pytest
from DATA_GENERATOR import fakers

class BaseUser:
    def __init__(self):
        self.email = fakers.generate_email()
        self.f_name = fakers.generate_f_name()
        self.s_name = fakers.generate_s_name()
        self.p_name = fakers.generate_p_name()
        self.age = fakers.generate_age()
        self.user_class = fakers.generate_user_class()
        self.school = fakers.generate_school()
        self.password = fakers.generate_password()

    def as_dict(self):
        return {
            'email': self.email,
            'f_name': self.f_name,
            's_name': self.s_name,
            'p_name': self.p_name,
            'age': self.age,
            'user_class': self.user_class,
            'school': self.school,
            'password': self.password,
        }

    def copy_modified(self, field, value):
        data = self.as_dict()
        data[field] = value
        return data

@pytest.fixture
def user_data_dict():
    return BaseUser().as_dict()