
import rhinoscriptsyntax as rs
from math import*
# Creates cool sphere in center of Event
a = rs.AddSphere([0,0,0], 5)
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
z = 45.0
# Rotates planes and draws arcs with varying color
for i in range(0,100): # Loop 100 times
    for k in range(0, 10): # Loop once for each plane
        o = rs.RotatePlane(obs[k], (k-1+2)**2, [p,p,p]) # Suppose to increase the size of the event, but not working
        print((k-1+2)**2) # print value for testing
        obsR.append(o) # append newly created obj to list
        for j in range(0, 2): # Loop 4 times to add arcs
            co = rs.AddArc(obsR[k],2,z) # Create object arc
            z += 45.0 # increase z each loop
            colObs.append(co)
            if j % 2 == 0:
                rs.ObjectColor(colObs[j], [0,x,x])
#                z = -45.0
            else:
                rs.ObjectColor(colObs[j], [255,255,255])
            x -= 5
#        z = 45.0
        x = 255
        p += 5

