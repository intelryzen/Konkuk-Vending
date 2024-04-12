
class Currency: #권종 클래스
	def __init__(self, value, quantity):
			self.value = value #권종
			self.quantity = quantity #개수
	def __str__(self):
		return f"{self.value} {self.quantity}"
