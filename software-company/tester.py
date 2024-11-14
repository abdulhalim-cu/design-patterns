from employee import Employee


class Tester(Employee):
    def perform_duties(self):
        self.test_codes()

    def test_codes(self):
        print("Tester tests codes")
