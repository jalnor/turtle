import turtle

class Turret:

    currentPos = 0 
    length = 0
    height = 0 
    width = 0


    def __init__(self, posX, posY):
        self.posX = posX
        self.posY = posY
        

    def drawRoof(self):
        tur = turtle.Turtle()       
        roofColor = "#b30000"
        tur.resizemode("user")
        self.height = 6
        self.width = .5
        self.length = 1
        tur.pu()
        tur.goto(self.posX, self.posY)
        while self.height > 0:
            tur.pd()
            tur.shape("circle")
            tur.shapesize(self.width, self.length)
            tur.fillcolor(roofColor)
            tur.stamp()
            self.length += 1
            #width += 1
            self.height -= 1
            self.posX -= .5
            self.posY -= 5
            tur.pu()
            tur.goto(self.posX, self.posY)        
        self.currentPos = tur.pos()
        #turtle.done()

    def drawTower(self):
        print(self.currentPos)
        tur = turtle.Turtle()
        self.height = 20
        tur.pu()
        tur.goto(self.posX - 2, self.posY)
        while self.height > 0:
            tur.pd()
            wallColor = "#808080"
            tur.shape("circle")
            tur.shapesize(self.width, (self.length-2))
            tur.fillcolor(wallColor)
            tur.stamp()
            self.height -= 1
            self.posY -= 5
            tur.pu()
            tur.goto(self.posX, self.posY)


