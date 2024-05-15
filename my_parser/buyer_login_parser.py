from .base_parser import BaseParser

'''
구매자 로그인(2차 확장)##
    올바른 입력이 아닙니다.
    아이디가 입력규칙을 준수하지 않습니다.
'''

# 허용 명령어
allows = [0]

class BuyerLoginParser(BaseParser):
    # 반환 형식: (정상 여부[bool], 정상일 경우 뒤로가기(0)나 None을, 비정상일 경우 오류메시지[str], id와 일치하지 않는 경우 파일 업데이트 후 true, none)
    def parse(self, input: str, id: str) -> tuple[bool, any]:
        command = self.parse_command(input)

        # 뒤로가기
        if command in allows:
            return True, command
        
        input = self.parse_all(input)
        
        if input == None or (len(input) == 1 and input[0] == ""):
            return False, "오류: 올바른 입력이 아닙니다."

        if len(input) == 1 and len(input[0]) <= 10 and self.is_word(input[0]):
            if input[0] == id:
                return True, None
            else:
                # 파일 업데이트 file.util id 생성
                return True, None

        return False, "오류: 아이디가 입력규칙을 준수하지 않습니다."
