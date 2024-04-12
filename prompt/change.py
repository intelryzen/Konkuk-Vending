from config import config as c

def Change():
	change = 0
	for key in parser_money:
		change += key * parser_money[key]
		for i in range(5):
			if c.currency_list[i].value == key:
				c.currency_list[i].quantity += parser_money[key]
	won = [0] * 6
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
			print("잔돈이 부족합니다.")
			return False

	ret = "거스름돈: " + str(change) + "원 ("
	for i in range(5, -1, -1):
		if won[i] > 0:
			ret += str(c.currency_list[i].value) + "원 " + str(won[i]) + "개 "
			for key in parser_money:
				if key == c.currency_list[i].value:
					parser_money[key] = won[i]
	ret += ")"
	print(ret)
	return True
