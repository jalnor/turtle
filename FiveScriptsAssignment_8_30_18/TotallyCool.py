import rhinoscriptsyntax as rs
import random
# Creates cool sphere in center of Event
a = rs.AddSphere([0,0,0], 5)
rs.ObjectColor(a,[255,0,0]) 
# Creates planes that expand toward sphere
plane = rs.WorldZXPlane()
plane2 = rs.WorldZXPlane()
plane3 = rs.WorldZXPlane()
plane4 = rs.WorldZXPlane()
plane5 = rs.WorldZXPlane()

# Rotates planes and draws arcs with varying color
for i in range(0,200):
    r = random.randint(0,255)    #########################
    g = random.randint(0,255)    # Creates random colors #
    b = random.randint(0,255)    #########################
    plane = rs.RotatePlane(plane, 2, [25,25,25])
    plane2 = rs.RotatePlane(plane2, 5, [25,25,25])
    plane3 = rs.RotatePlane(plane3, 11, [25,25,25])
    plane4 = rs.RotatePlane(plane4, 23, [25,25,25])
    plane5 = rs.RotatePlane(plane5, 47, [25,25,25])
    a1 = rs.AddArc( plane, 2, 45.0 )
    a2 = rs.AddArc( plane, 2, -45.0 )
    a3 = rs.AddArc(plane2, 5, 45.0)
    a4 = rs.AddArc(plane2, 5, -45.0)
    a5 = rs.AddArc(plane3, 11, 45.0)
    a6 = rs.AddArc(plane3, 11, -45.0)
    a7 = rs.AddArc(plane4, 23, 45.0)
    a8 = rs.AddArc(plane4, 23, -45.0)
    a9 = rs.AddArc(plane5, 47, 45.0)
    a10 = rs.AddArc(plane5, 47, -45.0)
    if i % 2 == 0:        
        rs.ObjectColor(a1, [r,g,b])
        rs.ObjectColor(a2, [r,g,b])
        rs.ObjectColor(a3, [r,g,b])
        rs.ObjectColor(a4, [r,g,b])
        rs.ObjectColor(a5, [r,g,b])
        rs.ObjectColor(a6, [r,g,b])
        rs.ObjectColor(a7, [r,g,b])
        rs.ObjectColor(a8, [r,g,b])
        rs.ObjectColor(a9, [r,g,b])
    else:        
        rs.ObjectColor(a1, [r,g,b])
        rs.ObjectColor(a2, [r,g,b])
        rs.ObjectColor(a3, [r,g,b])
        rs.ObjectColor(a4, [r,g,b])
        rs.ObjectColor(a5, [r,g,b])
        rs.ObjectColor(a6, [r,g,b])
        rs.ObjectColor(a7, [r,g,b])
        rs.ObjectColor(a8, [r,g,b])
        rs.ObjectColor(a9, [r,g,b])






