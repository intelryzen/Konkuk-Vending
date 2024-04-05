import re

from config import Admin
from config import config as c

Admin_List = [] #관리자 클래스 리스트 생성


def Load_Admin(): #관리자 파일 로드
	Admin_List = [] #관리자 클래스 리스트 생성
	"""
	아이디 비밀번호 이후 다른 문자에 대한 예외 처리 혹은 에러 처리가 필요함
	"""
	with open(c.sellerFilePath, 'r') as file:
		for line in file:
			parts = re.split(r'\s+', line.strip()) #횡공백류열1 기준으로 분리
			try:
				name, password = parts[0], parts[1]
			except IndexError:
				pass
			Admin_List.append(Admin(name, password)) #인스턴스 생성 (리스트)

def Save_Admin(): #관리자 파일 생성/저장
	"""
	저장하는 과정에서 저장에 대한 에러는 무시하는것으로 하는것이 맞는지 확인 필요함
	"""
	with open(c.sellerFilePath, 'w') as file:
		for Admin in c.Admin_List:
			file.write(f"{Admin.name} {Admin.password}\n") #공백으로 아이디, 비밀번호 분리