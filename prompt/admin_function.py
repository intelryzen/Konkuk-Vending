from parser.admin_function_parser import AdminFunctionParser
from file_utils.cash_util import Cash_Utils
from file_utils.drinks_util import Drinks_util
from config import config as c
from model.drink import Drink



class Admin:
    '''
        관리자 프롬프트
        command:
            0: 모드 선택 프롬프트로 이동
            1: 자판기 내의 음료수 재고 상황을 출력
            2: 자판기 내의 현금 상황을 출력
            3: 자판기 내의 현금 상황을 수정
            4: 자판기 내 특정 번호의 음료수 재고를 수정
            5: 자판기의 특정 번호에 음료수를 추가
            비정상: 오류 메시지 + 관리자 프롬프트로 이동
    '''    
    def __init__(self):
        self.parser = AdminFunctionParser()
        self.admin_prompt()

    # 관리자 프롬프트
    def admin_prompt(self):
        while True:
            print("\n<관리자>")
            print("1. 잔돈 확인")
            print("2. 음료수 재고 확인")
            print("3. 잔돈 수정")
            print("4. 음료수 재고 수정")
            print("5. 음료수 추가")
            print("(0.로그아웃)")
            print("-------------------------------------------")
            admin_input = input(">>>")

            is_valid, command = self.parser.parser(admin_input)
            
            if is_valid:
                admin_input = admin_input.strip()
                parts = admin_input.split()
                if command == 1:
                    # 잔돈 목록 출력, 비싼 권종에서 싼 권종 순으로
                    sorted_currency_list = sorted(c.currency_list, key=lambda x: x.value, reverse=True)
                    for Currency in sorted_currency_list:
                        print(f"{Currency.value}원 {Currency.quantity}개")            
                elif command == 2:
                    # 음료수 재고 확인 기능 구현 1번 부터 정렬
                    Drinks_util().print_drinks_for_admin()
                elif command == 3:
                    # 잔돈 수정 기능 구현 
                    cash_utils_instance = Cash_Utils()  # Cash_Utils 클래스의 인스턴스 생성
                    cash_utils_instance.change_currency(parts[1], parts[2])
                elif command == 4:
                    drinks_utils_instance = Drinks_util()
                    drinks_utils_instance.modify_stock(parts[1], parts[2])
                elif command == 5:
                    drinks_utils_instance = Drinks_util()
                    drinks_utils_instance.add_new_drink(parts[1], parts[2], parts[3], parts[4])
                elif command == 0:
                    from prompt.mode import Mode
                    Mode() # 입력 0이면 모드 선택 프롬프트로 이동
            else:
                print(command)  # 오류 메시지 출력
                continue
            
            
if __name__ == "__main__":
    # 관리자 프롬프트 테스트
    Admin()
