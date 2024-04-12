import re

"""
아이디 비밀번호 변경 함수 추가할지 논의 필요함
"""
class Seller_Utils:
	def load_admin(self, seller_file_path, admin_list, Admin): #관리자 파일 로드
		"""
		아이디 비밀번호 이후 다른 문자에 대한 예외 처리 혹은 에러 처리가 필요함
		"""
		try:
			with open(seller_file_path, 'r') as file:
				for line in file:
					parts = re.split(r'\s+', line.strip()) #횡공백류열1 기준으로 분리
					try:
						name, password = parts[0], parts[1]
					except IndexError:
							pass
					admin_list.append(Admin(name, password)) #인스턴스 생성 (리스트)
		except FileNotFoundError:
			print("관리자 로그인 정보 파일이 없습니다. 프로그램을 종료합니다.")
			exit()

		if not admin_list:
			print("관리자 로그인 정보 파일 내 데이터가 없습니다. 프로그램을 종료합니다.")
			exit()

	def save_admin(self, seller_file_path, admin_list, Admin): #관리자 파일 생성/저장
		"""
		저장하는 과정에서 저장에 대한 에러는 무시하는것으로 하는것이 맞는지 확인 필요함
		"""
		with open(seller_file_path, 'w') as file:
			for Admin in admin_list:
				file.write(f"{Admin.name} {Admin.password}\n") #공백으로 아이디, 비밀번호 분리