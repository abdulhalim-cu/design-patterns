from food import Food


class Sausage(Food):
    def get_nutrition(self):
        return 100
    
    def get_color(self):
        return 'Brown'
    
    def get_expiration(self):
        return '2024-12-31'
    
