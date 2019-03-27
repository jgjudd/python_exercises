import os
import random

#draw grid
#rando location for player, exit door, monster
#draw player in the grid
#take input for movement
#move players unless invalid move 
#check for win/loss
#clear screen and redraw grid 


CELLS = [(0,0), (1,0), (2,0), (3,0), (4,0),
		(0,1), (1,1), (2,1), (3,1), (4,1),
		(0,2), (1,2), (2,2), (3,2), (4,2),
		(0,3), (1,3), (2,3), (3,3), (4,3),
		(0,4), (1,4), (2,4), (3,4), (4,4)]

def clear_screen():
	os.system('cls' if os.name == 'nt' else 'clear')

def get_locations():
	return random.sample(CELLS, 3) #Sample > Returns 3 unique values from iterable


def move_player(player, move):
	#get player's location
	x, y = player
	if move == 'Left': 
		x -= 1
	if move == 'Right':
		x += 1
	if move == 'Up':
		y -= 1
	if move == 'Down':
		y += 1			 
	return x, y

def get_moves(player):
	moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']	
	x, y = player
	if x == 0:
		moves.remove('Left')
	if x == 4:
		moves.remove('Right')
	if y == 0:
		moves.remove('Up')
	if y == 4:
		moves.remove('Down')			
	return moves 

def game_loop():
	monster, door, player = get_locations()

while True:
	valid_moves = get_moves(player)
	clear_screen()
	print("Welcome to the dungeon!")
	input("Press RETURN to start!")
	clear_screen()
	game_loop()
	print("You're currently in room {}".format(player))
	print("You can move {}".format(", ".join(valid_moves)))
	print("Enter QUIT to quit")

	move = input("> ")
	move = move.upper()

	if move == 'QUIT':
		break
	if move in valid_moves:
		player = move_player(player, move)
	else:
		print("\n ** Walls are hard! Don't run into them! **\n")
		continue

