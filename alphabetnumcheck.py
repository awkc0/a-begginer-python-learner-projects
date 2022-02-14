alphabet = '$abcdefghijklmnopqrstuvwxyz'
alphabetnum = input('input the letter : ')
if alphabetnum.islower() == True :
	print(alphabet.index(alphabetnum))
else :
	alphabet = '$ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	print(alphabet.index(alphabetnum))

