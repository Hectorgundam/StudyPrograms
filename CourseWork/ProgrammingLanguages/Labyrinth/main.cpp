// Upload Assignment: C++ Investigation 
// COMP3800 - Programming Languages
// Professor Jose Navarro Figueroa

// Labyrinth Group Assignment

// Group Members:
// Juan Pacheco Nadal
// Gian Peña Bartolomei
// Charleen Ramirez Rios
// Diego Reyes Aquino

// Due Date: 2026-03-01

// Program Description:
// A program that solves a labyrinth file provided by a user.

#include <iostream>
#include <fstream>
#include <string>

using namespace std;


// Function name: readLabyrinthFromFile 
// Objective: Read text file containing the labyrinth and store it in the grid structure while making sure that it is rectangular. 
// Parameters:
// grid - array of strings where the labyrinth is stored 
// rows - reference to the number of rows in the labyrinth
// cols - reference to the number of columns in the labyrinth 
 
// Pre-conditions: The user enters the name of an existing file and it’s spelled correctly. The file has to contain only text. Labyrinth size must meet parameters: minimum 8x8, maximum 64x64. 
// Post-conditions: Labyrinth grid will contain all the rows and columns from the file labyrinth, rows and cols will contain the total number of rows and columns respectively. The function itself will return true if it was able to complete this process and false if it encountered an error. 
// Author: Juan Pacheco Nadal, Diego Reyes Aquino, Charleen Ramirez Rios, Gian Peña Bartolomei
// Creation date: 2026/02/07

bool readLabyrinthFromFile(string grid[], int &rows, int &cols) {

    string userInput;
    string filename;

    cout << "Enter labyrinth file name: ";
    getline(cin, userInput);

    if (userInput.length() >= 4 && userInput.substr(userInput.length() - 4) == ".txt") {

        filename = userInput;

    } else {

        filename = userInput + ".txt";

    }

    ifstream in(filename);

    if (!in.is_open()) {

        cout << "Could not open file: " << filename << "\n";
        return false;

    }

    rows = 0;
    cols = -1;

    string line;

    while (getline(in, line)) {

        if (cols == -1) cols = (int)line.length();

        if ((int)line.length() != cols) {

            cout << "Error: labyrinth must be rectangular.\n";
            return false;

        }

        if (cols > 64) {

            cout << "Error: labyrinth exceeds 64 columns.\n";
            return false;

        }

        if (rows >= 64) {

            cout << "Error: labyrinth exceeds 64 rows.\n";
            return false;

        }

        grid[rows] = line;
        rows++;

    }

    in.close();

    // Can't find anything in the file 
    if (rows == 0) {

        cout << "Error: file is empty.\n";
        return false;

    }

    return true;
}


// Function Name: validateLabyrinthSize 
// Objective: Validate that the labyrinth meets the required size: minimum 8x8, maximum 64x64. 
// Parameters: 
// Rows and cols - number of rows and columns in the labyrinth respectively. 

// Pre-conditions: Rows and columns amounts must be set by readLabyrinthFromFile
// Post-conditions: The function returns true if the labyrinth meets the size requirements and returns false if it doesn’t meet the requirements. 
// Author: Diego Reyes Aquino, Juan Pacheco Nadal
// Creation date: 2026/02/09

bool validateLabyrinthSize(int rows, int cols) {

    if (rows < 8 || cols < 8) {

        cout << "Error: labyrinth must be at least 8 rows and 8 columns.\n";
        return false;

    }

    if (rows > 64 || cols > 64) {

        cout << "Error: labyrinth cannot exceed 64 rows or 64 columns.\n";
        return false;

    }

    return true;

}

// Function Name: getYesNoInput 
// Objective: Request a yes or no response from the user and validate it. 
// Parameters:
// Prompt - the message that’s going to be displayed to the user

// Pre-conditions: Prompt contains a yes or no question that is being asked to the user. 
// Post-conditions: The function returns true if the user enters “S” or “s” for yes, and false if the user enters “N” or “n” for no. 
// Author: Charleen Ramirez Rios
// Creation date: 2026/02/07

bool getYesNoInput(const string &prompt) {

    while (true) {

        cout << prompt;

        string input;
        getline(cin, input);

        if (input.length() == 0) continue;

        char c = input[0];

        if (c == 'S' || c == 's') return true;
        if (c == 'N' || c == 'n') return false;

        cout << "Invalid input. Enter S or N.\n";

    }

}


// printLineToScreenAndFile
// Objective: Print the solution process messages onto the screen and to an output file if the user decides to. 
// Parameters:
// Text - Has the message lines that will be printed 
// outFile - pointer to the output file

// Pre-conditions: Decision to print to an output file or not is already made and passed through outFile
// Post-conditions: Solution process messages are printed to the screen and the output file if the user decided to. 
// Author: Gian Peña Bartolomei
// Creation date: 2026/02/16

void printLineToScreenAndFile(const string &text, ofstream *outFile) {

    cout << text << "\n";

    // If the user decided to print to an ouput file as well 
    if (outFile != nullptr && outFile->is_open()) {

        (*outFile) << text << "\n";

    }
}


// Function Name: printGridToScreenAndFile 
// Objective: Prints the rows and columns of the labyrinth with the solution to the screen and to a file if the user decides to. 
// Parameters:
// Grid - the array that contains the labyrinth of solution 
// Rows - the number of rows to print 
// outFile - pointer used to print to the output file if the user decides to

// Pre-conditions: grid has to contain a valid number of rows and they need to be consistent. Decision to print to an output file or not is already made and passed through outFile. 
// Post-conditions: Solution labyrinth grid is printed to the screen and to the output file if the user decided to. 
// Author: Gian Peña Bartolomei
// Creation date: 2026/02/16

void printGridToScreenAndFile(const string grid[], int rows, ofstream *outFile) {

    for (int r = 0; r < rows; r++) {

        printLineToScreenAndFile(grid[r], outFile);

    }
}


// Function Name: findStartAndGoal  
// Objective: Locate the starting point (represented by “S” or “s”) and the end/goal point (represented by “?”) inside the labyrinth. 
// Parameters:
// Grid - array that contains the labyrinth 
// Rows and cols - the number of rows and columns in the labyrinth respectively. 
// startRow and startCol - reference where the starting point row and column are located.
// goalRow and goalCol - reference where the end/goal point row and column are located. 
// Pre-conditions: Grid must contain the labyrinth, rows and columns represent the accurate dimensions of the maze. 
// Post-conditions: Returns true if it was able to locate the starting point and end/goal point rows and columns, and sets the values of startRow, startCol, goalRow, goalCol respectively. If it’s unable to locate the starting point and end/goal point it return false with an error message. 
// Author: Juan Pacheco Nadal, Charleen Ramirez Rios
// Creation date: 2026/02/13

bool findStartAndGoal(const string grid[], int rows, int cols, int &startR, int &startC, int &goalR, int &goalC) {
    
    // Starting point and end/goal point coordinates
    startR = -1;
    startC = -1;
    goalR = -1;
    goalC = -1;

    int startCount = 0;
    int goalCount = 0;

    // Using nested loops to find the coordinates
    for (int r = 0; r < rows; r++) {

        for (int c = 0; c < cols; c++) {

            char ch = grid[r][c];

            if (ch == 'S' || ch == 's') {

                startCount++;
                startR = r;
                startC = c;

            }

            if (ch == '?') {

                goalCount++;
                goalR = r;
                goalC = c;

            }

        }

    }

    // Making sure there is at least one start point and one end/goal point
    if (startCount != 1) {

        cout << "Error: labyrinth must contain exactly one start point.\n";
        return false;

    }

    if (goalCount != 1) {

        cout << "Error: labyrinth must contain exactly one goal point.\n";
        return false;

    }

    return true;
}


// Function Name: stepDirName 
// Objective: Determine the movement directions between two coordinates and defining them as words rather than logic for printing. 
// Parameters:
// fromR - current row 
// FromC - current column
// toR - destination row
// toC - destination column 

// Pre-conditions: The coordinates must represent cells in the labyrinth that are near or adjacent to each other. 
// Post-conditions: Returns the directions as strings (aka words that are easier for the user to read when printed). 
// Author: Diego Reyes Aquino
// Creation date: 2026/02/20

string stepDirName(int fromR, int fromC, int toR, int toC) {
    
    // Defining the directional movements from logic to words the user can understand when printed
    if (toR == fromR && toC == fromC + 1) return "right";
    if (toR == fromR && toC == fromC - 1) return "left";
    if (toR == fromR - 1 && toC == fromC) return "up";

    return "down";
}


// Function Name: solveLabyrinth 
// Objective: Solves the labyrinth by traversing the labyrinth, backtracks if dead ends are encountered and calls on other functions to print the solution and solution process based on the user’s decision.
// Parameters:
// Original - original labyrinth array 
// Rows and cols - number of rows and columns in the labyrinth respectively 
// showProcess - stores if the user wants to print the solution process or not 
// outFile - points to the output file if the user decided to have the program generate one
// Solved - the array with the solution to the labyrinth 
// totalmovesOut - keeps track of the number of moves the user made to traverse the labyrinth 

// Pre-conditions: labyrinth has to meet required parameters, start point and end point have been determined. 
// Post-conditions: Labyrinth has been solved (if a solution exists) and it’s stored in an array that is printed to the screen or to an output file based on the user’s decision. 
// Author: Juan Pacheco Nadal, Diego Reyes Aquino, Charleen Ramirez Rios, Gian Peña Bartolomei
// Creation date: 2026/02/13

bool solveLabyrinth(const string original[], int rows, int cols, bool showProcess, ofstream *outFile, string solved[], int &totalMovesOut) {

    string work[64];

    for (int r = 0; r < rows; r++) work[r] = original[r];

    int startR, startC, goalR, goalC;

    if (!findStartAndGoal(original, rows, cols, startR, startC, goalR, goalC)) {

        return false;

    }

    bool visited[64][64] = { false };

    int pathR[64 * 64];
    int pathC[64 * 64];
    int pathLen = 0;

    // Right, Up, Left, Down
    int dr[4] = { 0, -1, 0, 1 };  
    int dc[4] = { 1, 0, -1, 0 };

    pathR[pathLen] = startR;
    pathC[pathLen] = startC;

    pathLen++;

    visited[startR][startC] = true;

    int totalMoves = 0;

    bool inBacktrack = false;

    int fwdSteps = 0;

    string fwdDir = "";

    int fwdFromR = -1, fwdFromC = -1;
    int fwdToR = -1, fwdToC = -1;

    int btSteps = 0;

    string btDir = "";

    int btToR = -1, btToC = -1;

    auto flushForwardRun = [&]() {

        if (!showProcess) return;

        if (fwdSteps <= 0) return;

        string msg = "The rat moves " + to_string(fwdSteps) + " step";

        if (fwdSteps != 1) msg += "s";

        msg += " " + fwdDir + ", from (" + to_string(fwdFromR) + "," + to_string(fwdFromC) + ")";
        msg += " to (" + to_string(fwdToR) + "," + to_string(fwdToC) + ").";

        printLineToScreenAndFile(msg, outFile);

        fwdSteps = 0;
        fwdDir = "";
        fwdFromR = -1;
        fwdFromC = -1;
        fwdToR = -1;
        fwdToC = -1;

    };

    auto flushBacktrackRun = [&]() {

        if (!showProcess) return;

        if (btSteps <= 0) return;

        string msg = "The rat continues backtracking " + to_string(btSteps) + " step";

        if (btSteps != 1) msg += "s";

        msg += " " + btDir + ", to (" + to_string(btToR) + "," + to_string(btToC) + ").";

        printLineToScreenAndFile(msg, outFile);

        btSteps = 0;
        btDir = "";
        btToR = -1;
        btToC = -1;

    };

    if (showProcess) {

        printLineToScreenAndFile("", outFile);

        printLineToScreenAndFile("Solution Process:", outFile);

        printLineToScreenAndFile("The little rat entered the labyrinth at (" + to_string(startR) + "," + to_string(startC) + "), looking for cheese.",outFile);
    }

    while (pathLen > 0) {

        int curR = pathR[pathLen - 1];
        int curC = pathC[pathLen - 1];

        if (curR == goalR && curC == goalC) {

            flushForwardRun();
            flushBacktrackRun();
            inBacktrack = false;

            for (int r = 0; r < rows; r++) solved[r] = original[r];

            for (int i = 0; i < pathLen; i++) {

                int rr = pathR[i];
                int cc = pathC[i];

                char ch = solved[rr][cc];

                if (ch == 'S' || ch == 's' || ch == '?') continue;

                // The 'o' in our labyrinth represents the actual "final" route taken to solve the labyrinth  
                solved[rr][cc] = 'o';

            }

            if (showProcess) {

                printLineToScreenAndFile("The rat reached the goal at (" + to_string(goalR) + "," + to_string(goalC) + ") after " + to_string(totalMoves) +
                    " step" + (totalMoves == 1 ? "" : "s") + " and eats the cheese.", outFile);

            }

            totalMovesOut = totalMoves;

            return true;

        }

        bool moved = false;

        for (int d = 0; d < 4; d++) {

            int nr = curR + dr[d];
            int nc = curC + dc[d];

            if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) continue;

            char cell = work[nr][nc];

            if (cell == '#') continue;

            if (cell == '?') {

            // The end/goal point can be stepped into even if not marked visited

            } else {

                if (cell != ' ') continue;

                if (visited[nr][nc]) continue;

            }

            if (inBacktrack) {

                flushBacktrackRun();

                if (showProcess) printLineToScreenAndFile("The rat found a new route.", outFile);
                inBacktrack = false;

            }

            string dir = stepDirName(curR, curC, nr, nc);

            if (fwdSteps == 0) {

                fwdDir = dir;
                fwdFromR = nr;
                fwdFromC = nc;
                fwdToR = nr;
                fwdToC = nc;
                fwdSteps = 1;

            } else {

                if (dir == fwdDir) {

                    fwdToR = nr;
                    fwdToC = nc;
                    fwdSteps++;

                } else {

                    flushForwardRun();

                    fwdDir = dir;
                    fwdFromR = nr;
                    fwdFromC = nc;
                    fwdToR = nr;
                    fwdToC = nc;
                    fwdSteps = 1;

                }

            }

            if (cell != '?') visited[nr][nc] = true;

            totalMoves++;

            pathR[pathLen] = nr;
            pathC[pathLen] = nc;

            pathLen++;

            moved = true;
            break;

        }

        if (moved) continue;

        flushForwardRun();

        if (!inBacktrack) {

            inBacktrack = true;

            if (showProcess) {

                printLineToScreenAndFile("The rat encountered a dead end at (" + to_string(curR) + "," + to_string(curC) + ") and starts backtracking.", outFile);

            }

        }

        if (pathLen >= 2) {

            int prevR = pathR[pathLen - 2];
            int prevC = pathC[pathLen - 2];

            string dir = stepDirName(curR, curC, prevR, prevC);

            if (btSteps == 0) {

                btDir = dir;
                btToR = prevR;
                btToC = prevC;
                btSteps = 1;

            } else {

                if (dir == btDir) {

                    btToR = prevR;
                    btToC = prevC;
                    btSteps++;

                } else {

                    flushBacktrackRun();

                    btDir = dir;
                    btToR = prevR;
                    btToC = prevC;
                    btSteps = 1;

                }

            }

        }

        if (work[curR][curC] != 'S' && work[curR][curC] != 's' && work[curR][curC] != '?') {

            work[curR][curC] = '#';

        }

        pathLen--;

    }

    flushForwardRun();

    flushBacktrackRun();

    totalMovesOut = totalMoves;

    return false;

}

int main() {

    string grid[64];
    int rows;
    int cols;

    if (!readLabyrinthFromFile(grid, rows, cols)) {

        cout << "Failed to read labyrinth.\n";
        return 1;

    }

    if (!validateLabyrinthSize(rows, cols)) {

        cout << "Labyrinth size validation failed.\n";
        return 1;

    }

    cout << "\nLabyrinth loaded successfully.\n";
    cout << "Rows: " << rows << "  Cols: " << cols << "\n\n";

    bool showProcess = getYesNoInput("Show solution process on screen? (S or N): ");
    cout << "\n";

    bool saveToFile = getYesNoInput("Generate output text file? (S or N): ");
    cout << "\n";

    ofstream outFile;
    ofstream *outPtr = nullptr;

    if (saveToFile) {

        string outName;
        
        cout << "Enter output file name: ";
        getline(cin, outName);

        if (!(outName.length() >= 4 && outName.substr(outName.length() - 4) == ".txt")) {

            outName = outName + ".txt";

        }

        outFile.open(outName);

        if (!outFile.is_open()) {

            cout << "Could not open output file for writing.\n";
            return 1;

        }

        outPtr = &outFile;
        cout << "Output will be saved to: " << outName << "\n\n";
    }

    string solved[64];
    int totalMoves = 0;

    bool ok = solveLabyrinth(grid, rows, cols, showProcess, outPtr, solved, totalMoves);

    if (!ok) {

        printLineToScreenAndFile("No solution found.", outPtr);

        if (outPtr != nullptr && outPtr->is_open()) outFile.close();

        return 0;

    }

    printLineToScreenAndFile("", outPtr);

    printLineToScreenAndFile("Solution:", outPtr);

    printLineToScreenAndFile("", outPtr);

    printGridToScreenAndFile(solved, rows, outPtr);

    if (outPtr != nullptr && outPtr->is_open()) outFile.close();

    return 0;

}