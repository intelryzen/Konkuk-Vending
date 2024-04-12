from file_utils.drinks_util import Drinks_util
from my_parser.drink_selection_parser import DrinkSelectionParser
from config import config as c
from prompt.mode import ShowDrinksList
from .change import Change
from .cash_input import CashInput

class DrinkSelection:
    '''
    음료수 선택 프롬프트
    command:
        0: 거스름돈 출력하고 음료수 선택 프롬프트, 잔액 0원이면 금액 입력 프롬프트로 이동
        정상: 잔액 업데이트, 음료수 목록 업데이트 후 출력, 음료수 재고 0이면 drinks.txt에서 삭제
        비정상: 음료수 선택 프롬프트로 이동
    '''
    
    def __init__(self):
        self.drink_list = ShowDrinksList() #음료수 목록 출력 
       

    # 음료수 선택 프롬프트
    def drink_selection_prompt(self):
        self.command = input("\n구매하실 음료수 번호를 입력해주세요.(0. 거스름 돈 반환 및 뒤로가기)\n>>>")
        parser = DrinkSelectionParser()
        drink_check, parsed_command = parser.parse(self.command)
        drink_price=0
        
        # 0: 거스름돈 출력하고 음료수 목록 출력 후 금액입력 프롬프트로 이동
        if  drink_check == True:
            if parsed_command ==0:
                canChange = Change(c.cash_by_cus) # 거스름 돈 출력
                c.cash_by_cus =0
                canChange, msg = Change(drink_price) # 거스름 돈 출력
                print(msg)
                return
            else :
                # 구매자가 선택한 음료의 가격을 drink_price 변수로 저장
                for i in range (0, len(c.drinks_list)):
                    if int(c.drinks_list[i].number) == int(parsed_command):
                        drink_price = c.drinks_list[i].price
                r_flag = self.remain_cash(c.cash_by_cus, drink_price,parsed_command)
                if r_flag==False:
                    return
                else:
                    canChange, null = Change(drink_price)
                    if not canChange:
                        print("오류 : 잔돈이 부족합니다.")
                    return self.drink_selection_prompt()
            '''
            if not canChange:
                c.cash_by_cus += drink_price
            '''
        else:
            print(parsed_command)       
            return self.drink_selection_prompt()

        # 정상: 잔액과 업데이트 된 음료수 목록 출력 후 음료수 선택 프롬프트로 이동
        

    def remain_cash(self, cash_by_cus, drink_price,number):
        print(cash_by_cus)
        print(drink_price)
        print(number)
        if cash_by_cus < drink_price: # (잔액 혹은 투입금액) < (음료수 가격)인 경우
            print("오류: 금액이 부족합니다. 다른 음료수를 선택해주세요")
            return True
        else:
            c.cash_by_cus = c.cash_by_cus - drink_price
            Drinks_util().buy_drink(str(number)) # 해당 위치에서 음료수 목록 파일 업데이트
            self.drink_list.show_drinks_list() # 음료수 목록 출력 
            print("잔돈 :" ,c.cash_by_cus)
            if c.cash_by_cus ==0:
                return False #잔돈이 0일 때
            
            return True


if __name__ == "__main__":
    # 음료수 선택 프롬프트 테스트
    drinkselection = DrinkSelection()

# 37번 권종개수 초과, 잔돈부족 오류 - drink_selection_parser에서 만든 후 추가 예정

