import pytest
from DATA_GENERATOR import fakers

class BaseNews:
    def __init__(self):
        self.title =fakers.generate_string(5, 9)
        self.content = fakers.generate_string(20, 40)
        self.image = 'src/images/image.png'
        self.file = 'src/files/file.txt'

    def as_dict(self):
        return {
            'title': self.title,
            'content': self.content,
            'image': self.image,
            'file': self.file,
        }

    def copy_modified(self, field, value):
        data = self.as_dict()
        data[field] = value
        return data

@pytest.fixture
def news_data_dict():
    return BaseNews().as_dict()