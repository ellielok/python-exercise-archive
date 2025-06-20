from diceroll import roll_the_dice
from typing import Tuple


def initialise_game() -> Tuple[list, list, list, list, list, list]:
    players = ["Red", "Blue", "Green", "White"]
    positions = [0, 0, 0, 0]
    snake_heads = [25, 44, 65, 76, 99]
    snake_tails = [6, 23, 34, 28, 56]
    ladder_bases = [8, 26, 38, 47, 66]
    ladder_tops = [43, 39, 55, 81, 92]
    return players, positions, snake_heads, snake_tails, ladder_bases, ladder_tops

# Input on how many players they would like to play
def get_num_players() -> int:
    while True:
        try:
            num_player = int(input("Please input the number of players: "))
            if 1 <= num_player <= 4:
                return num_player
            else:
                print("The number of players must be between 1 and 4. Please enter a valid number again：")
        
        except Exception:
            print("The number of players must be between 1 and 4. Please enter a valid number again:")
            

def play_game(players, positions, snake_heads, snake_tails, ladder_bases, ladder_tops) -> list:    
    # Define the function of move
    # This function moves a player to a new position.  
    # This function accepts two arguments: player and positon. 
    # player is a string representing the player's color. 
    # position is an integer representing the player's current position.    
    # The return value is an integer representing the current player's finial position. 
    def move(player, position):
        if position != 100:

            # Roll the dice for the player
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
    while True:
        for index in range(len(positions)):
            # The player's position after moving
            position_after_move = move(
                # The player's name
                players[index], 
                # The player's current position 
                positions[index])

            positions[index] = position_after_move
            print(f"Player {players[index]} is in position {positions[index]}")
            if positions[index] == 100:
                print(f"Player {players[index]} has won the game!")
                return positions

def pick_winner(final_positions):
    for index in range(len(final_positions)):
        if final_positions[index] == 100:
            return index
    return -1

def main():
    num_players = get_num_players()
    players, positions, snake_heads, snake_tails, ladder_bases, ladder_tops = initialise_game()
    players = players[0:num_players]
    positions = positions[0:num_players]
    final_positions = play_game(players, positions, snake_heads, snake_tails, ladder_bases, ladder_tops)
    winner = pick_winner(final_positions)
    print(f"The winner is {players[winner]}!")

if __name__ == '__main__':
    main()
