# Player 1 Name
p1_name = "Red"

# Player 1 Position
p1_position = 0

# Player 2 Name
p2_name = "Blue"

# Player 2 Position
p2_position = 0

# Snake Head Positions
snake_heads = [14, 38, 44, 46, 49]

# Snake Tail Positions
snake_tails = [10, 6, 23, 25, 29]

# Ladder Base Positions
ladder_bases = [1, 4, 22, 31, 34]

# Ladder Tops Positions
ladder_tops = [17, 35, 42, 50, 48]


import numpy as np


def roll_the_dice():
    return np.random.randint(1, 7)


# Player 1 rolls the dice and the position changes
p1_roll = roll_the_dice()
p1_position =+ p1_roll

# Player 2 rolls the dice and the position changes
p2_roll = roll_the_dice()
p2_position =+ p2_roll

# Print the new positions of the two players
print()


