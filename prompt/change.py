from config import config as c

def Change(drink):
	change = 0
	for i in range(6):
		change += (c.customer_list[i].value * c.customer_list[i].quantity)
		c.currency_list[i].quantity += c.customer_list[i].quantity
	won = [0] * 6
	change -= drink
	ret = change
	i = 5
	while change > 0:
		if change >= c.currency_list[i].value and c.currency_list[i].quantity > 0:
			change -= c.currency_list[i].value
			c.currency_list[i].quantity -= 1
			won[i] += 1
		else:
			i -= 1
		if i < 0:
			for j in range(6):
				c.currency_list[i].quantity += won[j]
			return False, "오류: 잔돈이 부족합니다."

	ret = "거스름돈: " + str(ret) + "원 ("
	for i in range(5, -1, -1):
		if won[i] > 0:
			ret += str(c.currency_list[i].value) + "원 " + str(won[i]) + "개 "
		c.customer_list[i].quantity = won[i]
	ret += ")"
	return True, ret
