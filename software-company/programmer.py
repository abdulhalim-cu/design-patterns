from employee import Employee


class Programmer(Employee):
    def perform_duties(self):
        return self.write_codes()
    
    def write_codes(self):
        print("Programmer writes codes")
