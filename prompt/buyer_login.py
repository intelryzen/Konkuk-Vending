from my_parser.buyer_login_parser import BuyerLoginParser
from config import Config as c

class BuyerLogin:
    def __init__(self):
        self.parser = BuyerLoginParser()

    def show_buyer_login_prompt(self):
        print("\n<사용자 로그인>")
        print("이전 화면으로 가려면 '0'을 입력해주세요.")
        print("-------------------------------------------")
        while True:
            login_input = input("로그인\n>>>")

            for buyer in c.buyer_list:
                is_valid, result = self.parser.parse(login_input, buyer.buyer_id)

            if is_valid:
                    if result == '0':
                        return 0
                    else:
                        for buyer in c.buyer_list:
                            if buyer.buyer_id == login_input:
                                c.logged_in_buyer = buyer
                                break
                        else:
                            c.logged_in_buyer = next(buyer for buyer in c.buyer_list if buyer.buyer_id == login_input)
                    print(result)
                    return 1
            else:
                print(result)


if __name__ == "__main__":
    pass