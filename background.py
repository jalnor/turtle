import turtle

class Background:

    def __init__(self, length, width, color, setX, setY):
        self.length = length
        self.width = width
        self.color = color
        self.setX = setX
        self.setY = setY

    def drawSquare(self):
        sq = turtle.Turtle()
        sq.speed(0)
        sq.pu()
        sq.goto(self.setX, self.setY)
        sq.begin_fill()
        sq.color(self.color)
        sq.fd(self.length)
        sq.rt(90)
        sq.fd(self.width)
        sq.rt(90)
        sq.fd(self.length)
        sq.rt(90)
        sq.fd(self.width)
        sq.end_fill()





        