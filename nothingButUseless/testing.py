#----------------------------------------------------------
# File path.py
#----------------------------------------------------------
import bpy, mathutils, math
from mathutils import Vector
from math import pi

def addDistanceConstraint(ob, name, target):
    dis = ob.constraints.new('LIMIT_DISTANCE')
    dis.name = name
    dis.target = target
    dis.subtarget = 'Head'
    dis.distance = 5
    return

def addRotationConstraint(ob, name, target):
    rot = ob.constraints.new('LIMIT_ROTATION')
    rot.name = name
    #rot.target = target
    #rot.subtarget = 'Head'
    #rot.rotation=(0, 0, pi)
    #rot.min_x = 0
    #rot.max_x = 90
    #rot.use_limit_z = 0
    #rot.use_limit_z = 0
    return

def addTrackToConstraint(ob, name, target):
    cns = ob.constraints.new('TRACK_TO')
    cns.name = name
    cns.target = target
    cns.subtarget = 'Head'
    cns.track_axis = 'TRACK_NEGATIVE_Z'
    cns.up_axis = 'UP_Y'
    cns.owner_space = 'WORLD'
    cns.target_space = 'WORLD'
    return
 
def run(origin):
    # delete the existing camera and empty
    scn = bpy.context.scene
    for ob in scn.objects:
        if ob.type == 'CAMERA':
            bpy.data.objects[ob.name].select = True
            bpy.ops.object.delete()
            
    # crate a camera
    bpy.ops.object.add(type='CAMERA')        
    rot_cam = bpy.context.object
    rot_cam.name = 'rot_cam'
    
    # get the skel_obj
    skel_obj = bpy.data.objects['131_09_60fps']
    
    # add a distance constraint
    addDistanceConstraint(rot_cam, 'FiveUnits', skel_obj)
    
    # add a rotation constraint
    addRotationConstraint(rot_cam, 'LimitRotation', skel_obj)
    
    # add a track constraint    
    addTrackToConstraint(rot_cam, 'Tracking', skel_obj)
    
    return
 
if __name__ == "__main__":
    run((0,0,0))
    bpy.ops.screen.animation_play(reverse=False, sync=False)
