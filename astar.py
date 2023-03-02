import pygame
import sys
import math
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os

screen = pygame.display.set_mode((600, 600))

screencolor = [224, 224, 224]
screen.fill(screencolor)
pygame.display.set_caption("A* Navigator")

class point:
    def __init__(personal, x, y):
        personal.i = x
        personal.j = y
        personal.f = 0
        personal.g = 0
        personal.h = 0
        personal.adjacents = []
        personal.previous = None
        personal.obs = False
        personal.closed = False
        personal.value = 1

    def display(personal, color, st):
        if personal.closed == False :
            pygame.draw.rect(screen, color, (personal.i * w, personal.j * h, w, h), st)
            pygame.display.update()

    def movement(personal, color, st):
        pygame.draw.rect(screen, color, (personal.i * w, personal.j * h, w, h), st)
        pygame.display.update()
        
    def addadjacents(personal, grid):
        i = personal.i
        j = personal.j
        if i < cols-1 and grid[personal.i + 1][j].obs == False:
            personal.adjacents.append(grid[personal.i + 1][j])
        if i > 0 and grid[personal.i - 1][j].obs == False:
            personal.adjacents.append(grid[personal.i - 1][j])
        if j < row-1 and grid[personal.i][j + 1].obs == False:
            personal.adjacents.append(grid[personal.i][j + 1])
        if j > 0 and grid[personal.i][j - 1].obs == False:
            personal.adjacents.append(grid[personal.i][j - 1])

# main screen declaration            
cols = 30
grid = [0 for i in range(cols)]
row = 30
# openset closeset 
openSet = []
closedSet = []
# some already made color combinations
red = (255, 0, 0)
purple = (153,51, 255)
blue = (0, 102, 204) 
# the color around the edges of screen
bordercolor = (0, 102,51)
w = 600 / cols
h = 600 / row
cameFrom = []
# the grid lines color
boxborder= (0,204,102)

# 2d array creation
for i in range(cols):
    grid[i] = [0 for i in range(row)]

# initializing class point
for i in range(cols):
    for j in range(row):
        grid[i][j] = point(i, j)


#default start and end node
start = grid[1][1]
end = grid[28][28]

# the creation of boxes on main window
for i in range(cols):
    for j in range(row):
        grid[i][j].display((boxborder), 1)

# the creation of a different color border around the screen
for i in range(0,row): 
    grid[cols-1][i].obs = True
    grid[cols-1][i].display(bordercolor, 0)
    grid[i][row-1].display(bordercolor, 0)
    grid[i][0].display(bordercolor, 0)
    grid[i][0].obs = True
    grid[i][row-1].obs = True
    grid[0][i].display(bordercolor, 0)
    grid[0][i].obs = True

# SUBMIT/ ENTER button action
def onsubmit():
    global start
    global end
  
    st = startBox.get().split(',')
    ed = endBox.get().split(',')
    start = grid[int(st[0])][int(st[1])]
    end = grid[int(ed[0])][int(ed[1])]
    window.quit()
    window.destroy()
    
# dialogue boxfor user inputs  
window = Tk()
window.configure(background='black')
label = Label(window, text='Enter Starting Points : x,y ( in the range of 1,1 - 28,28)',fg='white', bg='black')
startBox = Entry(window)
label1 = Label(window, text='Enter Ending Points : x,y ( in the range of 1,1 - 28,28)',fg='white', bg='black')
endBox = Entry(window)
var = IntVar()
displaymovement = ttk.Checkbutton(window, text='Click for step by step demo', onvalue=1, offvalue=0, variable=var )
submit = Button(window, text='Enter',bg='blue', fg='white', command=onsubmit)

# the padding, managing and spacing of the labels text in the dialogue box 
displaymovement.grid(columnspan=3, row=3)
submit.grid(columnspan=4, row=4)
label1.grid(row=1, pady=4)
endBox.grid(row=1, column=1, pady=3)
startBox.grid(row=0, column=1, pady=3)
label.grid(row=0, pady=4)

window.update()
mainloop()

# assistance dialogue box 
def printSomething():
    # disappear button
    button.destroy()
    label = Label(root, text= "(1)- First add obstacles between point using 'mouse press or the mouse drag'\n\n  (2)- Then Press the 'ENTER Key' once you are done adding obstacles.\n\n (close this Dialogue Box to Continue)")
    # a new label to the GUI
    label.pack() 

#a new window initiated
root = Tk()

# button design
button = Button(root, text="Guidence \nClick HERE",bg='blue', fg='white', command=printSomething) 
button.pack()
root.mainloop()

# pygame module initialization
pygame.init()
openSet.append(start)

# user invoked functions definition

# creation of obstacles 
def mousePress(x):
    t = x[0]
    w = x[1]
    g1 = t // (600 // cols)
    g2 = w // (600 // row)
    acess = grid[g1][g2]
    if acess != start and acess != end:
        if acess.obs == False:
            acess.obs = True
            acess.display((255, 0, 0), 0)

end.display((0, 102, 204), 0)
start.display((0, 102, 204), 0)

# check for the events occuring during the run
loop = True
while loop:
# initialized events to occur    
    ev = pygame.event.get()
    for event in ev:
# check for if the user presses close button       
        if event.type == pygame.QUIT:
            pygame.quit()
# check for mouse press to add obstacles            
        if pygame.mouse.get_pressed()[0]:
            try:
                pos = pygame.mouse.get_pos()
                mousePress(pos)
            except AttributeError:
                pass
# check for keyboard press (ENTER) to start the Search            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                loop = False
                break
# use of addadjacents function
for i in range(cols):
    for j in range(row):
        grid[i][j].addadjacents(grid)

# heuristic function
def heurisitic(n, e):
    d = math.sqrt((n.i - e.i)**2 + (n.j - e.j)**2)
    return d

# A* Algorithm
def main():
    end.display((0, 102, 204), 0)
    start.display((0, 102, 204), 0)
    if len(openSet) > 0:
        lowestIndex = 0
        for i in range(len(openSet)):
            if openSet[i].f < openSet[lowestIndex].f:
                lowestIndex = i

        current = openSet[lowestIndex]
# shortest path found
        if current == end:
            print('done', current.f)
            #start.display((0, 0, 0),0)
            temp = current.f
            for i in range(round(current.f)):
                current.closed = False
                current.display((0, 0, 0), 0)
                current = current.previous
            end.display((0, 102, 204), 0)

# the output display
            Tk().wm_withdraw()
            result = messagebox.showinfo('Program Finished', ('The shortest distance to find the route is ' + str(temp) + ' blocks.'))

            ag = True
            while ag:
                ev = pygame.event.get()
                for event in ev:
                    if event.type == pygame.KEYDOWN:
                        ag = False
            pygame.quit()

        openSet.pop(lowestIndex)
        closedSet.append(current)
        
# deciding if the movement should be in the neighbor or not and it is represented by a different color 
        adjacents = current.adjacents
        for i in range(len(adjacents)):
            neighbor = adjacents[i]
            if neighbor not in closedSet:
                tempG = current.g + current.value
                if neighbor in openSet:
                    if neighbor.g > tempG:
                        neighbor.g = tempG
                else:
                    neighbor.g = tempG
                    openSet.append(neighbor)

            neighbor.h = heurisitic(neighbor, end)
            neighbor.f = neighbor.g + neighbor.h

            if neighbor.previous == None:
                neighbor.previous = current
    if var.get():
        for i in range(len(openSet)):
            openSet[i].display(purple, 0)

        for i in range(len(closedSet)):
            if closedSet[i] != start:
                closedSet[i].display(blue, 0)
    current.closed = True

# check for the proper working of the project
while True:
    ev = pygame.event.poll()
    if ev.type == pygame.QUIT:
        pygame.quit()
    pygame.display.update()
    main()