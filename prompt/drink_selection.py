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

    # 음료수 선택 프롬프트
    def drink_selection_prompt(self):
        command = input("\n구매하실 음료수 번호를 입력해주세요.(0. 거스름 돈 반환 및 뒤로가기)\n>>>")
        # 0: 거스름돈 출력하고 음료수 목록 출력 후 음료수 선택 프롬프트로 이동 
        #    잔액 0 아니면 음료수 선택 프롬프트로 이동, 잔액 0원이면 금액 입력 프롬프트로 이동
        # 정상: 잔액 업데이트, 음료수 목록 업데이트 후 출력, 
        #       음료수 재고 0이면 drinks.txt에서 삭제. 음료수 선택 프롬프트로 이동
        # 비정상: 음료수 선택 프롬프트로 이동

    # 잔액 업데이트
    
    # 음료수 목록 업데이트

# 음료수 선택 프롬프트 테스트
drinkselection = DrinkSelection()
