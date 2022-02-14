num1 = float(input('Type the first number : '))
op = input('Type the operator : ')
num2 = float(input('Type the second number : '))
if op == "+":
	print(num1+num2)
elif op == "-":
	print(num1-num2)
elif op == '÷' and num2 == 0:
	print('Can\'t divide by zero')
elif op == "÷":
	print(num1/num2)
elif op == "×":
	print(num1*num2)
else:
	print('Wrong operator')