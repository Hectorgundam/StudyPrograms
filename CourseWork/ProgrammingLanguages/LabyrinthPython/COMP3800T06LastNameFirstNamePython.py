# Upload Assignment: Python Investigation 
# COMP3800 - Programming Languages
# Professor Jose Navarro Figueroa

# Labyrinth Group Assignment

# Group Members:
# Juan Pacheco Nadal
# Gian Peña Bartolomei
# Charleen Ramirez Rios
# Diego Reyes Aquino

# Due Date: 2026-04-08

# Program Description:
# A program that solves a labyrinth file provided by a user and generates a VRML file from it. 


import os


# Function Name: getFullPath
# Objective: Determine the full path of a file based on the folder where the Python program is stored.
# Parameters:
# fileName - name of the file that will be searched or created
# Pre-conditions: fileName must be a valid text string. The Python program must already be saved in a valid folder.
# Post-conditions: The function returns the full path to the file inside the same folder as the Python program.
# Author: Charleen Ramirez Rios
# Creation date: 2026-03-21
def getFullPath(fileName):

    scriptFolder = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(scriptFolder, fileName)


# Function Name: getYesNoInput
# Objective: Request a yes or no response from the user and validate it.
# Parameters:
# promptMessage - the message that's going to be displayed to the user
# Pre-conditions: promptMessage contains a yes or no question that is being asked to the user.
# Post-conditions: The function returns true if the user enters "S" or "s", and false if the user enters "N" or "n".
# Author: Charleen Ramirez Rios
# Creation date: 2026-03-21
def getYesNoInput(promptMessage):

    while True:

        userInput = input(promptMessage)

        if len(userInput) == 0:
            continue

        # Only the first character is checked in case the user enters a longer response such as "Si" or "No". 
        firstCharacter = userInput[0]

        if firstCharacter == "S" or firstCharacter == "s":
            return True

        if firstCharacter == "N" or firstCharacter == "n":
            return False

        print("Invalid input. Please enter S for yes or N for no.")


# Function Name: printLineToScreenAndFile
# Objective: Print one line of text onto the screen and to an output file if one is being used.
# Parameters:
# textLine - has the line of text that will be printed
# outputFile - file object used to print to the output file if one is being used
# Pre-conditions: textLine must contain valid text. The decision to print to an output file or not is already made and passed 
# through outputFile.
# Post-conditions: The text line is printed to the screen and to the output file if one is being used.
# Author: Charleen Ramirez Rios, Diego Reyes Aquino
# Creation date: 2026-03-22
def printLineToScreenAndFile(textLine, outputFile):

    print(textLine)

    if outputFile is not None:

        outputFile.write(textLine + "\n")


# Function Name: printGridToScreenAndFile
# Objective: Print the rows of the maze or solved maze to the screen and to an output file if one is being used.
# Parameters:
# grid - list that contains the maze or solved maze rows
# totalRows - number of rows to print
# outputFile - file object used to print to the output file if one is being used
# Pre-conditions: grid has to contain a valid number of rows and they need to be consistent. The decision to print to an output file or 
# not is already made and passed through outputFile.
# Post-conditions: The maze rows are printed to the screen and to the output file if one is being used.
# Author: Charleen Ramirez Rios, Diego Reyes Aquino
# Creation date: 2026-03-21
def printGridToScreenAndFile(grid, totalRows, outputFile):

    for currentRow in range(totalRows):

        printLineToScreenAndFile(grid[currentRow], outputFile)

# Function Name: readMazeFile
# Objective: Read a text file containing the maze and store it in the maze structure while making sure that it is rectangular.
# Parameters:
# This function does not receive parameters directly because it asks the user for the file name.
# Pre-conditions: The user enters the name of an existing text file and it is spelled correctly. The file has to contain only text. 
# The maze must be rectangular.
# Post-conditions: The maze list will contain all the rows from the file maze, totalRows and totalColumns will contain the total number 
# of rows and columns respectively, and the function itself will return true if it was able to complete this process and false if it 
# encountered an error.
# Author: Charleen Ramirez Rios, Diego Reyes Aquino
# Creation date: 2026-03-21
def readMazeFile():

    userInput = input("Enter the maze file name: ").strip()

    if len(userInput) >= 4 and userInput[-4:] == ".txt":

        fileName = userInput

    else:

        fileName = userInput + ".txt"

    completePath = getFullPath(fileName)

    maze = []

    try:

        file = open(completePath, "r")

    except:

        print("Could not open file:", fileName)
        print("Looking in:", completePath)
        return [], 0, 0, False

    # The first row determines how many columns the maze should have
    totalColumns = -1

    for currentLine in file:

        currentLine = currentLine.rstrip("\n")

        if totalColumns == -1:

            totalColumns = len(currentLine)

        # Every row after the first one must match that same width.
        if len(currentLine) != totalColumns:

            print("Error: maze must be rectangular.")
            file.close()
            return [], 0, 0, False

        maze.append(currentLine)

    file.close()

    totalRows = len(maze)

    if totalRows == 0:

        print("Error: file is empty.")
        return [], 0, 0, False

    return maze, totalRows, totalColumns, True


# Function Name: getTextureFileName
# Objective: Request the name of a texture file from the user and validate it.
# Parameters:
# promptMessage - the message that's going to be displayed to the user
# Pre-conditions: promptMessage contains a valid question that is being asked to the user. The texture file must exist in the same 
# folder as the Python program and it must contain a valid image extension.
# Post-conditions: The function returns the valid name of the texture file once the user enters an existing file with a valid image 
# extension.
# Author: Charleen Ramirez Rios, Juan Pachecho Nadal, Diego Reyes Aquino, Gian Peña Bartolomei
# Creation date: 2026-03-26
def getTextureFileName(promptMessage):

    while True:

        fileName = input(promptMessage).strip()

        if "." not in fileName:

            print("Error: Please include the file extension.")
            continue

        validExtensions = [".jpg", ".jpeg", ".png"]

        isValidExtension = False

        for currentExtension in validExtensions:

            if fileName.lower().endswith(currentExtension):

                isValidExtension = True
                break

        if not isValidExtension:

            print("Error: Invalid file extension. Please enter a .jpg, .jpeg, or .png file.")
            continue

        completePath = getFullPath(fileName)

        if not os.path.isfile(completePath):

            print("Error: File doesn't exist. Please enter a valid file name.")
            continue

        return fileName


# Function Name: getVrmlFileName
# Objective: Request the name of the VRML output file from the user and validate it.
# Parameters:
# promptMessage - the message that's going to be displayed to the user
# Pre-conditions: promptMessage contains a valid question that is being asked to the user.
# Post-conditions: The function returns a valid VRML file name. If the user does not include an extension, the function adds .wrl. 
# If the user includes an invalid extension, the function asks again.
# Author: Charleen Ramirez Rios, Diego Reyes Aquino, Juan Pachecho Nadal
# Creation date: 2026-03-26
def getVrmlFileName(promptMessage):

    while True:

        fileName = input(promptMessage).strip()

        if fileName == "":

            print("Error: File name cannot be empty.")
            continue

        # If the user only types a name with no file extension, the program adds the VRML extension
        if "." not in fileName:

            fileName += ".wrl"
            return fileName

        if fileName.lower().endswith(".wrl"):

            return fileName

        print("Error: VRML file has to have a .wrl extension.")
        print("Please enter a valid file name or do not include extension.")


# Function Name: validateMazeSize
# Objective: Validate that the maze meets the required size limits.
# Parameters:
# totalRows and totalColumns - number of rows and columns in the maze respectively
# Pre-conditions: totalRows and totalColumns amounts must already be set by readMazeFile.
# Post-conditions: The function returns true if the maze meets the size requirements and returns false if it doesn't meet 
# the requirements.
# Author: Juan Pachecho Nadal, Diego Reyes Aquino, Charleen Ramirez Rios
# Creation date: 2026-03-24
def validateMazeSize(totalRows, totalColumns):

    if totalRows < 8 or totalColumns < 8:

        print("Error: maze must be at least 8 rows and 8 columns.")
        return False

    if totalRows > 64 or totalColumns > 64:

        print("Error: maze cannot exceed 64 rows or 64 columns.")
        return False

    return True


# Function Name: findStartAndExit
# Objective: Locate the starting point and exit point inside the maze.
# Parameters:
# maze - list that contains the maze
# totalRows and totalColumns - the number of rows and columns in the maze respectively
# Pre-conditions: maze must contain the full maze, and totalRows and totalColumns must represent the accurate dimensions of the maze.
# Post-conditions: The function returns true if it was able to locate the starting point and exit point rows and columns, and sets 
# their values respectively. If it's unable to locate them correctly it returns false with an error message.
# Author: Gian Peña Bartolomei, Charleen Ramirez Rios, Diego Reyes Aquino
# Creation date: 2026-03-25
def findStartAndExit(maze, totalRows, totalColumns):

    startRow = -1
    startColumn = -1
    exitRow = -1
    exitColumn = -1

    startCount = 0
    exitCount = 0

    for currentRow in range(totalRows):

        for currentColumn in range(totalColumns):

            currentCharacter = maze[currentRow][currentColumn]

            if currentCharacter == "*":

                startCount += 1
                startRow = currentRow
                startColumn = currentColumn

            if currentCharacter == "+":

                exitCount += 1
                exitRow = currentRow
                exitColumn = currentColumn

    if startCount != 1:

        print("Error: maze must contain exactly one starting point (*).")
        return -1, -1, -1, -1, False

    if exitCount != 1:

        print("Error: maze must contain exactly one exit point (+).")
        return -1, -1, -1, -1, False

    return startRow, startColumn, exitRow, exitColumn, True


# Function Name: stepDirectionName
# Objective: Determine the movement direction between two coordinates and define it as a word rather than logic for printing.
# Parameters:
# fromRow - current row
# fromColumn - current column
# toRow - destination row
# toColumn - destination column
# Pre-conditions: The coordinates must represent cells in the maze that are near or adjacent to each other.
# Post-conditions: The function returns the direction as a string that is easier for the user to read when printed.
# Author: Diego Reyes Aquino, Charleen Ramirez Rios
# Creation date: 2026-03-27
def stepDirectionName(fromRow, fromColumn, toRow, toColumn):

    if toRow == fromRow and toColumn == fromColumn + 1:
        return "right"

    if toRow == fromRow and toColumn == fromColumn - 1:
        return "left"

    if toRow == fromRow - 1 and toColumn == fromColumn:
        return "up"

    return "down"


# Function Name: isWalkable
# Objective: Determine if a maze cell can be used as part of the solution path.
# Parameters:
# cell - character stored in the current maze position
# Pre-conditions: cell must contain a valid character from the maze.
# Post-conditions: The function returns true if the cell can be walked through and false otherwise.
# Author: Charleen Ramirez Rios
# Creation date: 2026-03-27
def isWalkable(cell):

    if cell == "." or cell == " " or cell == "*" or cell == "+":
        return True

    return False


# Function Name: solveMaze
# Objective: Solve the maze by traversing it, backtracking if dead ends are encountered, and storing the final route.
# Parameters:
# originalMaze - original maze list
# totalRows and totalColumns - number of rows and columns in the maze respectively
# showProcess - stores if the user wants to print the solution process or not
# outputFile - file object used if the user decides to print the process to an output file
# Pre-conditions: The maze has to meet the required parameters, and the start point and exit point must already be determined 
# before the solution can be completed.
# Post-conditions: The maze is solved if a solution exists, the final route is stored in solvedMaze and in the path structure, 
# and the function returns true. If there is no solution, the function returns false.
# Author: Charleen Ramirez Rios, Diego  Reyes Aquino
# Creation date: 2026-03-26
def solveMaze(originalMaze, totalRows, totalColumns, showProcess, outputFile):

    workingMaze = []

    for currentRow in range(totalRows):

        workingMaze.append(originalMaze[currentRow])

    startRow, startColumn, exitRow, exitColumn, foundPoints = findStartAndExit(originalMaze, totalRows, totalColumns)

    if not foundPoints:
        return [], [], False

    visitedPositions = []

    for currentRow in range(totalRows):

        visitedRow = []

        for currentColumn in range(totalColumns):

            visitedRow.append(False)

        visitedPositions.append(visitedRow)

    pathRows = []
    pathColumns = []

    # These lists define the order the little rat tries to move: right, up, left, then down
    rowChanges = [0, -1, 0, 1]
    columnChanges = [1, 0, -1, 0]

    pathRows.append(startRow)
    pathColumns.append(startColumn)
    visitedPositions[startRow][startColumn] = True

    totalMoves = 0

    if showProcess:

        printLineToScreenAndFile("", outputFile)
        printLineToScreenAndFile("Solution Process:", outputFile)
        printLineToScreenAndFile("The little rat entered the maze at (" + str(startRow) + "," + str(startColumn) + ").", outputFile)

    while len(pathRows) > 0:

        # The current position is always going to be the last position stored in the path
        currentRow = pathRows[len(pathRows) - 1]
        currentColumn = pathColumns[len(pathColumns) - 1]

        if currentRow == exitRow and currentColumn == exitColumn:

            solvedMaze = []

            for mazeRow in range(totalRows):

                solvedMaze.append(originalMaze[mazeRow])

            for pathIndex in range(len(pathRows)):

                solutionRow = pathRows[pathIndex]
                solutionColumn = pathColumns[pathIndex]

                rowAsList = list(solvedMaze[solutionRow])

                # Only open spaces that are part of the final route are marked with "o",
                # the start and exit symbols stay the same
                if rowAsList[solutionColumn] != "*" and rowAsList[solutionColumn] != "+":

                    rowAsList[solutionColumn] = "o"

                solvedMaze[solutionRow] = "".join(rowAsList)

            if showProcess:

                printLineToScreenAndFile("The little rat reached the exit at (" + str(exitRow) + "," + str(exitColumn) + ") after "
                    + str(totalMoves) + " step" + ("" if totalMoves == 1 else "s") + ".", outputFile)

            finalPath = []

            for pathIndex in range(len(pathRows)):

                finalPath.append((pathRows[pathIndex], pathColumns[pathIndex]))

            return solvedMaze, finalPath, True

        moved = False

        for directionIndex in range(4):

            nextRow = currentRow + rowChanges[directionIndex]
            nextColumn = currentColumn + columnChanges[directionIndex]

            if nextRow < 0 or nextRow >= totalRows or nextColumn < 0 or nextColumn >= totalColumns:
                continue

            currentCell = workingMaze[nextRow][nextColumn]

            if not isWalkable(currentCell):
                continue

            if visitedPositions[nextRow][nextColumn]:
                continue

            visitedPositions[nextRow][nextColumn] = True
            pathRows.append(nextRow)
            pathColumns.append(nextColumn)
            totalMoves += 1
            moved = True

            if showProcess:

                directionName = stepDirectionName(currentRow, currentColumn, nextRow, nextColumn)
                printLineToScreenAndFile("Move " + directionName + " to (" + str(nextRow) + "," + str(nextColumn) + ").",outputFile)

            break

        if moved:
            continue

        if showProcess:

            printLineToScreenAndFile(
                "Dead end at (" + str(currentRow) + "," + str(currentColumn) + "). Backtracking.",
                outputFile
            )

        if workingMaze[currentRow][currentColumn] != "*" and workingMaze[currentRow][currentColumn] != "+":

            rowAsList = list(workingMaze[currentRow])

            # A dead end is marked with a temporary "#" so the program doesn't try to use that same deadend route again
            rowAsList[currentColumn] = "#"
            workingMaze[currentRow] = "".join(rowAsList)

        # Removing the last position from the path is what does the backtracking in the labyrinth
        pathRows.pop()
        pathColumns.pop()

    return [], [], False


# Function Name: gridToVrmlCoordinates
# Objective: Convert the row and column coordinates of the maze into VRML coordinates.
# Parameters:
# row - row of the maze
# column - column of the maze
# mazeWidth and mazeHeight - width and height of the maze respectively
# Pre-conditions: row and column must represent a valid maze position. mazeWidth and mazeHeight must contain the dimensions of the maze.
# Post-conditions: The function returns the x, y, and z coordinates that correspond to that maze position in the VRML scene.
# Author: Diego Reyes Aquino, Charleen Ramirez Rios
# Creation date: 2026-03-26
def gridToVrmlCoordinates(row, column, mazeWidth, mazeHeight):

    # The maze uses row and column positions
    # But VRML places objects around/relative to the center of the scene, so the coordinates need to be adjusted
    xCoordinate = column - (mazeWidth / 2.0) + 0.5
    zCoordinate = row - (mazeHeight / 2.0) + 0.5
    yCoordinate = 0

    return xCoordinate, yCoordinate, zCoordinate


# Function Name: buildVrmlHeader
# Objective: Generate the header and navigation section of the VRML file.
# Parameters:
# This function does not receive parameters.
# Pre-conditions: None.
# Post-conditions: The function returns the text that represents the header and navigation information of the VRML file.
# Author: Diego Reyes Aquino, Charleen Ramirez Rios, Juan Pachecho Nadal, Gian Peña Bartolomei
# Creation date: 2026-03-26
def buildVrmlHeader():

    vrmlText = ""
    vrmlText += "#VRML V2.0 utf8\n\n"
    vrmlText += "NavigationInfo {\n"
    vrmlText += "  avatarSize [0.25, 2, 0.75]\n"
    vrmlText += "}\n\n"

    return vrmlText


# Function Name: buildFloor
# Objective: Generate the VRML code for the floor of the maze.
# Parameters:
# mazeWidth and mazeHeight - width and height of the maze respectively
# wallHeight - height of the maze walls
# floorTexture - name of the image file that will be used as the floor texture
# Pre-conditions: mazeWidth, mazeHeight, and wallHeight must contain valid numeric values. floorTexture must contain a valid 
# image file name.
# Post-conditions: The function returns the VRML code that represents the floor of the maze.
# Author: Diego Reyes Aquino, Charleen Ramirez Rios, Juan Pachecho Nadal, Gian Peña Bartolomei
# Creation date: 2026-03-26
def buildFloor(mazeWidth, mazeHeight, wallHeight, floorTexture):

    # The floor is lowered so the walls are on top of it instead of being centered through/colliding with the floor
    floorPositionY = -(wallHeight / 2.0)

    vrmlText = ""
    vrmlText += "DEF Floor Transform {\n"
    vrmlText += "  translation 0 " + str(floorPositionY) + " 0\n"
    vrmlText += "  children [\n"
    vrmlText += "    Shape {\n"
    vrmlText += "      appearance Appearance {\n"
    vrmlText += "        texture ImageTexture { url [\"" + floorTexture + "\"] }\n"
    vrmlText += "      }\n"
    vrmlText += "      geometry Box {\n"
    vrmlText += "        size " + str(mazeWidth) + " 0.1 " + str(mazeHeight) + "\n"
    vrmlText += "      }\n"
    vrmlText += "    }\n"
    vrmlText += "  ]\n"
    vrmlText += "}\n\n"

    return vrmlText


# Function Name: buildBox
# Objective: Generate the VRML code for one box wall in the maze.
# Parameters:
# xCoordinate, yCoordinate, and zCoordinate - position of the box in the VRML scene
# wallHeight - height of the wall
# wallTexture - name of the image file that will be used as the wall texture
# index - number used to identify the box object
# Pre-conditions: The coordinates must be valid positions in the VRML scene. wallHeight must contain a valid numeric value. 
# wallTexture must contain a valid image file name.
# Post-conditions: The function returns the VRML code that represents one box wall.
# Author: Diego Reyes Aquino, Charleen Ramirez Rios, Juan Pachecho Nadal, Gian Peña Bartolomei
# Creation date: 2026-03-26
def buildBox(xCoordinate, yCoordinate, zCoordinate, wallHeight, wallTexture, index):

    vrmlText = ""
    vrmlText += "DEF Box" + str(index) + " Transform {\n"
    vrmlText += "  translation " + str(xCoordinate) + " " + str(yCoordinate) + " " + str(zCoordinate) + "\n"
    vrmlText += "  children [\n"
    vrmlText += "    Shape {\n"
    vrmlText += "      appearance Appearance {\n"
    vrmlText += "        texture ImageTexture { url [\"" + wallTexture + "\"] }\n"
    vrmlText += "      }\n"
    vrmlText += "      geometry Box {\n"
    vrmlText += "        size 1 " + str(wallHeight) + " 1\n"
    vrmlText += "      }\n"
    vrmlText += "    }\n"
    vrmlText += "  ]\n"
    vrmlText += "}\n\n"

    return vrmlText


# Function Name: buildCone
# Objective: Generate the VRML code for one cone wall in the maze.
# Parameters:
# xCoordinate, yCoordinate, and zCoordinate - position of the cone in the VRML scene
# wallHeight - height of the cone
# wallTexture - name of the image file that will be used as the wall texture
# index - number used to identify the cone object
# Pre-conditions: The coordinates must be valid positions in the VRML scene. wallHeight must contain a valid numeric value. 
# wallTexture must contain a valid image file name.
# Post-conditions: The function returns the VRML code that represents one cone wall.
# Author: Diego Reyes Aquino, Charleen Ramirez Rios, Juan Pachecho Nadal, Gian Peña Bartolomei
# Creation date: 2026-03-26
def buildCone(xCoordinate, yCoordinate, zCoordinate, wallHeight, wallTexture, index):

    vrmlText = ""
    vrmlText += "DEF Cone" + str(index) + " Transform {\n"
    vrmlText += "  translation " + str(xCoordinate) + " " + str(yCoordinate) + " " + str(zCoordinate) + "\n"
    vrmlText += "  children [\n"
    vrmlText += "    Shape {\n"
    vrmlText += "      appearance Appearance {\n"
    vrmlText += "        texture ImageTexture { url [\"" + wallTexture + "\"] }\n"
    vrmlText += "      }\n"
    vrmlText += "      geometry Cone {\n"
    vrmlText += "        height " + str(wallHeight) + "\n"
    vrmlText += "        bottomRadius 0.5\n"
    vrmlText += "        side TRUE\n"
    vrmlText += "        bottom TRUE\n"
    vrmlText += "      }\n"
    vrmlText += "    }\n"
    vrmlText += "  ]\n"
    vrmlText += "}\n\n"

    return vrmlText


# Function Name: buildSolutionTile
# Objective: Generate the VRML code for one tile that represents part of the solution path.
# Parameters:
# xCoordinate and zCoordinate - position of the tile in the VRML scene
# tileIndex - number used to identify the tile object
# wallHeight - height of the maze walls
# Pre-conditions: The coordinates must be valid positions in the VRML scene. tileIndex must contain a valid number. wallHeight must contain a valid numeric value.
# Post-conditions: The function returns the VRML code that represents one solution tile.
# Author: Diego Reyes Aquino, Charleen Ramirez Rios, Juan Pachecho Nadal, Gian Peña Bartolomei
# Creation date: 2026-03-26
def buildSolutionTile(xCoordinate, zCoordinate, tileIndex, wallHeight):

    floorPositionY = -(wallHeight / 2.0)

    # The solution tiles are placed slightly above the floor so they can be seen, otherwise they'd be colliding 
    # with the floor and not visible in the scene
    tilePositionY = floorPositionY + 0.1

    vrmlText = ""
    vrmlText += "DEF PathTile" + str(tileIndex) + " Transform {\n"
    vrmlText += "  translation " + str(xCoordinate) + " " + str(tilePositionY) + " " + str(zCoordinate) + "\n"
    vrmlText += "  children [\n"
    vrmlText += "    Shape {\n"
    vrmlText += "      appearance Appearance {\n"
    vrmlText += "        material Material {\n"
    vrmlText += "          diffuseColor 1 1 0\n"
    vrmlText += "        }\n"
    vrmlText += "      }\n"
    vrmlText += "      geometry Box {\n"
    vrmlText += "        size 0.8 0.1 0.8\n"
    vrmlText += "      }\n"
    vrmlText += "    }\n"
    vrmlText += "  ]\n"
    vrmlText += "}\n\n"

    return vrmlText


# Function Name: buildMazeObjects
# Objective: Generate the VRML code for all wall objects in the maze.
# Parameters:
# maze - list that contains the maze
# totalRows and totalColumns - number of rows and columns in the maze respectively
# wallHeight - height of the maze walls
# wallTexture - name of the image file that will be used as the wall texture
# Pre-conditions: maze must contain a valid maze, totalRows and totalColumns must represent the correct maze dimensions, 
# wallHeight must contain a valid numeric value, and wallTexture must contain a valid image file name.
# Post-conditions: The function returns the VRML code for all box and cone walls in the maze.
# Author: Diego Reyes Aquino, Charleen Ramirez Rios, Juan Pachecho Nadal, Gian Peña Bartolomei
# Creation date: 2026-03-26
def buildMazeObjects(maze, totalRows, totalColumns, wallHeight, wallTexture):

    vrmlText = ""
    boxIndex = 1
    coneIndex = 1

    for currentRow in range(totalRows):

        for currentColumn in range(totalColumns):

            currentCharacter = maze[currentRow][currentColumn]
            xCoordinate, yCoordinate, zCoordinate = gridToVrmlCoordinates(currentRow, currentColumn, totalColumns, totalRows)

            if currentCharacter == "B":

                vrmlText += buildBox(xCoordinate, 0, zCoordinate, wallHeight, wallTexture, boxIndex)
                boxIndex += 1

            elif currentCharacter == "C":

                vrmlText += buildCone(xCoordinate, 0, zCoordinate, wallHeight, wallTexture, coneIndex)
                coneIndex += 1

    return vrmlText


# Function Name: buildSolutionPath
# Objective: Generate the VRML code for all tiles that represent the final solution path.
# Parameters:
# path - list of coordinates that represent the final route of the maze
# totalRows and totalColumns - number of rows and columns in the maze respectively
# wallHeight - height of the maze walls
# Pre-conditions: path must contain valid coordinates from the solved maze. totalRows and totalColumns must represent the correct maze dimensions. wallHeight must contain a valid numeric value.
# Post-conditions: The function returns the VRML code for all tiles that represent the final solution path.
# Author: Diego Reyes Aquino, Charleen Ramirez Rios, Juan Pachecho Nadal, Gian Peña Bartolomei
# Creation date: 2026-03-26
def buildSolutionPath(path, totalRows, totalColumns, wallHeight):

    vrmlText = ""
    tileIndex = 1

    for currentPosition in path:

        row = currentPosition[0]
        column = currentPosition[1]
        xCoordinate, yCoordinate, zCoordinate = gridToVrmlCoordinates(row, column, totalColumns, totalRows)
        vrmlText += buildSolutionTile(xCoordinate, zCoordinate, tileIndex, wallHeight)
        tileIndex += 1

    return vrmlText


# Function Name: writeVrmlFile
# Objective: Create the VRML output file and write the generated VRML code into it.
# Parameters:
# fileName - name of the VRML file that will be created
# content - text that will be written into the file
# Pre-conditions: fileName must be a valid VRML file name. content must contain valid VRML text.
# Post-conditions: The VRML output file is created in the same folder as the Python program if the process is successful. 
# If the process fails, an error message is printed.
# Author: Diego Reyes Aquino, Charleen Ramirez Rios, Juan Pachecho Nadal, Gian Peña Bartolomei
# Creation date: 2026-03-26
def writeVrmlFile(fileName, content):

    completePath = getFullPath(fileName)

    try:

        file = open(completePath, "w")
        file.write(content)
        file.close()
        print()
        print("VRML file created successfully:", fileName)
        print("Saved in:", completePath)
        print()

    except:

        print("Error: Could not write VRML file.")
        print("Tried to save in:", completePath)
        print()


# Function Name: main
# Objective: Execute the full process to read the maze, solve it, generate the VRML code, and create the output file.
# Parameters:
# This function does not receive parameters.
# Pre-conditions: The maze file and texture files must exist in the same folder as the Python program. The maze must meet the 
# required conditions to be solved.
# Post-conditions: The solved maze is printed on the screen if a solution exists, the VRML code is generated, and the output 
# file is created.
# Author: Diego Reyes Aquino, Charleen Ramirez Rios, Juan Pachecho Nadal, Gian Peña Bartolomei
# Creation date: 2026-03-21
def main():

    maze, totalRows, totalColumns, wasReadSuccessful = readMazeFile()

    if not wasReadSuccessful:

        print("Failed to read maze.")
        return

    if not validateMazeSize(totalRows, totalColumns):

        print("Maze size validation failed.")
        return

    # Leaving here for testing purposes in case there is a need to measure the size of the labyrinth
    # print("\nMaze loaded successfully.")
    # print("Rows:", totalRows, " Cols:", totalColumns)
    # print()

    showProcess = getYesNoInput("Show solution process on screen? (S for yes or N for no): ")
    print()

    wallHeight = float(input("Enter wall height in meters: "))
    wallTexture = getTextureFileName("Enter wall texture file name: ")
    floorTexture = getTextureFileName("Enter floor texture file name: ")
    outputVrmlFileName = getVrmlFileName("Enter output VRML file name: ")

    solvedMaze, solutionPath, wasSolvedSuccessfully = solveMaze(maze, totalRows, totalColumns, showProcess, None)

    if not wasSolvedSuccessfully:
        
        print("No solution found.")
        return

    print()
    print("Solution:")
    print()

    printGridToScreenAndFile(solvedMaze, totalRows, None)

    vrmlText = ""
    vrmlText += buildVrmlHeader()
    vrmlText += buildFloor(totalColumns, totalRows, wallHeight, floorTexture)
    vrmlText += buildMazeObjects(maze, totalRows, totalColumns, wallHeight, wallTexture)
    vrmlText += buildSolutionPath(solutionPath, totalRows, totalColumns, wallHeight)

    writeVrmlFile(outputVrmlFileName, vrmlText)


main()