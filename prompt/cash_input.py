from parser.cash_input_parser import CashInputParser

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
        print("금액을 입력해주세요")
        command = input(">>>")
        
        parser = CashInputParser()
        parsed_command = parser.parse(command)
        
        if parsed_command == (True, 0):
            from .mode import Mode
            Mode()  
            

        elif parsed_command[0] and isinstance(parsed_command[1], dict):
            from .drink_selection import DrinkSelection
            DrinkSelection()

        else:
            # 비정상: 금액 입력 프롬프트로 이동
            print("오류: 올바른 입력이 아닙니다.")
            self.cash_input_prompt()
            

if __name__ == "__main__":
    # 임의의 값을 전달하는 대신, cash_input_prompt 메서드 내에서 입력을 받도록 설정합니다.
    cashinput = CashInput()
