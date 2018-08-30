import rhinoscriptsyntax as rs
from math import*

points = []
qpoints = []
a = 49
for i in range(0,100):
    if i < 50:
        p = rs.AddPoint([i - 49,20*sin(i),i])
        q = rs.AddPoint([20*sin(i),i - 49,i])
    elif i < 100 and i > 49:
        p = rs.AddPoint([i - 49, 20*sin(i),a])
        q = rs.AddPoint([20*sin(i),i - 49,a])
        a -= 1
    points.append(p)
    qpoints.append(q)
#    print(points)
rs.AddCurve(points)
rs.AddCurve(qpoints)