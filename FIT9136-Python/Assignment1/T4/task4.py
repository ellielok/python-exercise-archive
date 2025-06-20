# DO NOT delete this line
from diceroll import roll_the_dice

# Initialise the players
p1_name = "Red"
p1_position = 0

p2_name = "Blue"
p2_position = 0


# Initialise the snakes and ladders
snake_heads = [25, 44, 65, 76, 99]
snake_tails = [6, 23, 34, 28, 56]
ladder_bases = [8, 26, 38, 47, 66]
ladder_tops = [43, 39, 55, 81, 92]


# Commence the game
while int(p1_position) != 100 or int(p2_position) != 100:
    
    # Rolling the dice for Player 1
    diceroll = roll_the_dice()
    p1_total = p1_position + diceroll
    if p1_total <= 100:
        p1_position = p1_total

    # Check if player 1 is either on a snake head or ladder base
    for index in range(len(snake_heads)):
        snake_head = snake_heads[index]
        snake_tail = snake_tails[index]

        if p1_position == snake_head:
            p1_position = snake_tail 
            print(f"Player Red stepped on a snake and is now in position {p1_position}")

    for index in range(len(ladder_bases)):
        ladder_base = ladder_bases[index]
        ladder_top = ladder_tops[index]

        # Update position of player 1
        if p1_position == ladder_base:
            p1_position = ladder_top
            print(f"Player Red climbed a ladder and is now in position {p1_position}")

    if p1_position == 100:
        winner = "Red"
        break

    # Rolling the dice for Player 2
    diceroll = roll_the_dice()
    p2_total = p2_position + diceroll
    if p2_total <= 100:
        p2_position = p2_total

    # Check if player 2 is either on a snake head or ladder base
    for index in range(len(snake_heads)):
        snake_head = snake_heads[index]
        snake_tail = snake_tails[index]

        if p2_position == snake_head:
            p2_position = snake_tail 
            print(f"Player Blue stepped on a snake and is now in position {p2_position}")


    for index in range(len(ladder_bases)):
        ladder_base = ladder_bases[index]
        ladder_top = ladder_tops[index]

        if p2_position == ladder_base:
            p2_position = ladder_top
            print(f"Player Blue climbed a ladder and is now in position {p2_position}")

    if p2_position == 100:
        winner = "Blue"
        break

    print(f"Player Red is in position {p1_position}\nPlayer Blue is in position {p2_position}")


# Announce the winner
print(f"Player {winner} has reached 100 and is the winner!")








