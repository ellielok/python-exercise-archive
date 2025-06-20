# DO NOT delete this line
from diceroll import roll_the_dice

# Initialise the players
players = ["Red", "Blue", "Green", "White"]
positions = [0, 0, 0, 0]
winner = None

# Initialise the snakes and ladders
snake_heads = [25, 44, 65, 76, 99]
snake_tails = [6, 23, 34, 28, 56]
ladder_bases = [8, 26, 38, 47, 66]
ladder_tops = [43, 39, 55, 81, 92]

# Define the function for each round of the game for a player
def move(player, position):
    if position != 100:

        # Rolling the dice for the player
        diceroll = roll_the_dice()
        total = position + diceroll
        if total <= 100:
            position = total
            

        # Check if player is either on a snake head or ladder base
        for index in range(len(snake_heads)):
            snake_head = snake_heads[index]
            snake_tail = snake_tails[index]

            if position == snake_head:
                position = snake_tail 
                print(f"Player {player} stepped on a snake and is now in position {position}")

        for index in range(len(ladder_bases)):
            ladder_base = ladder_bases[index]
            ladder_top = ladder_tops[index]

            if position == ladder_base:
                position = ladder_top
                print(f"Player {player} climbed a ladder and is now in position {position}")
    return position

# Commence the game
# Input on how many players they would like to play
num_player = int(input("Please input the number of players: "))
while num_player < 1 or num_player > 4:
    num_player = int(input("The number of players must be between 1 and 4. Please enter a valid number again: "))
# Continue the game until a winner is determined
while winner == None:
    for index in range(num_player):
        # The player's position after move
        position_after_move = move(
            # The player's name
            players[index], 

            # The player's current position 
            positions[index]
        )
        positions[index] = position_after_move
        if positions[index] == 100:
                winner = players[index]
                break
        print(f"Player {players[index]} is in position {positions[index]}")

# Announce the winner
print(f"Player {winner} has reached 100 and is the winner!")







