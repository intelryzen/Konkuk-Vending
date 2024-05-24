import sys
from file_utils import *
from prompt import *
from model import *
from config import config as c

'''
parser/base_parser.py 의 BaseParser 클래스에서

    # 올바른 '권종'인지 확인 (50000|10000|5000|1000|500|100)
    # 올바른 '개수'인지 확인 (0?[0-9])|([1-9][0-9])
    # 올바른 '번호'인지 확인 (0?[1-9])|([1-9][0-9])
    # 개행이 포함되어 있는지 확인
    # 단어인지 확인
    # 한 자리 수 숫자인지
    # 〈횡공백류열0〉 〈명령어〉 〈횡공백류열0〉
    # 〈횡공백류열0〉 <단어> 〈횡공백류열1〉 〈단어〉 (〈횡공백류열1〉 〈단어〉)^* 〈횡공백류열0〉

구현되어 있으니 필요하면 가져다 쓰시면 됩니다.
'''

'''
file_utils 의 cash_util.py에서
    # file_utils.cash_util.Cash_Utils.load_currencies(file_utils.cash_util.Cash_Utils,c.CASH_FILE_PATH, cash.Currency) 인자로 호출해서 사용하시면 됩니다.
    # 불러온 Currency 데이터들은 c.Currency_List에 저장됩니다.
    # file_utils.cash_util.Cash_Utils.save_currencies(file_utils.cash_util.Cash_Utils, c.CASH_FILE_PATH, cash.Currency) 인자로 호출해서 사용하시면 됩니다.
    # cash_util.Change_Currency(file_utils.cash_util.Cash_Utils, cash.Currency, 권종, 개수) 인자로 호출해서 사용할 수 있습니다. (권종 최대, 최소 보유량 조건식 있음)

file_utils 의 seller_util.py에서
    # file_utils.seller_util.Seller_Utils.load_admin(file_utils.seller_util.Seller_Utils, c.SELLER_FILE_PATH,c.admin_list, seller.Admin) 인자로 호출해서 사용하시면 됩니다.
    # 불러온 Admin 데이터들은 c.Admin_List에 저장됩니다.
    # file_utils.seller_util.Seller_Utils.save_admin(file_utils.seller_util.Seller_Utils, c.SELLER_FILE_PATH,c.admin_list, seller.Admin) 인자로 호출해서 사용하시면 됩니다.
'''

def main():
        # 자판기(vending) 인스턴스 생성
            # 자판기가 파일 데이터를 가져와 초기값 저장. 물론 파일을 디코딩하면서 오류생기면 오류문구 출력 후 종료 (클래스가 직접 가져오던, 먼저 가져와서 자판기 클래스의 초기값을 주던 상관없을 것 같습니다.)
       
        #잔돈, 관리자 파일 로드
        Cash_Utils().load_currencies(c.CASH_FILE_PATH, cash.Currency)
        # c.drinks_list = [Drink_info(drink_number=1,name="d",price=11,stock=12)]
        DrinkInfoUtils().read()
        SlotUtils().read()
        BuyerUtils().read()
        Seller_Utils().load_admin(c.SELLER_FILE_PATH, c.admin_list, seller.Admin)
        Cash_Utils().save_currencies(c.CASH_FILE_PATH, cash.Currency)
        
        while(True):
            status, command = Mode().mode_selection_prompt()
            
            if status:
                if command == 0:
                    print("프로그램을 종료합니다.")        
                    exit()
                elif command == 1:
                    DrinkSelection().print_drinks_cus()
                    while True:
                        cash_input_instans = CashInput() 
                        C_result = cash_input_instans.cash_input_prompt() # 금액 입력 프롬프트로 이동
                        if C_result:
                            drink_select_prom = DrinkSelection()
                            drink_select_prom.drink_selection_prompt()
                            continue
                        else :
                            break
                elif command == 2:
                    login_instance = AdminLogin()  # Login 클래스의 인스턴스 생성
                    log_command = login_instance.show_admin_login_prompt()
                    if log_command == 0:
                        continue
                    else:
                        admin_instance = AdminPrompt()
                        admin_instance.admin_prompt() # 로그인 성공 어드민 프롬프트로 이동 
                        continue# 로그인 성공 어드민 프롬프트로이동
            else:
                continue


            # 모드 프롬프트를 호출
                # 모드 프롬프트 내 반복문 
                # 올바른 입력을 받을 때까지 계속 반복 수행함. (ex. 1(관리자 로그인) 또는 2(음료수 보기)를 리턴)
            # Mode()
            # 모드 프롬프트에서 반환한 값을 바탕으로 관리자 로그인 또는 금액 입력 프롬프트 호출
                # ...
            #i = input(c.cashFilePath)
        

# 강제 종료
def exit():
    sys.exit()

# 메인 호출
if __name__ == "__main__":
    main()
