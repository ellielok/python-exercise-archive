# Copy and paste everything from Task2
# DO NOT delete this line
from diceroll import roll_the_dice

# Copy and paste the work from Task 1 here 
p1_name = "Red"
p1_position = 0

p2_name = "Blue"
p2_position = 0

# Snake Head Positions
snake_heads = [14, 24, 44, 65, 98]
# Snake Tail Positions
snake_tails = [6, 10, 23, 38, 12]
# Ladder Base Positions
ladder_bases = [4, 17, 45, 55, 76]
# Ladder Tops Positions
ladder_tops = [20, 25, 66, 75, 92]

# Rolling the dice for Player 1
diceroll = roll_the_dice()
p1_total = p1_position + diceroll
if p1_total <= 100:
    p1_position = p1_total

# Check if player 1 is either on a snake head or ladder base
for index in range(len(snake_heads)):
    snake_head = snake_heads[index]
    snake_tail = snake_tails[index]
    # If P1 is on the snake head of the snake
    if p1_position == snake_head:
        p1_position = snake_tail 

for index in range(len(ladder_bases)):
    ladder_base = ladder_bases[index]
    ladder_top = ladder_tops[index]
    
    # If P1 is on the snake head of the snake
    if p1_position == ladder_base:
        p1_position = ladder_top

 
# Rolling the dice for Player 2
diceroll = roll_the_dice()
p2_total = p2_position + diceroll
if p2_total <= 100:
    p2_position = p2_total

# Check if player 2 is either on a snake head or ladder base
for index in range(len(snake_heads)):
    snake_head = snake_heads[index]
    snake_tail = snake_tails[index]

    # If P2 is on the snake head of the snake
    if p2_position == snake_head:
        p2_position = snake_tail 

for index in range(len(ladder_bases)):
    ladder_base = ladder_bases[index]
    ladder_top = ladder_tops[index]
    
    # If P2 is on the snake head of the snake
    if p2_position == ladder_base:
        p2_position = ladder_top

# Print the current position of Player 1
print(f"Player {p1_name} is in position {p1_position}")

# Print the current position of Player 2
print(f"Player {p2_name} is in position {p2_position}")
