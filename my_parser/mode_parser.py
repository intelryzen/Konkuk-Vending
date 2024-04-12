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
        print("\n<모드 선택>")
        print("0. 종료")
        print("1. 음료수 구매")
        print("2. 관리자 로그인")
        print("-------------------------------------------")
            
        command = input("모드를 선택해주세요.\n>>>")
            
        is_valid, mode = self.parser.parse(command)
        # if is_vaild == True:
        if is_valid:
            if mode == 0:
                return True, mode
            elif mode == 1:
                return True, mode
            elif mode == 2:
                return True, mode
        # if is_vaild == False:
        else:   
            print(mode)  # 오류 메시지 출력
            return False, mode
            
from file_utils.drinks_util import Drinks_util
class ShowDrinksList:
    def __init__(self):
        self.du = Drinks_util()

    def show_drinks_list(self):
        print("\n<음료수 목록>")
        self.du.print_drinks()
        print("(0. 뒤로가기)")
        print("-------------------------------------------")

if __name__ == "__main__":
    # 모드 선택 프롬프트 테스트
    mode = Mode()
    mode.mode_selection_prompt()
