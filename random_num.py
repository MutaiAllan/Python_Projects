import random

def roll():
    roll = random.randint(1, 6)
    return roll

players = input("Enter number of players(2-4): ")
if players.isdigit():
    players = int(players)
    if 2 <= players <= 4:
        pass
    else:
        print("Must be between 2-4 players")
else:
    print("Invalid input")

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for player in range(players):
        print(f"\n Player number {player + 1}, your turn!")
        current_score = 0

        roll_now = input("Would you want to play (y)? ")
        if roll_now.lower() != "y":
            break
        
        value = roll()
        print(f"You rolled a: {value}")

        player_scores[player] += value
        print(f"Your total score is{player_scores[player]}")
