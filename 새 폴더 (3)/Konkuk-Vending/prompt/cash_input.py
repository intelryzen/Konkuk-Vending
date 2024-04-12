from my_parser.cash_input_parser import CashInputParser
from config import config as c

class CashInput:
    '''
    금액 입력 프롬프트
    command:
        0: 모드 선택 프롬프트로 이동
        정상: 음료수 선택 프롬프트로 이동
        비정상: 오류 메시지 + 금액 입력 프롬프트로 이동
    '''
        
    def __init__(self):
        self.cash_input_prompt()

    def cash_input_prompt(self):

        new_input = input("금액을 투입해주세요.\n>>>")   
        c.cash_by_cus = c.cash_by_cus + new_input

        parser = CashInputParser()
        parsed_command = parser.parse(c.cash_by_cus)
        
        if parsed_command == (True, 0):
            from .mode import Mode
            modeselect = Mode()
            modeselect.mode_selection_prompt()  
            

        elif parsed_command[0] and isinstance(parsed_command[1], dict):
            from .drink_selection import DrinkSelection
            DrinkSelection()

        else:
            # 비정상: 금액 입력 프롬프트로 이동
            print("오류: 올바른 입력이 아닙니다.")
            self.cash_input_prompt()
