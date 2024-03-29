import os
import bpy
import bpy.utils.previews

mkb_icon_collections = {}
mkb_icons_loaded = False

def load_icons():
    global mkb_icon_collections
    global mkb_icons_loaded

    if mkb_icons_loaded: return mkb_icon_collections["main"]

    mkb_icons = bpy.utils.previews.new()

    icons_dir = os.path.join(os.path.dirname(__file__))

    #--------------------------------------------

    mkb_icons.load("icon_snap_active", os.path.join(icons_dir, "snap_active.png"), 'IMAGE')
    mkb_icons.load("icon_snap_closest", os.path.join(icons_dir, "snap_closest.png"), 'IMAGE')
    mkb_icons.load("icon_snap_cursor", os.path.join(icons_dir, "snap_cursor.png"), 'IMAGE')
    mkb_icons.load("icon_snap_grid", os.path.join(icons_dir, "snap_grid.png"), 'IMAGE')
    mkb_icons.load("icon_snap_retopo", os.path.join(icons_dir, "snap_retopo.png"), 'IMAGE')
    mkb_icons.load("icon_snap_place", os.path.join(icons_dir, "snap_place.png"), 'IMAGE')
    mkb_icons.load("icon_snap_set", os.path.join(icons_dir, "snap_set.png"), 'IMAGE')
    mkb_icons.load("icon_snap_move", os.path.join(icons_dir, "snap_move.png"), 'IMAGE')
    mkb_icons.load("icon_snap_rotate", os.path.join(icons_dir, "snap_rotate.png"), 'IMAGE')
    mkb_icons.load("icon_snap_scale", os.path.join(icons_dir, "snap_scale.png"), 'IMAGE')
    mkb_icons.load("icon_snap_measure", os.path.join(icons_dir, "snap_measure.png"), 'IMAGE')

    mkb_icons.load("icon_snap_annotate", os.path.join(icons_dir, "annotate.png"), 'IMAGE')
    mkb_icons.load("icon_snap_annotate_line", os.path.join(icons_dir, "annotate_line.png"), 'IMAGE')
    mkb_icons.load("icon_snap_annotate_polygon", os.path.join(icons_dir, "annotate_polygon.png"), 'IMAGE')
    mkb_icons.load("icon_snap_annotate_eraser", os.path.join(icons_dir, "annotate_eraser.png"), 'IMAGE')

    mkb_icons.load("icon_snap_center", os.path.join(icons_dir, "snap_center.png"), 'IMAGE')
    mkb_icons.load("icon_snap_perpendic", os.path.join(icons_dir, "snap_perpendic.png"), 'IMAGE')
    mkb_icons.load("icon_snap_pcursor", os.path.join(icons_dir, "snap_pcursor.png"), 'IMAGE')

    mkb_icons.load("icon_snap_custom", os.path.join(icons_dir, "snap_custom.png"), 'IMAGE')

    mkb_icons.load("icon_align_x", os.path.join(icons_dir, "align_x.png"), 'IMAGE')    
    mkb_icons.load("icon_align_y", os.path.join(icons_dir, "align_y.png"), 'IMAGE')    
    mkb_icons.load("icon_align_z", os.path.join(icons_dir, "align_z.png"), 'IMAGE') 
    mkb_icons.load("icon_align_xyz", os.path.join(icons_dir, "align_xyz.png"), 'IMAGE') 

    mkb_icons.load("icon_align_xy", os.path.join(icons_dir, "align_xy.png"), 'IMAGE')    
    mkb_icons.load("icon_align_zx", os.path.join(icons_dir, "align_zx.png"), 'IMAGE')    
    mkb_icons.load("icon_align_zy", os.path.join(icons_dir, "align_zy.png"), 'IMAGE')   

    mkb_icons.load("icon_rota_x", os.path.join(icons_dir, "rota_x.png"), 'IMAGE') 
    mkb_icons.load("icon_rota_y", os.path.join(icons_dir, "rota_y.png"), 'IMAGE') 
    mkb_icons.load("icon_rota_z", os.path.join(icons_dir, "rota_z.png"), 'IMAGE') 
    mkb_icons.load("icon_rota_xyz", os.path.join(icons_dir, "rota_xyz.png"), 'IMAGE') 

    mkb_icons.load("icon_scale_x", os.path.join(icons_dir, "scale_x.png"), 'IMAGE')    
    mkb_icons.load("icon_scale_y", os.path.join(icons_dir, "scale_y.png"), 'IMAGE')    
    mkb_icons.load("icon_scale_z", os.path.join(icons_dir, "scale_z.png"), 'IMAGE')    
    mkb_icons.load("icon_scale_xyz", os.path.join(icons_dir, "scale_xyz.png"), 'IMAGE')    

    mkb_icons.load("icon_world_x", os.path.join(icons_dir, "world_x.png"), 'IMAGE') 
    mkb_icons.load("icon_world_y", os.path.join(icons_dir, "world_y.png"), 'IMAGE') 
    mkb_icons.load("icon_world_z", os.path.join(icons_dir, "world_z.png"), 'IMAGE') 
    mkb_icons.load("icon_world_xyz", os.path.join(icons_dir, "world_xyz.png"), 'IMAGE') 
 
    mkb_icons.load("icon_cursor_loca_x", os.path.join(icons_dir, "cursor_loca_x.png"), 'IMAGE') 
    mkb_icons.load("icon_cursor_loca_y", os.path.join(icons_dir, "cursor_loca_y.png"), 'IMAGE') 
    mkb_icons.load("icon_cursor_loca_z", os.path.join(icons_dir, "cursor_loca_z.png"), 'IMAGE') 
    mkb_icons.load("icon_cursor_loca_xyz", os.path.join(icons_dir, "cursor_loca_xyz.png"), 'IMAGE') 

    mkb_icons.load("icon_cursor_rota_x", os.path.join(icons_dir, "cursor_rota_x.png"), 'IMAGE') 
    mkb_icons.load("icon_cursor_rota_y", os.path.join(icons_dir, "cursor_rota_y.png"), 'IMAGE') 
    mkb_icons.load("icon_cursor_rota_z", os.path.join(icons_dir, "cursor_rota_z.png"), 'IMAGE') 
    mkb_icons.load("icon_cursor_rota_xyz", os.path.join(icons_dir, "cursor_rota_xyz.png"), 'IMAGE') 

    mkb_icons.load("icon_event_x", os.path.join(icons_dir, "event_x.png"), 'IMAGE')    
    mkb_icons.load("icon_event_y", os.path.join(icons_dir, "event_y.png"), 'IMAGE')    
    mkb_icons.load("icon_event_z", os.path.join(icons_dir, "event_z.png"), 'IMAGE')    
    mkb_icons.load("icon_event_xy", os.path.join(icons_dir, "event_xy.png"), 'IMAGE')    
    mkb_icons.load("icon_event_zx", os.path.join(icons_dir, "event_zx.png"), 'IMAGE')    
    mkb_icons.load("icon_event_zy", os.path.join(icons_dir, "event_zy.png"), 'IMAGE')  

    mkb_icons.load("icon_align_n", os.path.join(icons_dir, "align_n.png"), 'IMAGE')  

    mkb_icons.load("icon_align_distribute", os.path.join(icons_dir, "align_distribute.png"), 'IMAGE')   
    mkb_icons.load("icon_align_straigten", os.path.join(icons_dir, "align_straigten.png"), 'IMAGE')   
    mkb_icons.load("icon_align_both", os.path.join(icons_dir, "align_both.png"), 'IMAGE')   

    mkb_icons.load("icon_align_laplacian", os.path.join(icons_dir, "align_laplacian.png"), 'IMAGE')   
    mkb_icons.load("icon_align_looptools", os.path.join(icons_dir, "align_looptools.png"), 'IMAGE')   
    mkb_icons.load("icon_align_vertices", os.path.join(icons_dir, "align_vertices.png"), 'IMAGE')   

    mkb_icons.load("icon_align_space", os.path.join(icons_dir, "align_space.png"), 'IMAGE')   
    mkb_icons.load("icon_align_circle", os.path.join(icons_dir, "align_circle.png"), 'IMAGE')   
    mkb_icons.load("icon_align_curve", os.path.join(icons_dir, "align_curve.png"), 'IMAGE')   
    mkb_icons.load("icon_align_flatten", os.path.join(icons_dir, "align_flatten.png"), 'IMAGE')   
    mkb_icons.load("icon_align_smooth", os.path.join(icons_dir, "align_smooth.png"), 'IMAGE')   

    #--------------------------------------------

    mkb_icon_collections["main"] = mkb_icons
    mkb_icons_loaded = True

    return mkb_icon_collections["main"]

def clear_icons():
    global mkb_icons_loaded
    for icon in mkb_icon_collections.values():
        bpy.utils.previews.remove(icon)
    mkb_icon_collections.clear()
    mkb_icons_loaded = False 