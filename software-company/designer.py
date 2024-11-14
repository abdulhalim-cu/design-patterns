from employee import Employee


class Designer(Employee):
    def perform_duties(self):
        self.design_architecture()
    
    def design_architecture(self):
        print("Designer design the architecture")
