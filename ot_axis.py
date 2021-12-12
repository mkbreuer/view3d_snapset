# LOAD MODUL #    
import bpy
from bpy import *
from bpy.props import *

class VIEW3D_OT_align_object_to_axis(bpy.types.Operator):
    """align object to an axis"""
    bl_idname = "tpc_ot.align_object_to_axis"
    bl_label = "Align to Axis"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return True

    use_align_axis_x : BoolProperty(name="X",  description=" ", default=True, options={'SKIP_SAVE'})    
    use_align_axis_y : BoolProperty(name="Y",  description=" ", default=False, options={'SKIP_SAVE'})    
    use_align_axis_z : BoolProperty(name="Z",  description=" ", default=False, options={'SKIP_SAVE'})   

    def draw(self, context):
        layout = self.layout   

        box = layout.box().column(align=True) 
        box.separator() 

        row = box.row(align=True)  
        row.label(text='Axis:') 
        row.prop(self, 'use_align_axis_x')  
        row.prop(self, 'use_align_axis_y')  
        row.prop(self, 'use_align_axis_z')  

        box.separator() 


    def execute(self, context):   

        current_mode = bpy.context.object.mode 
        bpy.ops.object.mode_set(mode = 'OBJECT')

        view_layer = bpy.context.view_layer
        selected = bpy.context.selected_objects
        for obj in selected:
            view_layer.objects.active = obj

            axis_x = ''                    
            axis_y = ''                    
            axis_z = '' 

            if self.use_align_axis_x == True and self.use_align_axis_y == False and self.use_align_axis_z == False:   
                obj.location[1] = 0
                axis_x = 'X Align'                    

            if self.use_align_axis_x == False and self.use_align_axis_y == True and self.use_align_axis_z == False:   
                obj.location[0] = 0                  
                axis_y = 'Y Align'                    
             
            if self.use_align_axis_x == False and self.use_align_axis_y == False and self.use_align_axis_z == True:   
                obj.location[2] = 0                 
                axis_z = 'Z Align' 

            if self.use_align_axis_x == True and self.use_align_axis_y == True and self.use_align_axis_z == False:   
                obj.location[1] = 0
                obj.location[0] = 0
                axis_x = 'X'                    
                axis_y = 'Y Align'                    

            if self.use_align_axis_x == True and self.use_align_axis_y == False and self.use_align_axis_z == True:   
                obj.location[1] = 0
                obj.location[2] = 0     
                axis_x = 'X'                                      
                axis_z = 'Z Align' 

            if self.use_align_axis_x == False and self.use_align_axis_y == True and self.use_align_axis_z == True:   
                obj.location[0] = 0
                obj.location[2] = 0                  
                axis_y = 'Y'                    
                axis_z = 'Z Align'  

            if self.use_align_axis_x == True and self.use_align_axis_y == True and self.use_align_axis_z == True:   
                obj.location[0] = 0
                obj.location[1] = 0
                obj.location[2] = 0
                axis_x = 'X'                    
                axis_y = 'Y'                    
                axis_z = 'Z Align'                                     

        bpy.ops.object.mode_set(mode=current_mode) 

        message = ("World Axis: " + axis_x + axis_y + axis_z)
        self.report({'INFO'}, message)
        return {'FINISHED'}
    
    
