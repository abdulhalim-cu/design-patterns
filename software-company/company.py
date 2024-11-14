from designer import Designer
from programmer import Programmer
from tester import Tester


class Company:
    def __init__(self, employees) -> None:
        self.employees = employees

    def do_work(self):
        for employee in self.employees:
            employee.perform_duties()


if __name__ == '__main__':
    employees = [Designer(), Programmer(), Tester()]
    company = Company(employees)
    company.do_work()
