import os
import time
from Stack import *

class maze:
    def __init__(self) -> None:
        self.maze = [

                    ["X", "X", "X", "X", "X", "X", "X"],

                    ["X", " ", " ", " ", " ", " ", "X"],

                    ["X", "X", "X", " ", "X", " ", " "],

                    ["X", " ", "X", " ", "X", " ", "X"],

                    ["X", " ", " ", " ", "X", "X", "X"],

                    ["X", " ", "X", " ", " ", " ", "X"],

                    ["X", " ", "X", "X", "X", "X", "X"],
                    ]
        self.ply = pos(6, 1)
        self.end = pos(2, 6)
        self.maze[self.ply.y][self.ply.x] = "P"
        self.maze[self.end.y][self.end.x] = "E"
    
    def isInBound(self, y, x):
        if y>=0 and x>=0 and y<len(self.maze) and x<len(self.maze[0]):
            return True
        else:
            return False
    
    def print(self):
        os.system("cls")
        print("\n\n\n")
        for row in self.maze:
            for col in row:
                print(col," ", end="")
            print("")
        print("\n\n\n")
    
    def printEND(self):
        os.system("cls")
        print("\n\n\n")
        print(">>>>> Congraturation!!! <<<<<")
        print("\n\n\n")

    def move_up(self):
        next_move = pos(self.ply.y-1, self.ply.x)
        if self.isInBound(next_move.y,next_move.x):
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "P"
                self.ply = next_move
                time.sleep(0.25)
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        return True
    
    def move_down(self):
        next_move = pos(self.ply.y+1, self.ply.x)
        if self.isInBound(next_move.y,next_move.x):
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "P"
                self.ply = next_move
                time.sleep(0.25)
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        return True

    def move_left(self):
        next_move = pos(self.ply.y, self.ply.x-1)
        if self.isInBound(next_move.y,next_move.x):
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "P"
                self.ply = next_move
                time.sleep(0.25)
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        return True

    def move_right(self):
        next_move = pos(self.ply.y, self.ply.x+1)
        if self.isInBound(next_move.y,next_move.x):
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "P"
                self.ply = next_move
                time.sleep(0.25)
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        return True

class pos:
    def __init__(self) -> None:
        self.y = None
        self.x = None
    
    def __init__(self, y, x) -> None:
        self.y = y
        self.x = x

# ------------------------ #
# ===== MAIN PROGRAM ===== #
# ------------------------ #

m = maze()
m.print()

s = Stack() 
s.push(pos(0,0)) 

def walking(): 
    while True:  
        m.print()  
        walk = m.ply   
        if m.ply.y-1 != s.peek().y: 
            if m.move_up():
              m.print()
            else:
                break
        if m.ply.x+1 != s.peek().x: 
            if m.move_right():
               m.print()
            else:
                break
        
        if m.move_up() == False or m.move_down() == False or m.move_left() == False or m.move_right() == False: 
            m.printEND()
            break               

walking()