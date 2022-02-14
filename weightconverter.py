choose = input('''kg to lb (a)
lb to kg (b)
 : ''')
if choose == 'a' :
	kgtolb = float(input('kg to lb : '))
	print(str(kgtolb*2.20462262)+" lb")
elif choose == "b" :
	lbtokg = float(input('lb to kg : '))
	print(str(lbtokg*0.45359237)+" kg")