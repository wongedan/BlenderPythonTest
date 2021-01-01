import bpy

#render tempelate based on https://youtu.be/ydAmFR2wN9w

for frame in range (0, 120):
    bpy.context.scene.frame_set(frame)
    bpy.context.scene.render.filepath = 'C:\\Users\\YourName\\Documents\\Blender\\render\\%04d.png' % frame
    bpy.ops.render.render(write_stSill=True)
