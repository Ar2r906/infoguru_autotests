from DATA_GENERATOR import fakers

class BaseQuestion:
    def __init__(self, test_id):
        self.test_id = test_id
        self.content = fakers.generate_string(8, 14)

    def as_dict(self):
        return {
            'test_id': self.test_id,
            'content': self.content,
        }

    def copy_modified(self, field, value):
        data = self.as_dict()
        data[field] = value
        return data