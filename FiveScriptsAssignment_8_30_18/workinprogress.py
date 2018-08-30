
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
obsR1 = []
obsR2 = []
obsR3 = []
colObs = []
p = 25
x = 255
z = 25.0
# Rotates planes and draws arcs with varying color
for i in range(0,200): # Loop 100 times
    for k in range(0, 10): # Loop once for each plane
        o = rs.RotatePlane(obs[k], (k + 100), [p,p,p]) # Suppose to increase the size of the event, but not working
        v = rs.RotatePlane(obs[k], (k - 1000), [p,p,p])
        w = rs.RotatePlane(obs[k], (k + 10000), [p,p,p])
        y = rs.RotatePlane(obs[k], (k - 400), [p,p,p])
        print((k-1+2)**2) # print value for testing
        obsR.append(o) # append newly created obj to list
        obsR1.append(v)
        obsR2.append(w)
        obsR3.append(y)
        for j in range(0, 4): # Loop 4 times to add arcs
#            if j % 2 == 1:
#                z = -45.0
            co = rs.AddArc(obsR[k],2,z) # Create object arc
            co1 = rs.AddArc(obsR1[k],2,z) # Create object arc
            co2 = rs.AddArc(obsR2[k],2,z) # Create object arc
            co3 = rs.AddArc(obsR3[k],2,z) # Create object arc
#            co4 = rs.AddPlanarMesh(co3)
            z += 5.0 # increase z each loop
            colObs.append(co)
            rs.ObjectColor(co1, [0,x,x])
            rs.ObjectColor(co2, [125,x,x])
            rs.ObjectColor(co3, [190,x,x])
            if j % 2 == 0:
                rs.ObjectColor(colObs[j], [0,x,x])
            else:
                rs.ObjectColor(colObs[j], [255,255,255])
            x -= 5
        x = 255
        p += 5
rs.ObjectColor(rs.AddPlanarMesh(co1), [0,100,x])
rs.ObjectColor(rs.AddPlanarMesh(co2), [125,150,x])
rs.ObjectColor(rs.AddPlanarMesh(co3), [190,200,x])

