class Drink:
    def __init__(self, number, name, price, stock):
        self.number = number
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.number} {self.name} {self.price}원 {self.stock}개"