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
		if change >= c.currency_list[i].value and c.currency_list[i].quantity > 99:
			change -= c.currency_list[i].value
			c.currency_list[i].quantity -= 1
			won[i] += 1
		if change < c.currency_list[i].value:
			if c.currency_list[i].quantity < 100:
				i -= 1
			else:
				for j in range(6):
					c.currency_list[j].quantity += won[j]
					c.currency_list[j].quantity -= c.customer_list[j].quantity
				return False, "오류: 잔돈이 포화상태입니다. 관리자에게 문의하거나 타 음료수를 선택해주세요." 
		if i == -1:
			break
	while change > 0:
		if change >= c.currency_list[i].value and c.currency_list[i].quantity > 0:
			change -= c.currency_list[i].value
			c.currency_list[i].quantity -= 1
			won[i] += 1
		else:
			i -= 1
		if i < 0:
			for j in range(6):
				c.currency_list[j].quantity += won[j]
				c.currency_list[j].quantity -= c.customer_list[j].quantity
			return False, "오류: 잔돈이 부족합니다."

	if ret == 0:
		for i in range(6):
			c.customer_list[i].quantity = 0
		return True, "거스름돈: 0원"
	msg = "거스름돈: " + str(ret) + "원 ("
	for i in range(5, -1, -1):
		if won[i] > 0:
			msg += str(c.currency_list[i].value) + "원 " + str(won[i]) + "개 "
		c.customer_list[i].quantity = won[i]
	msg += ")"
	return True, msg
