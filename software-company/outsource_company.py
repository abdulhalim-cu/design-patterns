from company import Company
from designer import Designer
from artist import Artist
from programmer import Programmer
from tester import Tester

class OutsourcingCompany(Company):
    def get_employees(self):
        return [Designer(), Programmer(), Tester(), Artist()]


class GameDevCompany(Company):
    def get_employees(self):
        return [Designer(), Artist()]
    

if __name__ == "__main__":
    game_dev_company = GameDevCompany()
    outsourcing_company = OutsourcingCompany()

    print("GameDevCompany is creating software:")
    game_dev_company.create_software()

    print("\nOutsourcingCompany is creating software:")
    outsourcing_company.create_software()
    