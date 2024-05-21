class Drink_info:
    def __init__(self, drink_number:int, name:str, price:int, stock:int):
        self.drink_number = drink_number
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.drink_number}. {self.name} {self.price} {self.stock}"