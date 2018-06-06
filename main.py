#A simple tic -tac-toe game
#all code by George A. Merrill (except where otherwise noted)
########################################################################################################################
#version 0.0.2 June  6th 2018
#added check that human player's move is legal
#cleanaed up code so there are no nested while loops
#######################################################################################################################
from graphics import * #graphics.py by John Zelle
def drawX(win, p):
    x = p.getX()
    y = p.getY()
    if 100<x<200: x = 150
    elif 200<x<300: x= 250
    elif 300 <x<400: x =350
    else:
            print ('invalid x')
            win.close()

    if 100<y<200: y = 150
    elif 200<y<300: y = 250
    elif 300<y<400: y = 350
    else:
            print('invalid y')
            win.close()
    xline1 = Line(Point(x-40, y+40), Point(x+40, y-40))
    xline1.setWidth(10)
    xline1.setFill('red')
    xline1.draw(win)
    xline2 = Line(Point(x-40,y-40), Point(x+40,y+40))
    xline2.setWidth(10)
    xline2.setFill('red')
    xline2.draw(win)
def drawO(win,p):
    x = p.getX()
    y = p.getY()

    if 100 < x < 200:
        x = 150
    elif 200 < x < 300:
        x = 250
    elif 300 < x < 400:
        x = 350
    else:
        print('invalid x')
        win.close()

    if 100 < y < 200:
        y = 150
    elif 200 < y < 300:
        y = 250
    elif 300 < y < 400:
        y = 350
    else:
        print('invalid y')
        win.close()
    circ1 = Circle(Point(x, y), 42)
    circ1.setWidth(10)
    circ1.setOutline('blue')
    circ1.draw(win)
def getP(x,y):
    px = 250
    py = 250
    if x == 0: px= 150
    if x == 1: px= 250
    if x == 2: px= 350
    if y == 0: py = 350
    if y == 1: py = 250
    if y == 2: py = 150
    return Point(px,py)
def checkWin(bb,i):
    if bb[0][0] + bb[1][1] + bb[2][2] == 3 *i:
        return  True
    if bb[0][2] + bb[1][1] + bb[2][0] == 3 *i:
        return True
    for x in [0,1,2]:
        if bb[x][0] + bb[x][1] + bb[x][2] == 3 * i:
            return True
        if bb[0][x] + bb[1][x] + bb[2][x] == 3 * i:
            return True


    return False
def find(i):
    if 100<i<200: return 0
    elif 200<i<300: return 1
    elif 300<i<400: return 2
def turnO(myboard, mywin): #player's move
    valid = False
    while(valid == False):
        p = mywin.getMouse()
        x = p.getX()
        y = p.getY()
        if (100 <x<400 and 100<y< 400):
            if (myboard[2 -find(y)][find(x)] == 0):
                drawO(mywin, p)
                myboard[2 - find(y)][find(x)] = -1
                valid = True
def turnX(myboard, mywin): #computer's move
    x = 0
    y = 0
    while (myboard[y][x] != 0):
        if x < 2: x += 1
        else:
            x = 0
            y += 1
        if (y > 2 and x >2):
            message = Text(Point(mywin.getWidth() /2, 50),'the game is a draw...')
            message.draw(mywin)
            return (3,3)
    return [x, y]
def init(myboard,mywin):
    board = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]

    mywin.update()
    # <editor-fold desc="draw the board">
    vbar0 = Line(Point(100,100), Point(100,400)) #left side of box
    vbar0.setWidth(10)
    vbar0.draw(mywin)
    vbar1 = Line(Point(200,100), Point(200, 400))
    vbar1.setWidth(10)
    vbar1.draw(mywin)
    vbar2 = Line(Point(300,100), Point(300, 400))
    vbar2.setWidth(10)
    vbar2.draw(mywin)
    vbar3 = Line(Point(400,100), Point(400,400)) #right side of box
    vbar3.setWidth(10)
    vbar3.draw(mywin)
    hbar0 = Line(Point(100, 100), Point(400, 100)) #bottom of box
    hbar0.setWidth(10)
    hbar0.draw(mywin)
    hbar1 = Line(Point(100, 200), Point(400, 200))
    hbar1.setWidth(10)
    hbar1.draw(mywin)
    hbar2 = Line(Point(100, 300), Point(400, 300))
    hbar2.setWidth(10)
    hbar2.draw(mywin)
    hbar3 = Line(Point(100, 400), Point(400, 400)) #top of box
    hbar3.setWidth(10)
    hbar3.draw(mywin)




    #</editor-fold>
def main():
#first initialize a window and a game board
    win = GraphWin('Tic-Tac-Toe',500,500)
    win.yUp()   #yUp by Andrew Harrington (makes coordinates so (0,0) is bottom left)
    board = [[0,0,0],[0,0,0],[0,0,0]] #each inner array is a row (top, middle, bottom)
    #it is important to note that the state of box x,y is stored in board[y][x]
    gameDone = False
    init(board, win)
    message = Text(Point(win.getWidth() / 2, 40), 'Click anywhere to continue.')
    message.draw(win)
    win.getMouse()
    message.undraw()

    while gameDone == False:
        xy = turnX(board, win)
        x = xy[0]
        y = xy[1]
        print ("TurnX, x= "+repr(x)+" y= " + repr(y))
        if (x + y == 6):
            gameDone = True
            break
        else:
            comPoint = getP(x,y)
            drawX(win, comPoint)
            board[y][x] = 1
            if (checkWin(board, 1)):
                message = Text(Point(win.getWidth() / 2, 50), 'X Wins!!!')
                message.setFill('red')
                message.draw(win)
                gameDone = True
                break
        if board[0].count(0) + board[1].count(0) + board[2].count(0) == 0:
            message = Text(Point(win.getWidth() / 2, 50), 'the game is a draw...')
            message.setFill('black')
            message.draw(win)
            gameDone =True
            break
        turnO(board,win)
        if (checkWin(board, -1)):
            message = Text(Point(win.getWidth() / 2, 50), 'O Wins!!!')
            message.setFill('blue')
            message.draw(win)
            gameDone = True
            break


    # <editor-fold desc="prompt user to close window">
    message = Text(Point(win.getWidth()/2,20), 'Click anywhere to quit.')
    message.draw(win)
    win.getMouse()
    win.close()
    #</editor-fold>

main()
