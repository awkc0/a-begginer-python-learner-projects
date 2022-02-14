num1 = float(input('Type the first number : '))
op = input('Type the operator : ')
num2 = float(input('Type the second number : '))
def sum():
	return num1 + num2
def sub():
	return num1 - num2
def div():
	return num1 / num2
def mul():
	return num1 * num2
if op == '+':
	print(sum())
elif op == '-':
	print(sub())
elif op == '÷' and num2 == 0:
	print('Can\'t divide by zero')
elif op == '÷':
	print(div())
elif op == '×':
	print(mul())
else :
	print('Wrong operator')