import rhinoscriptsyntax as rs
from math import*
# Creates cool sphere in center of Event
a = rs.AddSphere([20,20,20], 5)
rs.ObjectColor(a,[255,0,0]) 
obs = []
# Creates planes that expand toward sphere
for i in range(0, 10):
    plane = rs.WorldZXPlane()
    obs.append(plane)
obsR = []
colObs = []
p = 25
x = 255
# Rotates planes and draws arcs with varying color
for i in range(0,50):
    for k in range(0, 10):
        o = rs.RotatePlane(obs[k], (k-1+2)**2, [p,p,p])
        print(o)
        obsR.append(o)
#        for j in range(0, 4):
        rs.AddArc(obsR[k],2,45.0)
#            print(co) co = 
#            colObs.append(co)
#            if j % 2 == 0:
#                rs.ObjectColor(colObs[j], [0,x,x])
#            else:
#                rs.ObjectColor(colObs[j], [255,255,255])

