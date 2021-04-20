from turtle import Turtle
from turtle import Screen

hosszuvonal = 98
rovidvonal = 20
kozepesvonal = 70

class Mukodjel:
    def trapezbal(self, turtle):
        turtle.forward(hosszuvonal)
        turtle.left(135)
        turtle.forward(rovidvonal)
        turtle.left(45)
        turtle.forward(kozepesvonal)
        turtle.left(45)
        turtle.forward(rovidvonal)
        turtle.left(135)
        turtle.penup()
        turtle.forward(100)
        turtle.pendown()

    def emerald(self, turtle):
        turtle.left(225)
        turtle.forward(20)
        turtle.right(45)
        turtle.forward(70)
        turtle.right(45)
        turtle.forward(20)
        turtle.right(90)
        turtle.forward(20)
        turtle.right(45)
        turtle.forward(70)
        turtle.right(45)
        turtle.forward(20)
        turtle.right(45)

    def nyolc(self, turtle):
        self.trapezbal(turtle)
        turtle.left(90)
        self.trapezbal(turtle)
        self.trapezbal(turtle)
        turtle.left(90)
        self.trapezbal(turtle)
        turtle.left(90)
        self.trapezbal(turtle)
        self.trapezbal(turtle)
        turtle.left(90)
        turtle.penup()
        turtle.forward(hosszuvonal)
        turtle.left(90)
        turtle.forward(hosszuvonal)
        turtle.right(90)
        turtle.pendown()
        self.emerald(turtle)
        turtle.penup()
        turtle.goto(0, 0)
        turtle.left(90)

    def szinestrapez(self, turtle):
        turtle.fillcolor('red')
        turtle.begin_fill()
        self.trapezbal(turtle)
        turtle.end_fill()

    def __init__(self):
        screen = Screen()
        turtle = Turtle()
        turtle.speed(0)
        self.nyolc(turtle)
        self.szinestrapez(turtle)
        screen.mainloop()

Mukodjel()