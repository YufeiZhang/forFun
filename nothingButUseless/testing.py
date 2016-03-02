#----------------------------------------------------------
# File path.py
#----------------------------------------------------------
import bpy, mathutils, math
from mathutils import Vector
from math import pi
 
def run(origin):
    # Create path data and object
    path = bpy.data.curves.new('MyPath', 'CURVE')
    pathOb = bpy.data.objects.new('Path', path)
    pathOb.location = origin
    bpy.context.scene.objects.link(pathOb)
 
    # Set path data
    path.dimensions = '3D'
    path.use_path = True
    path.use_path_follow = True
    path.path_duration = 100
 
    # Animate path
    path.eval_time = 0
    path.keyframe_insert(data_path="eval_time", frame=0)
    path.eval_time = 100
    path.keyframe_insert(data_path="eval_time", frame=250)    
 
    # Add a spline to path
    spline = path.splines.new('POLY')
    spline.use_cyclic_u = True
    spline.use_endpoint_u = False
 
    # Add points to spline
    pointTable = [(0,0,0,0), (1,0,3,0), 
        (1,2,2,0), (0,4,0,0), (0,0,0,0)]
    nPoints = len(pointTable)
    spline.points.add(nPoints-1)
    for n in range(nPoints):
        spline.points[n].co = pointTable[n]
 
    # Add a monkey
    #bpy.ops.mesh.primitive_monkey_add()
    #monkey = bpy.context.object
    
    # Add camera
    # Create object and camera
    bpy.ops.object.add(
        type='CAMERA',
        location=origin,
        rotation=(pi/2,0,pi))        
    rotCam = bpy.context.object
    rotCam.name = 'rot_cam'
    #cam = ob.data
    #cam.name = 'MyCam'
    
 
    # Add follow path constraint to monkey
    #cns = monkey.constraints.new('FOLLOW_PATH')
    cns = rotCam.constraints.new('FOLLOW_PATH')
    cns.target = pathOb
    cns.use_curve_follow = True
    cns.use_curve_radius = True
    cns.use_fixed_location = False
    cns.forward_axis = 'FORWARD_Z'
    cns.up_axis = 'UP_Y'
 
    return
 
if __name__ == "__main__":
    run((0,0,0))
    bpy.ops.screen.animation_play(reverse=False, sync=False)
