import turtle

class Structure:

    currentPos = 0 
    length = 0
    height = 0 
    width = 0
    prevDir = ""
    prevPosX = 0
    prevPosY = 0


    def __init__(self, posX, posY, mapPlace):
        self.posX = posX
        self.posY = posY
        self.mapPlace = mapPlace
        

    def drawRoof(self):
        tur = turtle.Turtle()
        tur.speed(0)       
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
        print(self.mapPlace)
        print(self.prevDir)
        if self.prevDir != "":
            print("Made it!")
            if self.mapPlace[0] == self.prevDir[0] and self.prevDir[1] == "w":
                if self.mapPlace[0] == "n":
                    self.drawWall(0)
                    self.tower()
                else:
                    self.drawWall(270)
                    self.tower()
            else:
                if self.prevDir[1] == "e":
                    self.drawWall(0)
                    self.tower()
                else:
                    self.drawWall(180)
                    self.tower()
        else:
            self.prevDir.replace(self.prevDir , self.mapPlace)
            
            print("Made it!")
            self.tower()
            

    def tower(self):

        tur = turtle.Turtle()
        tur.speed(0)
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
        self.prevPosX = self.posX
        self.prevPosY = self.posY
        self.height = 20 
    
    def drawWall(self, direction):
        
        tur = turtle.Turtle()
        tur.speed(0)
        tur.pu()
        tur.goto(self.posX, self.posY)
        tur.pd()
        tur.begin_fill()
        tur.color("#808080")
        if self.height > 2:
            hi = self.height -2
            while self.height > 2:
                if direction == 0:
                    dis = self.posX - self.prevPosX                    
                    turnLeft(dis, hi)
                    tur.end_fill()
                elif direction == 90:
                    dis = self.posY - self.prevPosY
                    #turnRight(dis, hi)
                elif direction == 180:                    
                    dis = self.prevPosX - self.posX
                    tur.right(180)
                    #turnRight(dis, hi)
                elif direction == 270:
                    dis = self.prevPosY - self.posY
                    turnLeft(dis, hi)
        

        def turnLeft(self, dis, hi):
            tur.fd(dis)
            tur.left(90)
            tur.fd(hi)
            tur.left(90)
            tur.fd(dis)
            tur.left(90)
            tur.fd(hi)
        
        #def turnRight(self, dis, hi):
            
        
            

