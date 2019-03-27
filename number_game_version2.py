import random 

#prompt to start game 
#Player picks a number between 1 and 10
#Computer guesses until it finds the right number
#new game prompt

def new_game():
	new_game_prompt = input("Play again? Y/n?").lower()
	if new_game_prompt == 'n':
		print("Bye!")
		exit()
	elif new_game_prompt == 'y': 
		game()
		new_game()
	else:
		print("Error. Please restart game")
		exit()	

def game():
	answer = input("Enter a number between 1 and 10: ")
	answer = int(answer)
	count = 0 
	min_guess = 1
	max_guess = 10
	guess_count = 0

	while True:
		guess = random.randint(min_guess, max_guess)
		guess_count += 1

		if guess < answer:
			print("Too low. Try Again.")
			min_guess = guess
			continue
		elif guess > answer:
			print("Too high. Try Again.")
			max_guess = guess
			continue
		elif guess == answer:
			print("Computer's guess {}. Number of guesses: {}".format(guess, guess_count))
			break
		else:
			print("Incorrect")
			if guess_count > 5:
				print("Guess limit exceeded. User wins.")
				break
			else:
				continue

game()
new_game()