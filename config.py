'''
프로그램 전체에서 사용될 전역변수와 전역상수가 필요하면 Config 클래스 내 필요한 변수를 선언 및 정의
가져오기: from config import config (as c)
'''

class Config:
    _instance = None

    # 파일 경로
    sellerFilePath : str = 'seller.txt'
    cashFilePath : str = 'cash.txt'
    drinksFilePath : str = 'drinks.txt'
    Admin_List = [] #관리자 클래스 리스트 생성
    Currency_List = []
    @staticmethod
    def get_instance():
        if Config._instance is None:
            Config._instance = Config()
        return Config._instance
    
config = Config.get_instance()

class Currency: #권종 클래스
	def __init__(self, value, quantity):
			self.value = value #권종
			self.quantity = quantity #개수
	def __str__(self):
		return f"{self.value} {self.quantity}"

class Admin: #관리자 클래스
	def __init__(self, name, password):
		self.name = name #아이디
		self.password = password #비밀번호
	def __str__(self):
		return f"{self.name} {self.password}"
