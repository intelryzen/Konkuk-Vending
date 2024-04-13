from my_parser.login_parser import LoginParser
from config import config as c

class Login:
    '''
        관리자 로그인 프롬프트
        command:
            0: 모드 선택 프롬프트로 이동
            그외: 
                비정상: 오류 메시지 + 관리자 로그인 프롬프트로 이동
                정상: "로그인 성공" 관리자 프롬프트로 이동
    '''    
    def __init__(self):
        self.parser = LoginParser()
        
    # 관리자 로그인 프롬프트
    def show_admin_login_prompt(self):
        print("\n<관리자 로그인>")
        print("이전 화면으로 가려면 '0'을 입력해주세요.")
        print("-------------------------------------------")
        while True:
            login_input = input("로그인\n>>>")

            for Admin in c.admin_list:
                is_valid, result = self.parser.parse(login_input, str(Admin.name), str(Admin.password))  # parse 메서드 호출 시 입력 문자열 전달

            if is_valid:
                if result == 0:
                    return 0
                else:
                    print("로그인 성공")
                    return 1
                    '''
                    from .admin_function import Admin
                    Admin()  # 로그인 성공 시 관리자 프롬프트로 이동
                    '''
            else:
                print(result)  # 오류 메시지 출력
                continue

if __name__ == "__main__":
    # 로그인 프롬프트 테스트
    Login()
