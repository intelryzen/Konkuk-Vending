import re
import sys
import os
from my_parser.base_parser import BaseParser
from config import config as c

class Cash_Utils(BaseParser):
	def save_currencies(self,cash_file_path, Currency): #잔돈 파일 생성/저장
		"""
		저장하는 과정에서 저장에 대한 에러는 무시하는지 정해진 것으로 아는데 맞는지 확인 필요함
		"""
		with open(cash_file_path, 'w') as file:
			for Currency in c.currency_list:
				file.write(f"{Currency.value} {Currency.quantity}\n") #공백으로 권종, 개수 분리

	def load_currencies(self,cash_file_path, Currency): #잔돈 파일 로드
		"""
		잔돈 파일에서 100원, 500원, 1000원, 5000원, 10000원, 50000원 외에 
		다른 권종 있는지 로드하면서 판별하는 과정 필요 -> 무결점 검사에서 추가바람

		또한 권종 개수 이후 다른 문자에 대한 예외 처리 혹은 에러 처리가 필요함
		"""
  
		c.currency_list = [
			Currency(100,0),
			Currency(500,0),
			Currency(1000,0),
			Currency(5000,0),
			Currency(10000,0),
			Currency(50000,0)
		]
		c.customer_list = [
			Currency(100,0),
			Currency(500,0),
			Currency(1000,0),
			Currency(5000,0),
			Currency(10000,0),
			Currency(50000,0)
		]
  
		try:
			with open(cash_file_path, 'r') as file:
				for line in file:
					parts = re.split(r'\s+', line.strip()) #횡공백류열1 기준으로 분리
					if self.is_money_type(parts[0]):
						for Currency in c.currency_list:
							if str(Currency.value) == str(parts[0]):
								Currency.quantity += int(parts[1])
								if self.is_count(str(Currency.quantity)):
									pass
								else:
									print("파일 내 <개수>를 확인하십시오.")
									os.system('pause')
									sys.exit()
					else:
						print("허용되지 않은 권종이 포함된 파일입니다. 파일 내 권종을 확인하십시오.")
						os.system('pause')
						sys.exit()
		except FileNotFoundError:
			print("잔돈 파일이 없습니다. 파일을 생성합니다.")
			self.save_currencies(Cash_Utils, cash_file_path, Currency)
		if self.is_all_quantity_zero(c.currency_list, Currency):
			print("잔돈 파일 내 데이터가 없습니다.")

	def change_currency(self, Currency_Value, Currency_Amount):
		found = False  # Currency 객체를 찾았는지 여부를 추적하는 플래그
		for Currency in c.currency_list:
			if Currency.value == Currency_Value:
				Currency.quantity = Currency_Amount
				found = True  # Currency 객체를 찾았으므로 플래그를 True로 설정
				self.save_currencies(c.CASH_FILE_PATH, Currency)
				msg = str(Currency.value) + "원의 수량이 " + str(Currency.quantity) + "개로 변경되었습니다."
				print(msg)
				break
		if not found:  # Currency 객체를 찾지 못했으면, 예외를 발생시킴
			print("Currency not found.")
