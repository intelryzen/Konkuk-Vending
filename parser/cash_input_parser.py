from base_parser import BaseParser

'''
금액 입력
    올바른 입력이 아닙니다.
'''

# 허용 명령어
allows = [0]

class CashInputParser(BaseParser):
    
    # 반환 튜플 형식: (정상 여부), (정상일 경우 명령어(int)나 비정상일 경우 오류메시지)
    def parse(self, input: str) -> tuple[bool, any]:
        command = self.parse_command(input)

        # 뒤로가기(0) 인지 확인
        if command in allows:
            return True, command
       
        input = self.parse_all(input)
       
        # return True, command


# 테스트
if __name__ == "__main__":
    parser = CashInputParser()
    test_input = "   \t\f\v3 dsf\tds\nf \n\n"
    t = parser.parse(test_input)
    print(t)