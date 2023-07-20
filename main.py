import turtle
import random
import time
turtle.pos()
while 1:

    print(turtle.pos())
    #turtle.write(turtle.pos())
    #turtle.hideturtle()
    #time.sleep(.5)
    if((int(turtle.xcor())>300 | int(turtle.ycor()>300)) | (int(turtle.xcor())<-300 | int(turtle.ycor()<-300))):
        turtle.setx(0)
        turtle.sety(0)
    y=random.randint(0,3)
    x = random.random() * 100
    if(y==0):
        turtle.forward(x)
    elif(y==1):
        turtle.left(x)
    elif(y==2):
        turtle.right(x)
    else:
        turtle.back(x)