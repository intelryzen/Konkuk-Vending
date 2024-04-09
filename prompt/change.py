def change(cash):
  ch = list()
  while cash > 50000 and 50000.quantity > 0:
    50000.quantity -= 1
    ch[50000] += 1
    cash -= 50000
  if cash == 0:
    break
  while cash > 10000 and 10000.quantity > 0:
    10000.quantity -= 1
    ch[10000] += 1
    cash -= 10000
  if cash == 0:
    break
  while cash > 5000 and 1000.quantity > 0:
    5000.quantity -= 1
    ch[5000] += 1
    cash -= 5000
  if cash == 0:
    break
  while cash > 1000 and 1000.quantity > 0:
    1000.quantity -= 1
    ch[1000] += 1
    cash -= 1000
  if cash == 0:
    break
  while cash > 500 and 500.quantity > 0:
    500.quantity -= 1
    ch[500] += 1
    cash -= 500
  if cash == 0:
    break
  while cash > 100 and 100.quantity > 0:
    100.quantity -= 1
    ch[100] += 1
    cash -= 100
  if cash == 0:
    break
