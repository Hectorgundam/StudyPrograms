# Incomplete 

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
# solution(grid,shots) = ["Missed", "Attacked ship A", "Attacked ship B", "Ship A sunk", "Already attacked", "Ship C sunk", "Missed", "Attacked ship b", "Missed", "Ship B sunk"] 

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
    print("The contents of grid are ", grid)

    # Test printing the contents of shots 
    print("The contents of shots are ", shots)


    # Dictionary for our ship cells 
    shipCount = {}

    for row in grid: 

        for cell in row: 

            if cell != ".": 

                shipCount[cell] = shipCount.get(cell, 0) + 1


    attackedCells = set()

    results = []

    for shot in shots: 

        row, col = shot

        cell = grid[row][col] 

        if cell == ".": 

            results.append("Missed")

            continue 
        if (row, col) in attackedCells: 

            results.append("Already attacked")

            continue

        attackedCells.add((row, col))

        shipCount[cell] -= 1 

        if shipCount[cell] == 0: 

            results.append(f"Ship {cell} sunk")

        else: 

            results.append(f"Attacked ship {cell}")

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