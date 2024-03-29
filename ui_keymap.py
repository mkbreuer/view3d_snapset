# LOAD MODUL #    
import bpy
from bpy import *
from .ui_utils import get_addon_prefs

# ADD 3D VIEW MENU #  
from view3d_snapset.ui_menu         import (VIEW3D_MT_snapset_menu)
from view3d_snapset.ui_menu_pie_1   import (VIEW3D_MT_snapset_menu_pie_1)
from view3d_snapset.ui_menu_pie_2   import (VIEW3D_MT_snapset_menu_pie_2)

# KEY REGISTRY # 
addon_keymaps = []
def update_snapset_menu(self, context):
    
    # commented: registered as sub-classes
    # try:
    #     bpy.utils.unregister_class(VIEW3D_MT_snapset_menu)
    #     bpy.utils.unregister_class(VIEW3D_MT_snapset_menu_pie_1)        
    #     bpy.utils.unregister_class(VIEW3D_MT_snapset_menu_pie_2)

    #     # Keymapping
    #     # remove keymaps when add-on is deactivated
    #     for km, kmi in addon_keymaps:
    #         km.keymap_items.remove(kmi)
    #     # clear the list
    #     addon_keymaps.clear()
            
    # except:
    #     pass
    
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:   

        addon_prefs = get_addon_prefs()
        if addon_prefs.toggle_keymap_menus == True:
            
           
            if addon_prefs.toggle_keymap_type == 'menu':

               #bpy.utils.register_class(VIEW3D_MT_snapset_menu)

                km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
                #kmi = km.keymap_items.new('wm.call_menu', 'W', 'PRESS', shift=True) #, ctrl=True, alt=True)

                kmi = km.keymap_items.new('wm.call_menu', addon_prefs.hotkey_menu, 'PRESS', ctrl=addon_prefs.hotkey_menu_ctrl,  alt=addon_prefs.hotkey_menu_alt, shift=addon_prefs.hotkey_menu_shift)
                
                kmi.properties.name = "VIEW3D_MT_snapset_menu"                              
                addon_keymaps.append((km,kmi))

          
            if addon_prefs.toggle_keymap_type == 'pie':

                #if addon_prefs.toggle_pie_layout == False: 
                    #bpy.utils.register_class(VIEW3D_MT_snapset_menu_pie_1)
               # else:
                    #bpy.utils.register_class(VIEW3D_MT_snapset_menu_pie_2)

                km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
                #kmi = km.keymap_items.new('wm.call_menu_pie', 'W', 'PRESS', shift=True) #, ctrl=True, alt=True)                
          
                kmi = km.keymap_items.new('wm.call_menu_pie', addon_prefs.hotkey_menu, 'PRESS', ctrl=addon_prefs.hotkey_menu_ctrl,  alt=addon_prefs.hotkey_menu_alt, shift=addon_prefs.hotkey_menu_shift)
                
                if addon_prefs.toggle_pie_layout == False:               
                    kmi.properties.name = "VIEW3D_MT_snapset_menu_pie_1"   
                else:    
                    kmi.properties.name = "VIEW3D_MT_snapset_menu_pie_2"   
                addon_keymaps.append((km,kmi))            

   
        if addon_prefs.toggle_keymap_menus == False:
            
            # Keymapping
            # remove keymaps when add-on is deactivated
            for km, kmi in addon_keymaps:
                km.keymap_items.remove(kmi)
            # clear the list
            addon_keymaps.clear()

