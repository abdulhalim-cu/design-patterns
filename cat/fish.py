from food import Food


class Fish(Food):
    def get_nutrition(self):
        return 120
    
    def get_color(self):
        return 'Silver'
    
    def get_expiration(self):
        return '2025-03-14'
    
