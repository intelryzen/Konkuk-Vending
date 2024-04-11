


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
        Drinks_util.print_drinks_for_customer() #음료수 목록 출력 - 해당 함수 내'<음료수 목록>' 문구 필요
        command = input("\n구매하실 음료수 번호를 입력해주세요.(0. 거스름 돈 반환 및 뒤로가기)\n>>>")

    # 음료수 선택 프롬프트
    def drink_selection_prompt(self):

        parser = DrinkSelectionParser()
        parsed_command = parser.parse(command)

        # 0: 거스름돈 출력하고 음료수 목록 출력 후 금액입력 프롬프트로 이동
        if parsed_command[0] and parsed_command[1] == 0:
            canChange, msg = Change(CashInputParser.parse(command)[1]) # 거스름 돈 출력 <<검토필요: CashInputParser.parse(command)[1]값을 cash_input에서 가져와야함
            print(msg)
            if canChange:
                #투입금: 투입금 - 음료수 가격
            else:
                #투입금 변동 X
            ShowDrinksList() # 음료수 목록 출력
            return CashInput() # 금액입력 프롬프트로 이동

        # 정상: 잔액과 업데이트 된 음료수 목록 출력 후 음료수 선택 프롬프트로 이동
        elif parsed_command[0] and isinstance(parsed_command(command)[1],int):
######                     # 해당 위치에서 잔액 출력 << 잔액 어디서 가져올지 찾기 
            if remain_cash <= drink_price: # (잔액 혹은 투입금액) < (음료수 가격)인 경우
                print("오류: 금액이 부족합니다. 다른 음료수를 선택해주세요")# 이거 DrinkSelectionParser에서 만들어 주면 반영하기 
                return CashInput() # 잔액 0원이면 금액 입력 프롬프트로 이동 

            else: 
######                    # 해당 위치에서 음료수 목록 업데이트
######                    # 잔액 업데이트 << 32번 줄이랑 같이 해결, 잔액 데이터의 위치 필요
                ShowDrinksList() # 업데이트 된 음료수 목록 출력
                return self.drink_selection_prompt() #음료수 선택 프롬프트로 이동

        else:
        # 그 외 예외처리(권종개수 추가 오류)추가 예정 : 음료수 선택 프롬프트로 이동
            return self.drink_selection_prompt()


    

if __name__ == "__main__":
    # 음료수 선택 프롬프트 테스트
    drinkselection = DrinkSelection()


        # 잔액 0 아니면 음료수 선택, 잔액 0원이면 금액 입력 프롬프트로 이동 -> 투입금액 부족 오류 상황으로 분류하여 처리함
        #       >>>음료수 재고 0이면 drinks.txt에서 삭제 후 음료수 선택 프롬프트로 이동 
