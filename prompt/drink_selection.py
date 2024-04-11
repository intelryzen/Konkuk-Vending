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
        parser = DrinkSelectionParser()
        parsed_command = parser.parse(command)
    # 음료수 선택 프롬프트
    def drink_selection_prompt(self):

        if parser.parse(command)[0] and parser.parse(command)[1] == 0:
        # 0: 거스름돈 출력하고 음료수 목록 출력 후 금액입력 프롬프트로 이동
            Change(CashInputParser.parse(command)[1]) # 거스름 돈 출력 <<검토필요: CashInputParser.parse(command)[1]값을 cash_input에서 가져와야함
            return CashInput()

        elif parser.parse(command)[0] and isinstance(parser.parse(command)[1],int):
        # 잔액 0 아니면 음료수 선택, 잔액 0원이면 금액 입력 프롬프트로 이동
        #       >>>음료수 재고 0이면 drinks.txt에서 삭제
        # . 음료수 선택 프롬프트로 이동        
            if change_remain == 0: #change_remain;잔액 값을 어디서 가져와야하는지 모르겠음

                return drink_selection_prompt()
            else: # 정상: 잔액과 업데이트 된 음료수 목록 출력 후 음료수 선택 프롬프트로 이동
                return drink_selection_prompt()

        DrinkSelection()

        else:
        # 비정상: 음료수 선택 프롬프트로 이동
        self.drink_selection_prompt()

    # 잔액 업데이트
    
    # 음료수 목록 업데이트

# 음료수 선택 프롬프트 테스트
drinkselection = DrinkSelection()

