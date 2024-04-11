from file_utils.drinks_util import Drinks_util
from parser.drink_selection_parser import DrinkSelectionParser
from config import config as c
from prompt.mode import ShowDrinksList


class DrinkSelection:
    '''
    음료수 선택 프롬프트
    command:
        0: 거스름돈 출력하고 음료수 선택 프롬프트, 잔액 0원이면 금액 입력 프롬프트로 이동
        정상: 잔액 업데이트, 음료수 목록 업데이트 후 출력, 음료수 재고 0이면 drinks.txt에서 삭제
        비정상: 음료수 선택 프롬프트로 이동
    '''
    
    def __init__(self):
        self.drink_selection_prompt()
        self.drink_list = ShowDrinksList() #음료수 목록 출력 
        self.command = input("\n구매하실 음료수 번호를 입력해주세요.(0. 거스름 돈 반환 및 뒤로가기)\n>>>")

    # 음료수 선택 프롬프트
    def drink_selection_prompt(self):

        parser = DrinkSelectionParser()
        parsed_command = parser.parse(self.command)


        # 0: 거스름돈 출력하고 음료수 목록 출력 후 금액입력 프롬프트로 이동
        if parsed_command[0] and parsed_command[1] == 0:
            Change(c.cash_by_cus) # 거스름 돈 출력 
            return CashInput() # 금액입력 프롬프트로 이동

        # 정상: 잔액과 업데이트 된 음료수 목록 출력 후 음료수 선택 프롬프트로 이동
        elif parsed_command[0] and isinstance(parsed_command(self.command)[1],int):

            # 구매자가 선택한 음료의 가격을 drink_price 변수로 저장
            for i in range (0, len(c.drink_list), 4):
                if c.drinks_list[i] == self.command:
                    drink_price = c.drink_list[i+2]

            self.remain_cash(c.cash_by_cus, drink_price)

    def remain_cash(self, cash_by_cus, drink_price):
        if cash_by_cus <= drink_price: # (잔액 혹은 투입금액) < (음료수 가격)인 경우
            print("오류: 금액이 부족합니다. 다른 음료수를 선택해주세요")
            return CashInput() # 잔액 0원이면 금액 입력 프롬프트로 이동 
            print("잔액:",c.cash_by_cus,"원") # 해당 위치에서 잔액 출력

        else:
            c.cash_by_cus = c.cash_by_cus - drink_price
            Drinks_util.buy_drink(self.command) # 해당 위치에서 음료수 목록 파일 업데이트
            print("잔액:",c.cash_by_cus,"원") # 해당 위치에서 잔액 출력
            self.drink_list.show_drinks_list() # 음료수 목록 출력 
            return self.drink_selection_prompt() #음료수 선택 프롬프트로 이동


if __name__ == "__main__":
    # 음료수 선택 프롬프트 테스트
    drinkselection = DrinkSelection()

# 37번 권종개수 초과, 잔돈부족 오류 - drink_selection_parser에서 만든 후 추가 예정

