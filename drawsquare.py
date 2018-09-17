
from turtle import Turtle
def drawSquare(t, x, y, length):
	t.goto(x, y)
	t.setheading(270)
	t.pencolor(color)
	t.down()
	for count in range(4):
		t.forward(length)
		t.left(90)

def main():
	color = input("What color do you want the pen to be?")
	length = int(input("How long do you want each side?"))
	myTurtle = Turtle()
	drawSquare(myTurtle, 100, 100, length, color)
	input() 

main()