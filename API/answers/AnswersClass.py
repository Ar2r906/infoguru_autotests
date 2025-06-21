from DATA_GENERATOR import fakers

class BaseAnswers:
    def __init__(self, test_id, question_id):
        self.test_id = test_id
        self.question_id = question_id
        self.first_answer = fakers.generate_string(8, 14)
        self.second_answer = fakers.generate_string(8, 14)
        self.third_answer = fakers.generate_string(8, 14)
        self.fourth_answer = fakers.generate_string(8, 14)
        self.true_answer = fakers.generate_string(8, 14)

    def as_dict(self):
        return {
            "test_id": self.test_id,
            "question_id": self.question_id,
            "first_answer": self.first_answer,
            "second_answer": self.second_answer,
            "third_answer": self.third_answer,
            "fourth_answer": self.fourth_answer,
            "true_answer": self.true_answer,
        }

    def copy_modified(self, field, value):
        data = self.as_dict()
        data[field] = value
        return data