# Sudoku 
# Python program 

# Importing pygame library 
import pygame 

pygame.font.init()

# Variable Window is assigned the display mode settings for our window 
# set_mode() is the display module function which initializes and sets the size of the window 
Window = pygame.display.set.mode((500, 500))

# set_caption() is the display module function which sets the window title
pygame.display.set_caption("SUDOKU GAME by DataFlair") 

x = 0 
z = 0

# Variable diff is being used as the size of a block 
diff = 500 / 9

value = 0 

# Variable defaultgrid is our Sudoku grid of 9x9
# Using a nested list for our Sudoku grid 
defaultgrid = [
        [0, 0, 4, 0, 6, 0, 0, 0, 5],
        [7, 8, 0, 4, 0, 0, 0, 2, 0],
        [0, 0, 2, 6, 0, 1, 0, 7, 8],
        [6, 1, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 7, 5, 4, 0, 0, 6, 1],
        [0, 0, 1, 7, 5, 0, 9, 3, 0],
        [0, 7, 0, 3, 0, 0, 0, 1, 0],
        [0, 4, 0, 2, 0, 6, 0, 0, 7],
        [0, 2, 0, 0, 0, 7, 4, 0, 0],
    ]

# font.SysFont from the pygame library is used to create a font object called font that's a System Font called 
# comicsans of size 40
font = pygame.font.SysFont("comicsans", 40)

# font.SysFont from the pygame library is used to create a font object called font that's a System Font called 
# comicsans of size 20
font1 = pygame.font.SysFont("comicsans", 20)

# 
def cord(pos): 

    global x 
    x = pos[0]//diff
    global z 
    z = pos[1]//diff

# Function that will highlight the cell selected by the user
def highlightBox():

    for k in range(2): 

        # draw.line() is the function that draws a straight line using the parameters provided
        pygame.draw.line(Window, (0, 0, 0), (x * diff-3, (z + k)*diff), (x * diff + diff + 3, (z + k)*diff), 7)

        pygame.draw.line(Window, (0, 0, 0), ( (x + k)* diff, z * diff ), ((x + k) * diff, z * diff + diff), 7) 

# Function that will draw the lines for the Sudoku grids 
def drawLines(): 

    for i in range(9):

        for j in range(9): 

            if defaultgrid[i][j] != 0: 

                # draw.rect() is a function to draw a rectangle with the given parameters 
                pygame.draw.rect(Window, (255,255,0), (i*diff, j*diff, diff+1, diff+1))

                # font.render() is a function to render font with the given parameters 
                text1 = font.render(str(defaultgrid[i][j]), 1, (0,0,0))

                # .blit() is a function that copies the content of one surface to another surface 
                Window.blit(text1, (i*diff+15, j*diff+15))

                for l in range(10): 
                    if l % 3 == 0: 
                        thick = 7 
                    else: 
                        thick = 1 

                    pygame.draw.line(Window, (0,0,0), (0,l * diff), (500, l * diff), thick)

                    pygame.draw.line(Window, (0,0,0), (l*diff, 0), (l*diff,500), thick)

# Function that fills a cell with the value entered by the user  
def fillValue(value): 

    # Variable text1 stores the text entered by the user 
    text1 = font.render(str(value), 1, (0,0,0))
    Window.blit(text1, (x*diff+15, z*diff+15))

# Function that raises/notifies of an error when the wrong value is entered 
def raiseError(): 
    text1 = font.render("wrong", 1, (0,0,0))
    Window.blit(text1, (20, 570))

def raiseError1(): 
    text1 = font.render("wrong! enter a valie key for the game", 1, (0,0,0))
    Window.blit(text1, (20, 570))

# Function that checkes if the value entered by the user is valid 
def validValue(m, k , l, value):

    # range() is the sequence of numbers starting from 0 is returned by range() and increments the number 
    # every time by 1 and stops before the given number

    # range() helps a loop run for as long as the parameter variable is below the parameter given within the parenthesis 
    # The loop will run (for) as long as (parameter) is (in) the (range) of (parameter) 
    for it in range(9): 
        if m[k][it] == value: 
            return False
        if m[it][l] == value: 
            return False
        
    it = k//3 
    jt = l//3 

    for k in range(it*3, it*3+3): 
        for l in range(jt*3, jt*3+3): 
            if m[k][l] == value: 
                return False
    
    return True

# Function that solves the Sudoku game 
def solveGame(defaultgrid,i,j): 

    while defaultgrid[i][j] != 0: 
        if i < 8: 
            i+=1 
        elif i == 8 and j < 8: 
            i=0 
            j+=1
        elif i == 8 and j==8:
            return True
        
    # .event.pump() is a function that puts the events in an event queue
    pygame.event.pump()

    for it in range(1,10): 
        if validValue(defaultgrid, i, j, it) == True: 
            defaultgrid[i][j] = it 
            global x, z 
            x = i 
            z = j 
            Window.fill((255,255,255))
            drawLines()
            highlightBox()

            # .display.update() is a function that helps in updating a portion of the screen 
            pygame.display.update()

            # .time.delay() is a function that causes a time delay by the specified parameter milliseconds
            pygame.time.delay(20)
            if solveGame(defaultgrid, i, j) == 1: 
                return True
            else: 
                defaultgrid[i][j] = 0 
            Window.fill((0,0,0))

            drawLines()
            highlightBox()
            pygame.display.update()
            pygame.time.delay(50)

    return False

# Function that shows the results of the game once it's finished 
def gameResults(): 

    text1 = font.render("game finished", 1, (0,0,0))
    Window.blit(text1, (20, 570))

    # Variable flag is used for running the window 
    flag = True
    flag1 = 0
    flag2 = 0
    rs = 0 
    error = 0 

    while flag: 
        Window.fill((255,182,193))

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                flag = False
            if event.type == pygame.MOUSEBUTTONDOWN: 
                flag1 = 1
                pos = pygame.mouse.get_pos()
                cord(pos)

            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_LEFT: 
                    x-=1 
                    flag1 = 1
                if event.key == pygame.K_RIGHT:
                    x+= 1
                    flag1 = 1
                if event.key == pygame.K_UP:
                    y-= 1
                    flag1 = 1
                if event.key == pygame.K_DOWN:
                    y+= 1
                    flag1 = 1   
                if event.key == pygame.K_1:
                    value = 1
                if event.key == pygame.K_2:
                    value = 2   
                if event.key == pygame.K_3:
                    value = 3
                if event.key == pygame.K_4:
                    value = 4
                if event.key == pygame.K_5:
                    value = 5
                if event.key == pygame.K_6:
                    value = 6
                if event.key == pygame.K_7:
                    value = 7
                if event.key == pygame.K_8:
                    value = 8
                if event.key == pygame.K_9:
                    value = 9 
                if event.key == pygame.K_RETURN:
                    flag2 = 1  
                if event.key == pygame.K_r:
                    rs = 0
                    error = 0
                    flag2 = 0
                    defaultgrid=[
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0]
                    ]
                if event.key == pygame.K_d:
                    rs = 0
                    error = 0
                    flag2 = 0
                    defaultgrid  =[
                        [0, 0, 4, 0, 6, 0, 0, 0, 5],
                        [7, 8, 0, 4, 0, 0, 0, 2, 0],
                        [0, 0, 2, 6, 0, 1, 0, 7, 8],
                        [6, 1, 0, 0, 7, 5, 0, 0, 9],
                        [0, 0, 7, 5, 4, 0, 0, 6, 1],
                        [0, 0, 1, 7, 5, 0, 9, 3, 0],
                        [0, 7, 0, 3, 0, 0, 0, 1, 0],
                        [0, 4, 0, 2, 0, 6, 0, 0, 7],
                        [0, 2, 0, 0, 0, 7, 4, 0, 0],
                    ]

        while flag:
        Window.fill((255,182,193))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = False   
            if event.type == pygame.MOUSEBUTTONDOWN:
                flag1 = 1
                pos = pygame.mouse.get_pos()
                cord(pos)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT
                    x-= 1
                    flag1 = 1
                if event.key == pygame.K_RIGHT:
                    x+= 1
                    flag1 = 1
                if event.key == pygame.K_UP:
                    y-= 1
                    flag1 = 1
                if event.key == pygame.K_DOWN:
                    y+= 1
                    flag1 = 1   
                if event.key == pygame.K_1:
                    value = 1
                if event.key == pygame.K_2:
                    value = 2   
                if event.key == pygame.K_3:
                    value = 3
                if event.key == pygame.K_4:
                    value = 4
                if event.key == pygame.K_5:
                    value = 5
                if event.key == pygame.K_6:
                    value = 6
                if event.key == pygame.K_7:
                    value = 7
                if event.key == pygame.K_8:
                    value = 8
                if event.key == pygame.K_9:
                    value = 9 
                if event.key == pygame.K_RETURN:
                    flag2 = 1  
                if event.key == pygame.K_r:
                    rs = 0
                    error = 0
                    flag2 = 0
                    defaultgrid=[
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0]
                    ]

                if event.key == pygame.K_d:
                    rs = 0
                    error = 0
                    flag2 = 0
                    defaultgrid  =[
                        [0, 0, 4, 0, 6, 0, 0, 0, 5],
                        [7, 8, 0, 4, 0, 0, 0, 2, 0],
                        [0, 0, 2, 6, 0, 1, 0, 7, 8],
                        [6, 1, 0, 0, 7, 5, 0, 0, 9],
                        [0, 0, 7, 5, 4, 0, 0, 6, 1],
                        [0, 0, 1, 7, 5, 0, 9, 3, 0],
                        [0, 7, 0, 3, 0, 0, 0, 1, 0],
                        [0, 4, 0, 2, 0, 6, 0, 0, 7],
                        [0, 2, 0, 0, 0, 7, 4, 0, 0],
                    ]
        
                if flag2 == 1:
                    if solveGame(defaultgrid , 0, 0)== False:
                        error = 1
                    else:
                        rs = 1
                    
                    flag2 = 0   
                if value != 0:           
                    fillValue(value)
                    if validValue(defaultgrid , int(x), int(z), value)== True:
                        defaultgrid[int(x)][int(z)]= value
                        flag1 = 0
                    else:
                        defaultgrid[int(x)][int(z)]= 0
                        raiseError1()  
                    value = 0   
                
                if error == 1:
                    raiseError() 
                if rs == 1:
                    gameResult()       
                drawLines() 
                if flag1 == 1:
                    highlightBox()      
                pygame.display.update() 
            
        pygame.quit()    
