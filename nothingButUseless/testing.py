#----------------------------------------------------------
# File path.py
#----------------------------------------------------------
import bpy, mathutils, math
from mathutils import Vector
from math import pi

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
        if ob.type == 'EMPTY' or  ob.type == 'CAMERA':
            scn.objects.unlink(ob)
            
    # crate a camera
    bpy.ops.object.add(type='CAMERA')        
    rot_cam = bpy.context.object
    rot_cam.name = 'rot_cam'
    
    # get the skel_obj
    skel_obj = bpy.data.objects['131_09_60fps']
    
    # add a track constraint    
    addTrackToConstraint(rot_cam, 'Tracking', skel_obj)
    
    return
 
if __name__ == "__main__":
    run((0,0,0))
    bpy.ops.screen.animation_play(reverse=False, sync=False)
