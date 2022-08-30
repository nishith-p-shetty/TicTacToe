#!/usr/local/bin/python3.10

import os

def show_board():
  os.system('clear')
  for i in range(0,9,3):
    print("       -------------")
    print("       | {} | {} | {} |".format(display[i], display[i+1], display[i+2]))
  print("       -------------")

def ip_pos():
    global turn
    pos = int(input("Select Position {}: ".format(p1+" (X)" if turn else p2+" (O)")))
    if(pos >= 1 and pos <= 9 and pos not in pos_c):
      pos_c.append(pos)
      return pos
    else:
      print('Invalid Input:')
      return ip_pos()

def pattern(c):
  if(display[0]==display[1]==display[2]==c  or display[4-1]==display[5-1]==display[6-1]==c or display[7-1]==display[8-1]==display[9-1]==c or display[1-1]==display[4-1]==display[7-1]==c or display[2-1]==display[5-1]==display[8-1]==c or display[3-1]==display[6-1]==display[9-1]==c or display[1-1]==display[5-1]==display[9-1]==c or display[3-1]==display[5-1]==display[7-1]==c):
    return True
  return False
  
def w_d():
  if pattern('X'):
    print(p1,'Wins!!!')
    return False
  
  elif pattern('O'):
    print(p2,'Wins!!!')
    return False
  else:
    return True

def game():
  global turn, p1, p2, pos_c, display
  display = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  p1 = input("Name of Player 1 (X): ")
  p2 = input("Name of Player 2 (O): ")

  for r in range(9):
      show_board()
      if(w_d() == True):
        pos = ip_pos()
        if(turn):
          display[pos-1] = "X"
          turn = False
        else:
          display[pos-1] = "O"
          turn = True
        if(r == 8):
          show_board()
          print("Out of Turns...!!!")

if __name__ == "__main__":
  pos_c = []
  turn = True
  p1,p2 = '',''
  display = []
  game()
  while(True):
    turn = True
    pos_c.clear()
    ta = input('Do you want to try again y/n : ')
    os.system('clear')
    game() if ta=='y' else exit()