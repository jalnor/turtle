import rhinoscriptsyntax as rs
from math import*
# Creates lists
points = []
qpoints = []
# An integer to control z direction in loop
a = 49
for i in range(0,100):
    if i < 50: # Controls ascending points
        p = rs.AddPoint([i - 49,20*sin(i),i])
        q = rs.AddPoint([20*sin(i),i - 49,i])
    elif i < 100 and i > 49: # controls descending points
        p = rs.AddPoint([i - 49, 20*sin(i),a])
        q = rs.AddPoint([20*sin(i),i - 49,a])
        a -= 1
    points.append(p) # Appends points ot lists
    qpoints.append(q)
#Adds curve to poihnts
rs.AddCurve(points) 
rs.AddCurve(qpoints)