# DO NOT delete this line
from diceroll import roll_the_dice

# Copy and paste the work from Task 1 here 
# Name of Player 1
p1_name = "Red"

# Current position of Player 1
p1_position = 0

# Name of Player 2
p2_name = "Blue"

# Current position of Player 2
p2_position = 0

# Positions of snake heads
snake_heads = [25, 44, 65, 76, 99]

# Positions of snake tails
snake_tails = [6, 23, 34, 28, 56]

# Positions of ladder bases
ladder_bases = [8, 26, 38, 47, 66]

# Positions of ladder tops
ladder_tops = [43, 39, 55, 81, 92]

# Rolling the dice for Player 1
# Implementing the logic for Player 1's movement
diceroll = roll_the_dice()
# Calculating the potential new position for Player 1 after the dice roll
p1_total = p1_position + diceroll
# Update position of Player 1
if p1_total <= 100:
    p1_position = p1_total

 
# Rolling the dice for Player 2
# Implementing the logic for Player 2's movement
diceroll = roll_the_dice()
# A new variable for the possible position after rolling the dice
p2_total = p2_position + diceroll
# Update position of Player 2
if p2_total <= 100:
    p2_position = p2_total

# Print the current position of Player 1
print(f"Player {p1_name} is in position {p1_position}")

# Print the current position of Player 2
print(f"Player {p2_name} is in position {p2_position}")

