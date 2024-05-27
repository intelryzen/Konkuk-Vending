from my_parser.buyer_login_parser import BuyerLoginParser
from config import Config as c

class BuyerLogin:
    '''
        구매자 로그인 프롬프트
        command:
            0: 모드 선택 프롬프트로 이동
            그외:
                신규 사용자: 사용자 등록 후 로그인 성공 메시지 출력
                기존 사용자: "로그인 성공" 메시지 출력
    '''
    def __init__(self):
        self.parser = BuyerLoginParser()
    
    # 구매자 로그인 프롬프트
    def show_buyer_login_prompt(self):
        print("\n<구매자 로그인>")
        print("이전 화면으로 가려면 '0'을 입력해주세요.")
        print("-------------------------------------------")
        while True:
            login_input = input("ID를 입력해주세요\n>>>")
            is_valid, result = self.parser.parse(login_input, "")

            if is_valid:
                if result == 0:
                    return 0
                else:
                    for buyer in c.buyer_list:
                        if buyer.buyer_id == login_input:
                            c.logged_in_buyer = buyer
                            break
                    else:
                        # 신규 사용자인 경우
                        new_buyer = buyer(buyer_id=login_input)
                        c.buyer_list.append(new_buyer)
                        c.logged_in_buyer = new_buyer
                    print(result)
                    return 1
            else:
                print(result)

if __name__ == "__main__":
    # 로그인 프롬프트 테스트
    BuyerLogin().show_buyer_login_prompt()
