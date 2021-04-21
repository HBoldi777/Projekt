from turtle import *

hosszuvonal = 98
rovidvonal = 20
kozepesvonal = 70


class Szamok:

    screen = Screen()

    def trapezbal(self):
        self.turtle.fillcolor('red')
        self.turtle.begin_fill()
        self.turtle.forward(hosszuvonal)
        self.turtle.left(135)
        self.turtle.forward(rovidvonal)
        self.turtle.left(45)
        self.turtle.forward(kozepesvonal)
        self.turtle.left(45)
        self.turtle.forward(rovidvonal)
        self.turtle.left(135)
        self.turtle.penup()
        self.turtle.forward(100)
        self.turtle.pendown()
        self.turtle.end_fill()

    def trapezjobb(self):
        self.turtle.fillcolor('red')
        self.turtle.begin_fill()
        self.turtle.left(180)
        self.turtle.forward(hosszuvonal)
        self.turtle.right(135)
        self.turtle.forward(rovidvonal)
        self.turtle.right(45)
        self.turtle.forward(kozepesvonal)
        self.turtle.right(45)
        self.turtle.forward(rovidvonal)
        self.turtle.right(135)
        self.turtle.penup()
        self.turtle.forward(100)
        self.turtle.pendown()
        self.turtle.end_fill()

    def emerald(self):
        self.turtle.fillcolor('red')
        self.turtle.begin_fill()
        self.turtle.left(225)
        self.turtle.forward(20)
        self.turtle.right(45)
        self.turtle.forward(70)
        self.turtle.right(45)
        self.turtle.forward(20)
        self.turtle.right(90)
        self.turtle.forward(20)
        self.turtle.right(45)
        self.turtle.forward(70)
        self.turtle.right(45)
        self.turtle.forward(20)
        self.turtle.right(45)
        self.turtle.end_fill()

    def lefttrapezbal90(self):
        self.turtle.left(90)
        self.trapezbal()

    def rightemrightup(self):
        self.turtle.right(90)
        self.emerald()
        self.turtle.right(90)
        self.turtle.penup()
    def upforhosszdown(self):
        self.turtle.penup()
        self.turtle.forward(hosszuvonal)
        self.turtle.pendown()
    def lefttrapez902xtrapezbal(self):
        self.lefttrapezbal90()
        self.trapezbal()
        self.lefttrapezbal90()

    def nulla(self, turtle):
        self.trapezbal()
        turtle.left(90)
        self.trapezbal()
        self.trapezbal()
        turtle.left(90)
        self.trapezbal()
        turtle.left(90)
        self.trapezbal()
        self.trapezbal()

    def egy(self, turtle):
        turtle.penup()
        turtle.forward(hosszuvonal)
        turtle.left(90)
        self.trapezbal()
        self.trapezbal()

    def ketto(self, turtle):
        self.trapezbal()
        turtle.left(90)
        turtle.penup()
        turtle.forward(hosszuvonal)
        turtle.pendown()
        turtle.right(90)
        self.emerald()
        turtle.left(180)
        self.trapezbal()
        turtle.left(90)
        self.trapezbal()
        turtle.left(90)
        turtle.penup()
        turtle.forward(hosszuvonal + 1)
        turtle.pendown()
        self.trapezbal()
        turtle.left(90)

    def harom(self, turtle):
        self.trapezbal()
        turtle.left(90)
        self.trapezbal()
        turtle.right(90)
        self.emerald()
        turtle.left(180)
        self.trapezbal()
        turtle.left(90)
        self.trapezbal()
        turtle.left(90)
        turtle.penup()
        turtle.forward(hosszuvonal + 1)
        turtle.forward(hosszuvonal + 1)
        turtle.left(90)
        turtle.pendown()

    def negy(self, turtle):
        turtle.penup()
        turtle.forward(hosszuvonal)
        turtle.left(90)
        turtle.pendown()
        self.trapezbal()
        turtle.right(90)
        self.emerald()
        turtle.left(180)
        self.trapezbal()
        turtle.left(90)
        turtle.penup()
        turtle.forward(hosszuvonal)
        turtle.left(90)
        turtle.pendown()
        self.trapezbal()
        turtle.penup()
        turtle.forward(hosszuvonal)
        turtle.left(90)
        turtle.pendown()

    def ot(self, turtle):
        self.trapezbal()
        turtle.left(90)
        self.trapezbal()
        turtle.right(90)
        self.emerald()
        turtle.left(180)
        turtle.penup()
        turtle.forward(hosszuvonal)
        turtle.left(90)
        turtle.pendown()
        self.trapezbal()
        turtle.left(90)
        self.trapezbal()
        turtle.penup()
        turtle.forward(hosszuvonal)
        turtle.left(90)
        turtle.pendown()

    def hat(self, turtle):
        self.trapezbal()
        turtle.left(90)
        self.trapezbal()
        turtle.right(90)
        self.emerald()
        turtle.penup()
        turtle.right(180)
        turtle.forward(hosszuvonal)
        turtle.left(90)
        turtle.pendown()
        self.trapezbal()
        turtle.left(90)
        for i in range(2):
            self.trapezbal()
        turtle.left(90)

    def het(self, turtle):
        turtle.penup()
        turtle.forward(hosszuvonal)
        turtle.left(90)
        for e in range(2):
            self.trapezbal()
        turtle.left(90)
        self.trapezbal()
        turtle.penup()
        turtle.left(90)
        turtle.forward(hosszuvonal)
        turtle.forward(hosszuvonal)
        turtle.left(90)
        turtle.penup()

    def nyolc(self, turtle):
        self.trapezbal()
        turtle.left(90)
        self.trapezbal()
        for w in range(2):
            self.trapezbal()
            turtle.left(90)
        for r in range(2):
            self.trapezbal()
        turtle.backward(hosszuvonal)
        turtle.right(90)
        self.emerald()
        turtle.backward(hosszuvonal)
        turtle.setheading(0)

    def kilenc(self, turtle):
        self.trapezbal()
        turtle.left(90)
        self.trapezbal()
        turtle.right(90)
        self.emerald()
        turtle.left(180)
        self.trapezbal()
        turtle.left(90)
        self.trapezbal()
        turtle.left(90)
        self.trapezbal()
        turtle.penup()
        turtle.forward(hosszuvonal + 1)
        turtle.left(90)
        turtle.pendown()

    def __init__(self):
        self.turtle = Turtle()
        self.turtle.speed(0)

