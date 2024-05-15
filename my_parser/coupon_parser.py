from .base_parser import BaseParser

allows = [1, 2]

class CouponParser(BaseParser):
    
    # 반환 형식: (정상 여부[bool], 정상일 경우 명령어(str)나 비정상일 경우 오류메시지[str])
    def parse(self, input: str) -> tuple[bool, any]:
        command = self.parse_command(input)
        if command in allows:
            return True, command
        else: 
            return False, "오류: 올바른 입력이 아닙니다."