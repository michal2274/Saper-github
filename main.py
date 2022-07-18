import random

#show the empty field
row1 = ["⬜️", "⬜️"]
row2 = ["⬜️", "⬜️"]
map = [row1, row2]
fake_row1 = ["⬜️", "⬜️"]
fake_row2 = ["⬜️", "⬜️"]
fake_map = [fake_row1, fake_row2]
print(f"{row1}\n{row2}")

#randomize the position of the mine
column = random.randint(0, 1)
row = random.randint(0, 1)
#column = 1
#row = 1
map[row][column] = "X"

#check if map works
#print(f"Real map:\n{row1}\n{row2}")

win = False
while win == False:
    # ask for mine location
    guess_column = int(input("Where is the mine? Enter column, \nColumn: ")) - 1
    guess_row = int(input("Row: ")) - 1
    
    # Error check
    if guess_column > 1 or guess_column < 0 or guess_row > 1 or guess_row < 0:
        print("You must choose numbers between 1 and 2!!")
        
    #guess won
    elif map[guess_row][guess_column] == "X":
        fake_map[row][column] = "X"
        print(f"{fake_row1}\n{fake_row2}")
        print("You won!")
        win = True

    # guess missed
    else:
        fake_map[guess_row][guess_column] = "o"
        print(f"{fake_row1}\n{fake_row2}")