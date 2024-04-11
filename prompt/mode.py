from ..parser.mode_parser import ModeParser

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
        self.parser = ModeParser()
        self.mode_selection_prompt()

    # 모드 선택 프롬프트
    def mode_selection_prompt(self):
        print("\n<모드 선택>")
        print("0. 종료")
        print("1. 음료수 구매")
        print("2. 관리자 로그인")
        print("-------------------------------------------")
        
        command = input("모드를 선택해주세요.\n>>>")
        
        is_valid, result = self.parser.parse(command)

        if is_valid:
            if result == 0:
                print("프로그램을 종료합니다.")
                return True, result
            elif result == 1:
                show_drink_list = ShowDrinksList() # 음료수 목록을 출력하고 금액입력 프롬프트로 이동
                CashInput()
                return True, result
            elif result == 2:
                Login() # 로그인 프롬프트로 이동
                return True, result
        else:
            print(result)  # 오류 메시지 출력
            Mode() # 모드 프롬프트로 이동
            return False, result


class ShowDrinksList:

    def __init__(self):
        self.show_drinks_list()

    def show_drinks_list(self):
        print("\n<음료수 목록>")
        sorted_drink_list = sorted(drink_list, key=lambda x: x.number)
        for Drink in sorted_drink_list:
            print(f"{Drink.number}. {Drink.name} {Drink.quantity}개 {Drink.value}원")
        print("(0. 뒤로가기)")
        print("-------------------------------------------")
        cashinput = CashInput()# 금액 입력 프롬프트로 이동

# 모드 선택 프롬프트 테스트
modeselection = Mode()
