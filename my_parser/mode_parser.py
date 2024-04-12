from .base_parser import BaseParser

allows = [0, 1, 2]

class ModeParser(BaseParser):
    
    # 반환 형식: (정상 여부[bool], 정상일 경우 명령어(int)나 비정상일 경우 오류메시지[str])
    def parse(self, input: str) -> tuple[bool, any]:
        command = self.parse_command(input)
        if command in allows:
            return True, command
        else: 
            return False, "오류: 올바른 입력이 아닙니다."

if __name__ == "__main__":
    # 모드 선택 프롬프트 테스트
    mode = Mode()
    mode.mode_selection_prompt()
