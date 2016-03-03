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
    camera = bpy.data.objects[ob.name]
    camera.select = True
    camera.lock_location[2] = True   
    head = target.pose.bones['Head']
    camera.rotation_mode = 'XYZ'
    
    if index % 360 == 0:
        camera.location[0] = head.location[0] + 10 * cos(0)
        camera.location[1] = head.location[1] + 10 * sin(0)
        camera.keyframe_insert('location')
    elif index % 360 == 90:
        camera.location[0] = head.location[0] + 10 * cos(pi/2)
        camera.location[1] = head.location[1] + 10 * sin(pi/2)
        camera.keyframe_insert('location')
    elif index % 360 == 180:
        camera.location[0] = head.location[0] + 10 * cos(pi)
        camera.location[1] = head.location[1] + 10 * sin(pi)
        camera.keyframe_insert('location')
    elif index % 360 == 270:
        camera.location[0] = head.location[0] + 10 * cos(3/2*pi)
        camera.location[1] = head.location[1] + 10 * sin(3/2*pi)
        camera.keyframe_insert('location')

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
    
    # I want to change the degree every frame
    rotateAsTime(rot_cam, skel_obj, scn.frame_current)
        
    return
 
 
if __name__ == "__main__":
    run((0,0,0))
    bpy.ops.screen.animation_play(reverse=False, sync=False)
