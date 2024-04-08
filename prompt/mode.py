class Mode:
    '''
    모드 프롬프트
    '''
    def __init__(self):
        self.mode_select_prompt()

    # 모드 선택 프롬프트 메뉴
    def mode_select_prompt(self):
        print("<모드 선택>")
        print("0. 종료")
        print("1. 음료수 구매")
        print("2. 관리자 로그인")
        print("-------------------------------------------")
        print("모드를 선택해주세요.\n>>>")

# 출력 확인
mode_selector = Mode()
