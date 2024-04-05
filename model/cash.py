import re

from ..config import Currency
from ..config import config as c

Currency_List = [] #권종 클래스 리스트 생성

def Save_Currencies(): #잔돈 파일 생성/저장
	"""
	저장하는 과정에서 저장에 대한 에러는 무시하는지 정해진 것으로 아는데 맞는지 확인 필요함
	"""
	with open(".." + c.cashFilePath, 'w') as file:
		for Currency in c.Currency_List:
			file.write(f"{Currency.value} {Currency.quantity}\n") #공백으로 권종, 개수 분리

def Load_Currencies(): #잔돈 파일 로드
	"""
	잔돈 파일에서 100원, 500원, 1000원, 5000원, 10000원, 50000원 외에 
	다른 권종 있는지 로드하면서 판별하는 과정 필요 -> 무결점 검사에서 추가바람

	또한 권종 개수 이후 다른 문자에 대한 예외 처리 혹은 에러 처리가 필요함
	"""
	with open(c.cashFilePath, 'r') as file:
		for line in file:
			parts = re.split(r'\s+', line.strip()) #횡공백류열1 기준으로 분리
			try:
				value, quantity = parts[0], parts[1]
			except IndexError:
				pass
			c.Currency_List.append(Currency(int(value), int(quantity))) #인스턴스 생성 (리스트)