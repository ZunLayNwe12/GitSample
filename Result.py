x = int(input("Examination Result:"))
if x >= 90 and x < 101:
	print('A')
elif x >= 70 and x < 90:
	print('B')
elif x >= 60:
	print('C')
elif x >= 40:
	print('D')
elif x >= 10 and x < 40:
	print('Fail')
else:
	print('Your typing is wrong')