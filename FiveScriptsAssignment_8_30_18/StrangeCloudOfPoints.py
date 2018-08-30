import rhinoscriptsyntax as rs
import random
# Creates points list
points = []
for i in range(100): #Creates a point cloud
    s = random.randint(100, 500) #
    x = random.random() * 10     #########################
    y = random.random() * 10     # Creates random points #
    z = random.random() * 10     #########################
    r = random.randint(0,255)    #########################
    g = random.randint(0,255)    # Creates random colors #
    b = random.randint(0,255)    #########################
    p = rs.AddPoint([x,y,z])     # Add point
    rs.PointScale(p,s)           # Scale point
    rs.ObjectColor(p, [r,g,b])   # Assign color
    points.append(p)             # Append point to list
    print(points)                # print the point
f = rs.AddCurve(points)          # Add curve to point cloud
rs.AddPlanarMesh(f)              # Supposed to add mesh