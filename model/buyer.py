class Buyer:
    def __init__(self, buyer_id:str, money:int, coupon_number:int):
        self.buyer_id = buyer_id
        self.money = money
        self.coupon_number = coupon_number

    def __str__(self):
        return f"{self.buyer_id} {self.money}, {self.coupon_number}"
