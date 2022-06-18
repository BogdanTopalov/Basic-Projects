class TestPaper:
    def __init__(self, subject, mark_scheme, pass_mark):
        self.subject = subject
        self.mark_scheme = mark_scheme
        self.pass_mark = pass_mark


class Student:
    def __init__(self):
        self.tests_taken = 'No tests taken'

    def take_test(self, test, answers):
        minimum_pass = int(test.pass_mark[:2])
        wrong_answers = list(set(test.mark_scheme) - set(answers))
        result = len(answers) - len(wrong_answers)
        percentage = (result / len(test.mark_scheme)) * 100
        pass_or_fail = 'Passed!' if percentage >= minimum_pass else 'Failed!'

        if self.tests_taken == 'No tests taken':
            self.tests_taken = {}

        self.tests_taken[test.subject] = f"{pass_or_fail} ({round(percentage)}%)"