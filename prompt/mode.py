class Mode:
    '''
    모드 선택 프롬프트
    command:
        0: 프로그램 종료
        1: 금액 입력 프롬프트로 이동
        2: 관리자 프롬프트로 이동
        비정상: 모드 선택 프롬프트로 이동
    '''
    def __init__(self):
        self.mode_selection_prompt()

    # 모드 선택 프롬프트
    def mode_selection_prompt(self):
        print("\n<모드 선택>")
        print("0. 종료")
        print("1. 음료수 구매")
        print("2. 관리자 로그인")
        print("-------------------------------------------")
        command = input("모드를 선택해주세요.\n>>>")
        if command == '0':
            print("프로그램을 종료합니다.")
            return True, command
        elif command == '1':
            showdrinklist = ShowDrinksList()
            return True, command
        elif command == '2':
            login = Login()
            return True, command
        else:
            print("오류: 올바른 입력이 아닙니다.\n")
            modeselection = Mode()
            return False, command
    
class ShowDrinksList:

    def __init__(self):
        self.show_drinks_list()

    def show_drinks_list(self):
        print("\n<음료수 목록>")
        # drinks.txt 파일에서 음료수 불러오기
        print("(0. 뒤로가기)")
        print("-------------------------------------------")
        # 금액 입력 프롬프트로 이동

# 모드 선택 프롬프트 테스트
modeselection = Mode()
