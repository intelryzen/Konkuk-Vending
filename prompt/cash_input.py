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

    # 금액 입력 프롬프트
    def cash_input_prompt(self):
        command = input("금액을 투입해주세요.\n>>>")

    # 입력 0: 모드 선택 프롬프트로 복귀
    # 정상: 음료수 선택 프롬프트로 이동
    # 비정상: 금액 입력 프롬프트로 이동

# 금액 입력 프롬프트 테스트
cashinput = CashInput()
