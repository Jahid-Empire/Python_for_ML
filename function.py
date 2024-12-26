def expTotal(exp):
  total=0
  for item in exp:
    total = total + item
  return total
JahidExpenses = [
    1200, 1300, 1250, 1400, 1300, 1350, 1300, 1400, 1350, 1300, 1400, 1300
]
HassanExpenses = [
    150, 160, 155, 170, 165, 160, 175, 180, 170, 160, 150, 145
]

jahidex= expTotal(JahidExpenses)
hassanex= expTotal(HassanExpenses)

print("Jahid Expenses for 12 moths in 2023 is:  ", jahidex)
print("Hassan Expenses for 12 moths in 2023 is:  ", hassanex)


def printPattern(n):
  for i in range(n):
    s = ''
    for j in range(i+1):
      s = s+'*'
    print(s)

print(printPattern(3))


