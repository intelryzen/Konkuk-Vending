class Drink_info:
    def __init__(self, drink_number, name, price):
        self.drink_number = drink_number
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.drink_number}. {self.name} {self.price} {self.stock}"