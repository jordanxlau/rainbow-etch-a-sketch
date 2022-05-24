from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor("#3E3E3E")

#Declare and initialize a turtle and adjust settings
player = Turtle()
player.speed(10)
player.width(10)
player.hideturtle()

#Other global variables
c = 0 #counter that counts number of colour changes
h = 0 #keeps track of the hex digit we want
#dictionary with all hexadecimal digits, their keys are the corresponding 4-digit binary value
hexdigits = {'0000':'0','0001':'1','0010':'2','0011':'3','0100':'4','0101':'5','0110':'6','0111':'7','1000':'8','1001':'9','1010':'A','1011':'B','1100':'C','1101':'D','1110':'E','1111':'F'}

def hex(inp):
    global hexdigits
    b = str( bin(inp) )
    b = '00000000' + b[2:]
	
    return hexdigits[b[-8] + b[-7] + b[-6] + b[-5]] + hexdigits[b[-4] + b[-3] + b[-2] + b[-1]]

def changeColour():
        global player
        global h, c
        
        if (c < 256):
                player.pencolor("#FF" + hex(h) + "00")
                h+=1
        elif (c >= 256 and c < 512):
                player.pencolor("#" + hex(h) + "FF00")
                h-=1
        elif (c >= 512 and c < 768):
                if (c==512):
                        h = 0
                player.pencolor("#00FF" + hex(h))
                h+=1
        elif (c >= 768 and c < 1024):
                player.pencolor("#00" + hex(h) + "FF")
                h-=1
        elif (c >= 1024 and c < 1280):
                if (c==1024):
                        h = 0
                player.pencolor("#" + hex(h) + "00FF")
                h+=1
        elif (c >= 1280 and c < 1536):
                player.pencolor("#FF00" + hex(h))
                h-=1

        #increment the counter each time
        c+=1
        if (c==1536):#Go back to starting colour
                c=0

#TURTLE MOVEMENT FUNCTIONS
def move():#moves forward
    screen.onkeypress(None, "w")  # disable handler in handler
    changeColour()
    changeColour()
    player.forward(10)
    screen.onkeypress(move, "w")  # reenable handler
    
def left():#turns left and moves forward
    screen.onkeypress(None, "a")  # disable handler in handler
    changeColour()
    changeColour()
    player.forward(10)
    player.left(10)
    screen.onkeypress(left, "a")  # reenable handler
    
def right():#turns right and moves forward
    screen.onkeypress(None, "d")  # disable handler in handler
    changeColour()
    changeColour()
    player.forward(10)
    player.right(10)
    screen.onkeypress(right, "d")  # reenable handler

def undo(): #moves backwards, erasing the colour trail
    screen.onkeypress(None, "s")  # disable handler in handler
    player.undo()
    screen.onkeypress(undo, "s")  # reenable handler

def clear():#clears the turtle window
    screen.onkeypress(None, "c")  # disable handler in handler
    player.clear()
    screen.onkeypress(clear, "c")  # reenable handler

#main
screen.listen()

move()
left()
right()
undo()
clear()

screen.mainloop()
