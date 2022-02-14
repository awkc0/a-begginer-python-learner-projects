num1 = float(input('First number : '))
op = input('First operator : ')
num2 = float(input('Second number : '))
if op == '÷' and num2 == 0:
	print('Can\'t divide by zero')
	quit()
op2 = input('Second operator (If you do not want to continue type stop) : ')
sum = num1 + num2
sub = num1 - num2
div = num1 / num2
mul = num1 * num2
if op == '+' and op2 == 'stop' :
	print(sum)
	quit()
elif op == '-' and op2 == 'stop' :
	print(sub)
	quit()
elif op == '÷' and op2 == 'stop' :
	print(div)
	quit()
elif op == '×' and op2 == 'stop' :
	print(mul)
	quit()
num3 = float(input('Third number : '))
if op2 == '÷' and num3 == 0:
	print('Can\'t divide by zero')
	quit()

sum1 = sum + num3
sum2 = sub + num3
sum3 = div + num3
sum4 = mul + num3
sub1 = sum - num3
sub2 = sub - num3
sub3 = div - num3
sub4 = mul - num3
div1 = sum / num3
div2 = sub / num3
div3 = div / num3
div4 = mul / num3
mul1 = sum * num3
mul2 = sub * num3
mul3 = div * num3
mul4 = mul * num3
if op == '+' and op2 == '+':
	print(sum1)
elif op == '-' and op2 == '+':
	print(sum2)
elif op == '÷' and op2 == '+':
	print(sum3)
elif op == '×' and op2 == '+':
	print(sum4)
if op == '+' and op2 == '-':
	print(sub1)
elif op == '-' and op2 == '-':
	print(sub2)
elif op == '÷' and op2 == '-':
	print(sub3)
elif op == '×' and op2 == '-':
	print(sub4)
if op == '+' and op2 == '÷':
	print(div1)
elif op == '-' and op2 == '÷':
	print(div2)
elif op == '÷' and op2 == '÷':
	print(div3)
elif op == '×' and op2 == '÷':
	print(div4)
if op == '+' and op2 == '×':
	print(mul1)
elif op == '-' and op2 == '×':
	print(mul2)
elif op == '÷' and op2 == '×':
	print(mul3)
elif op == '×' and op2 == '×':
	print(mul4)