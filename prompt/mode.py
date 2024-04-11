class Mode:
    '''
    모드 선택 프롬프트
    command:
        #ModeParser 클래스 연동
        0: 프로그램 종료
        1: 금액 입력 프롬프트로 이동
        2: 관리자 프롬프트로 이동
        비정상: 모드 선택 프롬프트로 이동
    '''
    def __init__(self):
        self.mode_selection_prompt()

    # 모드 선택 프롬프트
    def mode_selection_prompt(self):
        while True:  # 잘못된 입력이면 반복적으로 모드선택프롬프트
            print("\n<모드 선택>")
            print("0. 종료")
            print("1. 음료수 구매")
            print("2. 관리자 로그인")
            print("-------------------------------------------")
            
            command = input("모드를 선택해주세요.\n>>>")
            
            is_valid, result = self.parse(command)

            if is_valid:
                if result == 0:
                    print("프로그램을 종료합니다.")
                    return True, result
                elif result == 1:
                    show_drink_list = ShowDrinksList()
                    show_drink_list.show_drinks_list()  # 음료수 목록을 출력
                    CashInput() # 금액 입력 프롬프트로 이동
                    return True, result
                elif result == 2:
                    Login() # 로그인 프롬프트로 이동
                    return True, result
            else:
                print(result)  # 오류 메시지 출력
                continue


class ShowDrinksList:

    def show_drinks_list(self):
        print("\n<음료수 목록>")
        sorted_drink_list = sorted(drinklist, key=lambda x: x.number)
        for Drink in sorted_drink_list:
            print(f"{Drink.number}. {Drink.name} {Drink.quantity}개 {Drink.value}원")
        print("(0. 뒤로가기)")
        print("-------------------------------------------")

# 모드 선택 프롬프트 테스트
Mode()
