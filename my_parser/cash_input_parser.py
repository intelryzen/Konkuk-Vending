from .base_parser import BaseParser

'''
금액 입력
    올바른 입력이 아닙니다.
'''

# 허용 명령어
allows = [0]

class CashInputParser(BaseParser):
    
    # 반환 형식: (정상 여부[bool], 정상일 경우 뒤로가기(0) 또는 money[dict]나 비정상일 경우 오류메시지[str])
    def parse(self, input: str) -> tuple[bool, any]:
        error_message = "오류: 올바른 입력이 아닙니다."
        money = {}
        command = self.parse_command(input)

        # 뒤로가기(0) 인지 먼저 확인
        if command in allows:
            return True, command
       
        input = self.parse_all(input)
                
        # 인자가 홀수 개이면 오류, 인자가 \n을 포함하고 있으면 오류, 주어진 인자가 규칙을 따르지 않으면 오류 
        try:
            for i in range(0, len(input), 2):
                # 권종과 개수
                money_type = input[i]
                count = input[i+1]

                if(not self.is_money_type(money_type)):
                    raise Exception("권종 아님") 
                
                if(not self.is_count(count)):
                    raise Exception("개수 아님") 

                money_type = int(input[i])
                count = int(input[i+1])

                # 중복된 키(권종)가 이미 있으면 개수를 더함.
                if(money_type in money):
                    money[money_type] += count
                    if(money[money_type] > 99):
                        raise Exception("동일 권종 99개 초과") 
                else:
                    money[money_type] = count
        except:
             return False, error_message
        
        return True, money

# 테스트
if __name__ == "__main__":
    parser = CashInputParser()
    test_input = "   \t\f\v500 01 100 10 100 1 50000 30 100 88"
    # test_input = "   \t\f\v0\n\n"
    t = parser.parse(test_input)
    print(t)