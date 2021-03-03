from turtle import Turtle, Screen
import random
import time

WIDTH = 500
HEIGHT = 400

class Race_Turtle:
    def __init__(self,name,index):
        self.obj = Turtle(shape= "turtle")
        self.obj.color(name)
        self.obj.penup()
        self.obj.shapesize(stretch_wid=1)
        self.obj.goto(x=-(WIDTH/2), y= -(HEIGHT/4) + index*35 )

    def start_racing(self,speed):
        self.obj.forward(speed)
        x,y = self.obj.pos()
        return True if x>=WIDTH/2-23 else False

def create_text():
    text=Turtle()
    text.hideturtle()
    text.penup()
    text.setposition(0, HEIGHT/2-20)
    
    return text

screen=Screen()
screen.setup(width=WIDTH,height=HEIGHT)
screen.listen()
screen.tracer(0)
# Get user's guessing color
guess = screen.textinput(title = "Make your bet", prompt ="who will win the race? Enter a color:")
colors = ["red","orange","yellow","green","blue","purple"]

## create turtle obj using Class
objs = list(Race_Turtle(name=i, index=colors.index(i)) for i in colors)
screen.update()
## Write text on screen
text = create_text()
text.write(f"User's Choice : {guess}", align="center",font=("D2Coding",10,"normal"))


## Turtle Racing
final = False
winner = "None"

while not final:
    screen.update()
    time.sleep(0.1)
    for i in objs:
        
        final = i.start_racing(random.randint(0,10))
        
        if final :
            winner = colors[objs.index(i)]
            break
screen.tracer(1)
# display racing result
text.clear()
if winner == guess:
    text.write(f"You win! The {winner} color turtle is the winner.", align="center",font=("D2Coding",10,"normal"))
else:
    text.write(f"You Lose! The {winner} color turtle is the winner.", align="center",font=("D2Coding",10,"normal"))


screen.exitonclick()

 