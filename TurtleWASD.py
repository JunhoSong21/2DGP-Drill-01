import turtle

def MoveLeft():
	turtle.setheading(180)
	turtle.forward(50)
	turtle.stamp()

def MoveRight():
	turtle.setheading(0)
	turtle.forward(50)
	turtle.stamp()

def MoveUp():
	turtle.setheading(90)
	turtle.forward(50)
	turtle.stamp()

def MoveDown():
	turtle.setheading(-90)
	turtle.forward(50)
	turtle.stamp()

def restart():
	turtle.reset()

turtle.shape("turtle")

turtle.onkey(MoveLeft, 'a')
turtle.onkey(MoveRight, 'd')
turtle.onkey(MoveUp, 'w')
turtle.onkey(MoveDown, 's')
turtle.onkey(restart, 'Escape')

turtle.listen()