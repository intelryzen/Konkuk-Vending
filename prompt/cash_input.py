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
        
    def cash_input_prompt(self):
       
        new_input = input("금액을 투입해주세요.\n>>>")
        
      #  c.cash_by_cus = c.cash_by_cus + new_input

        parser = CashInputParser()
        parsed_command, parser_money = parser.parse(new_input)
        total_money = 0
        if parsed_command:     
            if not parser_money==0:
                for key in parser_money:
                    total_money += key * parser_money[key]
                c.cash_by_cus = total_money
                return True
            else:
                return False
        else:
            # 비정상: 금액 입력 프롬프트로 이동
            print("오류: 올바른 입력이 아닙니다.")
            return self.cash_input_prompt()
