# This program marks an 'X' spot on a treasure map, depending on the user input

row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ") # The user input is a string, e.g "23"

horizontal = int(position[0]) # This takes the first number in the string which is converted into an integer
vertical = int(position[1]) # This takes the second number in the string which is converted into an integer

map[vertical - 1][horizontal - 1] = "X" # The row is determined by the horizontal number, the position in the row is determined by the vertical number where X will be marked
print(f"{row1}\n{row2}\n{row3}") # This prints out the map with the "X" marked using the user's input
