def Change(change):
	won = [0] * 6
	i = 5
	while change > 0:
		if change > Currency_List[i].value and Currency_List[i].quantity > 0:
			change -= Currency_List[i].value
			Currency_List[i].quantity -= 1
			won[i] += 1
		else:
			i -= 1
		if i < 0:
			for j in range(6):
				Currency_List[i].quantity += won[j]
			return False

	ret = "거스름돈: " + str(change) + "원 ("
	for i in range(5, -1, -1):
		if won[i] > 0:
			ret += str(Currency_List[i].value) + "원 " + str(won[i]) + "개 "
	ret += ")"
	return ret
