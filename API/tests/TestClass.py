import pytest
from DATA_GENERATOR import fakers
from API.auths.conftest import get_admin_uid

class BaseTests:
    def __init__(self, uid):
        self.theme = fakers.generate_string(5, 10)
        self.uid = uid

    def as_dict(self):
        return {
            'theme': self.theme,
            'uid': self.uid,
        }

    def copy_modified(self, field, value):
        data = self.as_dict()
        data[field] = value
        return data

@pytest.fixture
def tests_data_dict(get_admin_uid):
    return BaseTests(get_admin_uid).as_dict()