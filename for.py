expenses=[2111,2400,3400,6400,7800,933,8745,546,6554,213]

total=0



for item in range(len(expenses)):
  print("Month", (item+1),"Expense",expenses[item])
  total=total + expenses[item]
print(total)

# Printing in Range 

# for i in range(1,101):
#   print(i*i)