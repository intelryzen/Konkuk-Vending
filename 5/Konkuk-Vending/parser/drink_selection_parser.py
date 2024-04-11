from .base_parser import BaseParser

'''
음료수 선택
    올바른 입력이 아닙니다. (정상 입력일 경우, 0(뒤로가기) 또는 번호 반환 => 파일에 등록된 음료수 번호인지는 별도 검증해야함.)
    금액이 부족합니다. 다른 음료수를 선택해주세요. (외부 입력값 필요, 별도로 처리해야함.)
    잔돈이 부족합니다. (외부 입력값 필요, 별도로 처리해야함.)
    잔돈이 포화상태입니다. 관리자에게 문의하거나 타 권종을 이용해주세요. (외부 입력값 필요, 별도로 처리해야함.)
'''

# 허용 명령어
allows = [0]

class DrinkSelectionParser(BaseParser):
    
    # 반환 형식: (정상 여부[bool], 정상일 경우 뒤로가기(0)나 번호[int]를, 비정상일 경우 오류메시지[str])
    def parse(self, input: str) -> tuple[bool, any]:
        error_message = "오류: 올바른 입력이 아닙니다."
        command = self.parse_command(input)

        # 뒤로가기(0) 인지 먼저 확인
        if command in allows:
            return True, command
       
        # 개행 포함 여부 확인
        if self.contains_newline(input):
            return False, error_message

        input = input.strip()
        if self.is_number(input):
            return True, int(input)
        
        return False, error_message

# 테스트
if __name__ == "__main__":
    parser = DrinkSelectionParser()
    test_input = "   \t\f\v30  \t "
    # test_input = "   \t\f\v0  \t "
    t = parser.parse(test_input)
    print(t)
