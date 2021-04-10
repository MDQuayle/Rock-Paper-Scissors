import random
player_wins = 0
computer_wins = 0
winning_score = 2

while player_wins < winning_score and computer_wins < winning_score:
	print(f"Player wins: {player_wins} Computer wins: {computer_wins}")
	print("Hello! Welcome to Rock Paper Scissors! \nRock \nPaper \nScissors!")
	player = input("Enter Player One's Choice: ").lower()
	if player == "quit" or player == "q":
		break
	ran_num = random.randint(0,2)
	if ran_num == 0:
		computer = "rock"
	elif ran_num == 1:
		computer = "paper"
	else:
		computer = "scissors"
	print(f"Computer plays {computer}")
	if player == "rock": 
		if computer == "scissors":
			print("You win!")
			player_wins += 1
		if computer == "paper":
			print("computer wins!")
			computer_wins +=1
		if computer == "rock":
			print("Tie!")
	elif player == "scissors":
		if computer == "paper":
			print("You win!")
			player_wins += 1
		if computer == "rock":
			print("computer wins!")
			computer_wins +=1
		if computer == "scissors":
			print("Tie!")
	elif player == "paper": 
		if computer == "rock":
			print("You win!")
			player_wins += 1
		if computer == "scissors":
			print("computer wins!")
			computer_wins +=1
		if computer == "paper":
			print("Tie!")
	else: 
		print("Please enter a valid move!")
if player_wins > computer_wins:
	print(f"You win. Heck yeah! Final score Player:{player_wins} Computer:{computer_wins}")
elif player_wins == computer_wins:
	print(f"Tied! What a waste! Final score Player:{player_wins} Computer:{computer_wins}")
else:
	print(f"Oh no :( Final score Player:{player_wins} Computer:{computer_wins}")
