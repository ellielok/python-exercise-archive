from diceroll import roll_the_dice, special_roll
from helpers import generate_surprises
from typing import Tuple

def initialise_game(num_players:int = 4) -> dict:
    if num_players == 1:
        players = {"Red":0}
    if num_players ==2:
        players = {"Red":0, "Blue":0}
    if num_players ==3:
        players = {"Red":0, "Blue":0, "Green":0}
    if num_players ==4:
        players = {"Red":0, "Blue":0, "Green":0, "White":0}
    snakes = {"25":6, "44":23, "65":34, "76":28, "99":56}
    ladders = {"8":43, "26":39, "38":55, "47":81, "66":92}
    game = {"players":players, "snakes":snakes, "ladders":ladders}
    return game

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
         

# Define the function of move
# This function moves a player to a new position.  
# This function accepts two arguments: player and positon. 
# player is a string representing the player's color. 
# position is an integer representing the player's current position.    
# The return value is an integer representing the current player's finial position. 
def move(player:str, position:int, game:dict) ->Tuple[int, bool]:
    snakes = game['snakes']
    ladders = game['ladders']
    players = game['players']
    surprise_tiles = game['surprise_tiles']
    skip_next_player = False

    if position != 100:

        # Roll the dice for the player
        diceroll = roll_the_dice()
        total = position + diceroll
        if total <= 100:
            position = total


        # Check if player is either on a snake head or ladder base
        for snake_head, snake_tail in snakes.items():
            if position == int(snake_head):
                position = snake_tail 
                # print(f"Player {player} stepped on a snake and is now in position {position}")

        for ladder_base, ladder_top in ladders.items():
            if position == int(ladder_base):
                position = ladder_top
                # print(f"Player {player} climbed a ladder and is now in position {position}")
        
        for tile in surprise_tiles:
            if position == tile:
                specialroll = special_roll()
                if specialroll == 0:
                    position, skip_next_player = move(player, position, game)
                if specialroll == 1:
                    skip_next_player = True
                if specialroll == 2:
                    for player_temp, position_temp in players.items():
                        if player_temp != player:
                            position_temp_after_move = position_temp - 5
                            if position_temp_after_move < 0:
                                players[player_temp] = 0
                            else:
                                players[player_temp] = position_temp_after_move
                break                
    return position, skip_next_player


def play_game(game: dict) -> str:
    # Call the function generate_surprises to return a list of surprise tile locations
    surprise_tiles = generate_surprises()
    game["surprise_tiles"] = surprise_tiles
    # Commence the game
    skip_next_player = False
    while True:
        players = game['players']

        for player, position in players.items():
            if skip_next_player == True:
                skip_next_player = False
                continue
            else:
                print(f"Player {player} is in position {position}")

                # The player's position after move
                position_after_move, skip_next_player = move(
                    # The player's name
                    player, 
                    # The player's current position 
                    position,
                    # The dictionary
                    game)

                players[player] = position_after_move

                print(f"Player {player} has been moved to position {position_after_move}")

                winner = pick_winner(players)
                if winner != None:
                    return winner

            # Another choice for the function
            # if players[player] == 100:
            #     # print(f"Player {players[index]} is in position {positions[index]}")
            #     # return the winner player
            #     print(f"The winner is found! Here is players' positions: {players}")
            #     return player



def pick_winner(players: dict) -> str:
    for player, position in players.items():
        if position == 100:
            return player
    return None

def turn_by_turn_gameplay():
    game = initialise_game()
    players = game['players']
    del players['Green']
    del players['White']
    snakes = game['snakes']
    ladders = game['ladders']
    surprise_tiles = generate_surprises()
    game["surprise_tiles"] = surprise_tiles
    skip_next_player = False

    while True:
        for player, position in players.items():
            # Players's term
            enter = input("Enter 'roll' or 'quit':")
            while enter != "roll" and enter != "quit":
                enter = input("Enter 'roll' or 'quit':")
            
            if enter == "roll":
                if skip_next_player == True:
                    skip_next_player = False
                    continue
                else:
                    position_after_move, skip_next_player = move(
                        # The player's name
                        player, 
                        # The player's current position 
                        position,
                        # The dictionary
                        game)       
                    players[player] = position_after_move
                    print(f"Player {player} moved from {position} to {players[player]}")       
                    winner = pick_winner(players)
                    if winner != None:
                        print(f"The {player} player has won the game.")
                        return winner
            if enter == "quit":
                print(f"The {player} player has surrendered.")
                return winner





def main():
    num_players = get_num_players()
    game = initialise_game(num_players)
    winner = play_game(game)
    print(f"The winner is {winner}!")

    # Play a turn by turn game
    turn_by_turn_gameplay()

if __name__ == '__main__':
    main()
