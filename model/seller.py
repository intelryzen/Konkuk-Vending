
class Admin: #관리자 클래스
	def __init__(self, name, password):
		self.name = name #아이디
		self.password = password #비밀번호
	def __str__(self):
		return f"{self.name} {self.password}"