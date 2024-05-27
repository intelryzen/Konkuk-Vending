from config import config as c
from file_utils.buyer_util import BuyerUtils
from my_parser.coupon_parser import CouponParser

class Coupon:
    def coupon_prompt(num_coupon):
        if num_coupon > 0:
            use = False
            while not use:
                print("<보유 쿠폰>")
                print("1000원 할인 쿠폰:" + str(num_coupon) + "개")
                command = input("쿠폰을 사용하시겠습니까? (1: 사용 2: 미사용)\n>>>")
                parser = CouponParser()
                use, parsed_command = parser.parse(command)
                if not use:
                    print(parsed_command)
                    print()
            return parsed_command
        else:
            return 3