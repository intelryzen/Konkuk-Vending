class Login:
    '''
        관리자 로그인 프롬프트
        command:
            0: 모드 선택 프롬프트로 이동
            비정상: 오류 메시지 + 관리자 로그인 프롬프트로 이동
            정상: "로그인 성공" 관리자 프롬프트로 이동
    '''    
    def __init__(self):
        self.admin_login_prompt()

    # 관리자 로그인 프롬프트
    def admin_login_prompt(self):
        print("\n<관리자 로그인>")
        print("이전 화면으로 가려면 '0'을 입려해주세요.")
        print("-------------------------------------------")
        command = input("로그인\n>>>")

# 로그인 프롬프트 테스트
adminlogin = Login()
