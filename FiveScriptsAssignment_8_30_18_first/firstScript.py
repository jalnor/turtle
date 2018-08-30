import rhinoscriptsyntax as rs
import random
# Creates points and a line
a = rs.AddPoint([5,5,20])
b = rs.AddPoint([20,20,5])
c = rs.AddLine(a,b)
# Prints the point
print(a)
print(b)
print(c)
# Creates points and a line
d = rs.AddPoint([10,25,10])
e = rs.AddPoint([30,30, 50])
f = rs.AddLine(d,e)
# Points list
points = []
for i in range(20): # Creates a point cloud
    x = random.random() * 10
    y = random.random() * 10
    z = random.random() * 10
    p = rs.AddPoint([x,y,z])
    points.append(p) # Add point to list
    print(points)
rs.AddCurve(points) # Add curve to points list