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

        parser = CashInputParser()
        parsed_command = parser.parse(command)

        if parsed_command == (True, 0):
            # 입력 0: 모드 선택 프롬프트로 복귀    
            Mode()

        elif parsed_command[0] and isinstance(parsed_command[1], dict):
            # 정상: 음료수 선택 프롬프트로 이동
            DrinkSelection()

        else:
            # 비정상: 금액 입력 프롬프트로 이동
            print("오류: 올바른 입력이 아닙니다.")
            self.cash_input_prompt()
            

if __name__ == "__main__":
    # 금액 입력 프롬프트 테스트
    cashinput = CashInput()
