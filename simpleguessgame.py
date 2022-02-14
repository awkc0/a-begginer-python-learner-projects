guess_word = 'zhongli'
guess_lives = 5
what = '\n_ _ _ _ _ _ _\n'
print(what)
print('Your lives are ' + str(guess_lives))
guess = input('Guess the word : ')
while guess != guess_word and guess_lives >1 :
	guess_lives -= 1
	if guess_lives == 4 :
		what = '\nz _ _ _ _ _ _\n'
	elif guess_lives == 3 :
		what = '\nz h _ _ _ _ _\n'
	elif guess_lives == 2 :
		what = '\nz h o _ _ _ _\n'
	elif guess_lives == 1 :
		what = '\nz h o n _ _ _\n'
	print(what)
	print('Your lives is ' + str(guess_lives))
	guess = input('Guess the word : ')
if guess == guess_word :
	print('\nYou won the word is zhongli')
	quit()
print('\nYou lost the word is zhongli')