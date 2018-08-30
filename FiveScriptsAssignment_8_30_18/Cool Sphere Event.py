import rhinoscriptsyntax as rs
# Creates cool sphere in center of Event
a = rs.AddSphere([20,20,20], 5)
rs.ObjectColor(a,[255,0,0]) 
# Creates planes that expand toward sphere
plane = rs.WorldZXPlane()
plane2 = rs.WorldZXPlane()
plane3 = rs.WorldZXPlane()
plane4 = rs.WorldZXPlane()
plane5 = rs.WorldZXPlane()

# Rotates planes and draws arcs with varying color
for i in range(0,200):
    plane = rs.RotatePlane(plane, 2, [25,25,25])
    plane2 = rs.RotatePlane(plane2, 5, [25,25,25])
    plane3 = rs.RotatePlane(plane3, 11, [25,25,25])
    plane4 = rs.RotatePlane(plane4, 23, [25,25,25])
    plane5 = rs.RotatePlane(plane5, 47, [25,25,25])
    a1 = rs.AddArc( plane, 2, 45.0 )
    a2 = rs.AddArc( plane, 2, -45.0 )
    a3 = rs.AddArc(plane2, 5, 45.0)
    a4 =rs.AddArc(plane2, 5, -45.0)
    a5 = rs.AddArc(plane3, 11, 45.0)
    a6 = rs.AddArc(plane3, 11, -45.0)
    a7 = rs.AddArc(plane4, 23, 45.0)
    a8 = rs.AddArc(plane4, 23, -45.0)
    a9 = rs.AddArc(plane5, 47, 45.0)
    a10 = rs.AddArc(plane5, 47, -45.0)
    rs.ObjectColor(a1, [0,255,255])
#    rs.ObjectColor(a2, [0,255,255])
    rs.ObjectColor(a3, [0,230,230])
#    rs.ObjectColor(a4, [0,230,230])
    rs.ObjectColor(a5, [0,204,204])
#    rs.ObjectColor(a6, [0,204,204])
    rs.ObjectColor(a7, [0,179,179])
#    rs.ObjectColor(a8, [0,102,102])
    rs.ObjectColor(a9, [0,153,153])






