# Battleship shots
# Python program

# You're implementing a server for your own Sea Battle game
# In this game, each player has a fixed 5x5 rectangular grid with several ships o it 
# Each ship can be placed either horizontally or vertically
# A ship can't intersect with any other ship, but it can touch them
# A ship can be 1 to 4 grid cells long and will always be 1 grid cell wide 
# All values given below and in tests are [row, col] and are zero based 

# Given the first player's game grid populated with several ships and several shots made by the second player, implement a function that goes through the shots one by one and returns the effect of each 
# If a shot didn't hit a ship, the result is "Missed" 
# If a shot hit a cell that has already been attacked, the result is "Already attacked" 
# A cell is only "Already attacked" if there was a ship in the cell
# A cell will continue to be "Missed" no matter how many times it is attacked if there was a never a ship in in that cell
# If a shot hit ship x and it's not the last remaining cell of this ship, the result is "Attacked ship x"
# If a shot hit ship x and it is the last cell of this ship, the result is "Ship x sunk" 

# Example 
# For grid 
# grid = [[".". "A", "B". "B", "B""],
# [".", "A", ".", ".", "C"]
# [".", ".", ".", ".", "."],
# ["D", "D", ".", ".", "."],
# [".", "E", "E", "E", "E"]]

# and 
# shots = [[0,0],[0,1],[0,2],[1,1],[0,1], [1,4], [2,2], [2,4], [0,3], [0,0], [0,4]]

# The ouput should be 
# solution(grid,shots) = ["Missed", "Attacked ship A", "Attacked ship B", "Ship A sunk", "Already attacked", "Ship C sunk", "Missed", "Missed", "Attacked ship B", "Missed", "Ship B sunk"] 

# Input/Ouput 

# [execution time limit] 4 seconds (py3) 
# [memory limit] 1 GB 
# [input] array.array.string grid 

# The first player's game grid. If a cell is empty, it's represented as ".". If it's not empty, it is represeted as a sigle upper chase character A-Z. It is guaranteed that there is at least one ship on the grid 

# Guaranteed constraints 
# grid.length = 5
# grid[i].length = 5
# grid[i][j] E {".", "A-Z"}

# [input] array.array.integer shots

# The second player's shots. Each shot is represented as two integers, a row-coordinate and a col-coordinate. o-based 

# Guaranteed constraints 
# 1 <= shots.length <= 10^4
# shots[i].length = 2
# 0 <= shots[i][0] < grid.length
# 0 <= shots[i][1] < grid[0].length

# [output] array.string 

# For each shot, return its result

def solution(grid, shots):

    # Test printing the contents of grid 
    # print("The contents of grid are ", grid)

    # Test printing the contents of shots 
    # print("The contents of shots are ", shots)


    # Dictionary for our ship cells 
    shipCount = {}

    # Cycling through the rows in our grid 
    for row in grid: 

        # Cycling through the cells in our rows
        for cell in row: 

            # If the cell doesn't contains "." 
            if cell != ".": 

                
                shipCount[cell] = shipCount.get(cell, 0) + 1

    # Creating an empty set for our attacked cells 
    attackedCells = set()

    # Creating an empty list 
    results = []

    # Cycling through the shots elements
    for shot in shots: 

        # Test printing the contents of shot
        # print("The contents of shot are ", shot)

        # Our rows and columns will be equal to the values that shot contains as [x, y] (our coordinates)
        row, col = shot

        # Test printing the contents of row 
        # print("The contents of row are ", row)

        # Test printing the contents of col
        # print("The contents of col are ", col)

        # Our cell will vbe equal to the the row and col values in our grid as [x, y] 
        # This helps us check what value is within a specific row and column "." or "A-Z" 
        cell = grid[row][col] 

        # Test printing the contents of cell 
        # print("The contents of cell are ", cell)

        # If our cell contains "." - an empty space 
        if cell == ".": 

            # We will add "Missed" as the value obtained when the user shot at that specific coordinate 
            # Using .append() to add the specified parameter to the end of our list 
            results.append("Missed")

            # Stop the current iteration and go to the next one 
            continue 

        # If the row and column value is in the attacked cells list 
        if (row, col) in attackedCells: 

            # We will add "Already attacked" as the value obtained when the user shot at that specific coordinate
            # Using .append() to add the specified parameter to the end of our list
            results.append("Already attacked")

            # Stop the current iteration and go to the next one 
            continue

        # If the row and column value is not in the attacked cells list then we add it to the dictionary
        # Using .add() to add the specified parameter to our dictionary
        attackedCells.add((row, col))

        # Test printing the contents of attackedCells
        # print("The contents of attackedCells are ", attackedCells)

        # We decrease the amount of the cell value in our shipCount by 1 
        # This lets us know that one of our ships was hit and we decrease the amount of ship cells left 
        shipCount[cell] -= 1 

        # Test printing the contents of shipCount[cell]
        # print("The contents of shipCount[cell] are ", shipCount[cell])

        # If the shipCount[cell] value reaches 0 
        if shipCount[cell] == 0: 

            # We will add "Ship -specific ship- sunk"
            # Using .append() to add the specified parameter to the end of our list 
            # Using an f string - (f"{parameter}") - to display content 
            results.append(f"Ship {cell} sunk")

            # Test printing the contents of results
            # print("The contents of results are ", results)

        # Otherwise a ship that still has cells left was hit 
        else: 

            # We will add "Attacked ship -specific ship-"
            # Using .append() to add the specified parameter to the end of our list 
            # Using an f string - (f"{parameter}") - to display content 
            results.append(f"Attacked ship {cell}")
            
            # Test printing the contents of results
            # print("The contents of results are ", results)

    # Return the contents of results
    return results



if __name__ == '__main__':

    grid = [
    [".", "A", "B", "B", "B"],
    [".", "A", ".", ".", "C"],
    [".", ".", ".", ".", "."],
    ["D", "D", ".", ".", "."],
    [".", "E", "E", "E", "E"]
    ]
    
    shots = [[0,0],[0,1],[0,2],[1,1],[0,1],[1,4],[2,2],[2,4],[0,3],[0,4]]

    print(solution(grid, shots))