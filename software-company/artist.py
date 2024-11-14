from employee import Employee


class Artist(Employee):
    def perform_duties(self):
        return self.create_graphics()
    
    def create_graphics(self):
        print("Artist is creating graphics.")
