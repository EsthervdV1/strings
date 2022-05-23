# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

#Part 1

player_1 = "Ruud Gullit"
player_2= "Marco van Basten"

goal_0 = 32
goal_1 = 54

scorers = player_1 + " " + str(goal_0) + ", " + player_2 + " " + str(goal_1)

report = f"{player_1} scored in the {goal_0}nd minute\n{player_2} scored in the {goal_1}th minute"

#Part 2

player = "Frank Rijkaard"
first_name = player[:5]
last_name_len = len(player[6:])
name_short = f"{first_name[0]}. {player[6:]}"

x = len(first_name)
chant = (f"{first_name}! " * x)[:-1]

good_chant = chant[5] != chant[6]