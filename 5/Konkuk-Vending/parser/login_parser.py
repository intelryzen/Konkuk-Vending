from .base_parser import BaseParser

'''
관리자 로그인
    올바른 입력이 아닙니다.
    아이디와 비밀번호를 구분하여 입력해주세요. 아이디와 비밀번호 사이에는 적어도 하나의 횡공백류열이 필요합니다.
    아이디 또는 비밀번호가 입력규칙을 준수하지 않습니다.
    아이디 또는 비밀번호가 일치하지 않습니다.
'''

# 허용 명령어
allows = [0]

class LoginParser(BaseParser):
    
    # 반환 형식: (정상 여부[bool], 정상일 경우 뒤로가기(0)나 None을, 비정상일 경우 오류메시지[str])
    # id , pw 를 seller 클래스로 대체 예정
    def parse(self, input: str, id: str, pw: str) -> tuple[bool, any]:
        command = self.parse_command(input)

        # 뒤로가기
        if command in allows:
            return True, command
        
        input = self.parse_all(input)
        
        if input == None or (len(input) == 1 and input[0] == ""):
            return False, "오류: 올바른 입력이 아닙니다."

        if len(input) == 1:
            return False, "오류: 아이디와 비밀번호를 구분하여 입력해주세요. 아이디와 비밀번호 사이에는 적어도 하나의 횡공백류열이 필요합니다."

        if len(input) == 2 and len(input[0]) <= 10 and len(input[1]) <= 10 and self.is_word(input[0]) and self.is_word(input[1]):
            if input[0] == id and input[1] == pw:
                return True, None
            else: 
                return False, "오류: 아이디 또는 비밀번호가 일치하지 않습니다."

        return False, "오류: 아이디 또는 비밀번호가 입력규칙을 준수하지 않습니다."

# 테스트
if __name__ == "__main__":
    parser = LoginParser()
    test_input = "   \t\f\va \t \tb\t"
    t = parser.parse(test_input, "a", "b")
    print(t)