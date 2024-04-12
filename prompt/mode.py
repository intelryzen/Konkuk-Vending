from my_parser.mode_parser import ModeParser
from prompt.cash_input import CashInput
from prompt.login import Login


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

    # 모드 선택 프롬프트
    def mode_selection_prompt(self):
        while True:  # 잘못된 입력이면 모드 선택 프롬프트 반복
            print("\n<모드 선택>")
            print("0. 종료")
            print("1. 음료수 구매")
            print("2. 관리자 로그인")
            print("-------------------------------------------")
            
            command = input("모드를 선택해주세요.\n>>>")
            
            is_valid, mode = self.parser.parse(command)

            if is_valid:
                if mode == 0:
                    print("프로그램을 종료합니다.")
                    return False, mode
                elif mode == 1:
                    show_drink_list = ShowDrinksList()
                    show_drink_list.show_drinks_list()  # 음료수 목록을 출력
                    
                    CashInput()  # 금액 입력 프롬프트로 이동
                    return True, mode
                elif mode == 2:
                    
                    Login()  # 로그인 프롬프트로 이동
                    return True, mode
            else:
                print(mode)  # 오류 메시지 출력
                continue
            '''
            # Mode()수정
            is_valid, mode = self.parser.parse(command)
            
            if is_valid:
                return mode
            else:
                print(mode)
                continue
                
            # main() 추가
            mode = Mode()
            mode = mode.mode_selection_prompt()
            if mode == 0:
                print("프로그램을 종료합니다.")
                return
            elif mode == 1:
                show_drink_list = ShowDrinksList()
                show_drink_list.show_drinks_list()
                CashInput()
            elif mode == 2:
                Login()
            '''
            
from file_utils.drinks_util import Drinks_util
class ShowDrinksList:
    def __init__(self):
        self.du = Drinks_util()

    def show_drinks_list(self):
        print("\n<음료수 목록>")
        self.du.print_drinks_for_customer()
        print("(0. 뒤로가기)")
        print("-------------------------------------------")

if __name__ == "__main__":
    # 모드 선택 프롬프트 테스트
    mode = Mode()
    mode.mode_selection_prompt()
