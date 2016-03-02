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
    cns.track_axis = 'TRACK_NEGATIVE_Z'
    cns.up_axis = 'UP_Y'
    cns.owner_space = 'WORLD'
    cns.target_space = 'WORLD'
    return
 
def run(origin):
    scn = bpy.context.scene
    for ob in scn.objects:
        if ob.type == 'EMPTY':
            scn.objects.unlink(ob)
        elif ob.type == 'ARMATURE':
            #headPosition = (-1.5,6.9,3.5)
            head = ob
            poss = head.location
    
    bpy.ops.object.add(type='EMPTY',location=Vector(poss))
    target = bpy.context.object 
    target.name = 'Target'
    
    addTrackToConstraint(target, 'Tracking', target)
    

 
    return
 
if __name__ == "__main__":
    run((0,0,0))
    bpy.ops.screen.animation_play(reverse=False, sync=False)
