'''
프로그램 전체에서 사용될 전역변수와 전역상수가 필요하면 Config 클래스 내 필요한 변수를 선언 및 정의
가져오기: from config import config (as c)
'''

class Config:
    _instance = None

    # 파일 경로
    SELLER_FILE_PATH : str = 'seller.txt'
    CASH_FILE_PATH : str = 'cash.txt'
    DRINKS_FILE_PATH : str = 'drinks.txt'
    SLOTS_FILE_PATH : str = 'machine.txt'
    BUYER_FILE_PATH : str = 'buyers.txt'
    
    buyer_list : list = [] #구매자 정보 리스트 
    admin_list  : list= [] #관리자 클래스 리스트 생성
    currency_list  : list= [] #권종 클래스 리스트 생성
    drinks_list : list = [] # 음료 정보 리스트
    slots_list  : list =[] # 슬롯 관리 리스트
    # customer_list : list[Drink_info] = []
    
    coupon = 0 #쿠폰 개수
    cash_by_cus = 0 # 투입금액 변수 생성
    logged_in_buyer = None

    @staticmethod
    def get_instance():
        if Config._instance is None:
            Config._instance = Config()
        return Config._instance
    
config = Config.get_instance()

