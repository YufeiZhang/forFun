#----------------------------------------------------------
# File path.py
#----------------------------------------------------------
import bpy, mathutils, math
from mathutils import Vector
from math import pi, sin, cos # sin(pi/2) = 1.0


def addCopyLocationConstraint(ob, name, target):
    cpyloc = ob.constraints.new('COPY_LOCATION')
    cpyloc.name = name
    cpyloc.use_x = False
    cpyloc.use_y = False
    cpyloc.target = target
    cpyloc.subtarget = 'Head'
    

def addDistanceConstraint(ob, name, target):
    dis = ob.constraints.new('LIMIT_DISTANCE')
    dis.name = name
    dis.target = target
    dis.subtarget = 'Head'
    dis.distance = 5
    dis.limit_mode = "LIMITDIST_ONSURFACE"
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


def rotateAsTime(ob, target, index):
    head = target.pose.bones['Head']
    bpy.data.objects[ob.name].select = True
    bpy.context.object.location[0] = head.location.x + 10 * cos((index%360)/180*pi)
    bpy.context.object.location[1] = head.location.y + 10 * sin((index%360)/180*pi)
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
    
    # add a copy location constarin
    addCopyLocationConstraint(rot_cam, 'location', skel_obj)
    
    # add a distance constraint
    addDistanceConstraint(rot_cam, 'distance', skel_obj)
                
    # add a track constraint    
    addTrackToConstraint(rot_cam, 'tracking', skel_obj)
    
    #rotateAsTime(rot_cam, skel_obj, scn.frame_current)
    
    # I want to change the degree every frame
    #for i in range(1147):      
    #    rotateAsTime(rot_cam, skel_obj, i)
        
    return
 
 
if __name__ == "__main__":
    run((0,0,0))
    bpy.ops.screen.animation_play(reverse=False, sync=False)
