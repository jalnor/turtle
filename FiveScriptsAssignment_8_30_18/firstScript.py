import rhinoscriptsyntax as rs
import random

a = rs.AddPoint([5,5,20])
b = rs.AddPoint([20,20,5])
c = rs.AddLine(a,b)

print(a)
print(b)
print(c)

d = rs.AddPoint([10,25,10])
e = rs.AddPoint([30,30, 50])
f = rs.AddLine(d,e)

points = []
for i in range(20):
    x = random.random() * 10
    y = random.random() * 10
    z = random.random() * 10
    p = rs.AddPoint([x,y,z])
    points.append(p)
    print(points)
rs.AddCurve(points)