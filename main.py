import os

def inputPlayers():
    p1 = input("Name of Player 1 [X]: ")
    p2 = input("Name of Player 2 [O]: ")
    if (p1.strip() == '' or p2.strip() == ''):
        os.system('clear')
        p1,p2 = inputPlayers()
    return p1,p2

def inputPosition(p,ch):
    print(p,' [',ch,'] ',end='')
    pos = input(' : Enter Your Position: ')
    pos.strip()
    pos = int(pos)
    if (pos.strip() == ''):
        pos = inputPosition(p,ch)
    if (pos >= 1 and pos <=9 and pos not in e):
        e.append(pos)
        return pos
    else:
        print('Invalid Input')
        return inputPosition(p,ch)

def printBoard():
    os.system('clear')
    for i in range(1,10,3):
        print("-------------")
        print("| {} | {} | {} |".format(d[i],d[i+1],d[i+2]))
    print("-------------")


def patternCheck(c):
    if(d[1] == d[2] == d[3] == c or
       d[4] == d[5] == d[6] == c or
       d[7] == d[8] == d[9] == c or
       d[1] == d[4] == d[7] == c or
       d[2] == d[5] == d[8] == c or
       d[3] == d[6] == d[9] == c or
       d[1] == d[5] == d[9] == c or
       d[3] == d[5] == d[7] == c ):
        return True
    return False

def turner():
    global turn
    if turn == 1:
        return p1
    else:
        return p2
def turner2():
    global turn
    if turn == 1:
        return 'X'
    else:
        return 'O'
def game():
    global turn
    for r in range(1,10):
        printBoard()
        pos = inputPosition(turner(),turner2())
        d[pos] = turner2() 
        if patternCheck(turner2()):
            printBoard()
            print('Congradulations: ',turner())
            return 0
        turn*=-1
        printBoard()
    print("Out of turns: Draw")


os.system('clear')
p1,p2 = inputPlayers()
while True:
    e = []
    d = [0,1,2,3,4,5,6,7,8,9]
    print(e)
    turn = 1
    game()
    if input('Do you want to play again y/n : ') == 'n':
        exit()
