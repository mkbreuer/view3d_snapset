# SnapSet - Blender Addon

Batch presets for snapping task
- as durable buttons or as one time modal buttons 
- all buttons are full customizable
- different layouts for context menus and pie menu with custom shortcut key creation
- appending to different locations: editor header, special menu, snapping setting panel, etc.
- with auxiliary addons for the pie menu: align objects (objectmode), looptools and align mesh (editmode)

Release Download https://github.com/mkbreuer/view3d_snapset/releases
                               
Durable Tools 
- After execute the snap settings toggle to the needed durable preferences.                       
                      
- Grid        > snap pivot with absolute grid alignment               
- Place       > snap pivot to surface of other objects  
- Cursor      > set 3d cursor to active or selected  
- Closest     > snap closest point onto target  
- Active      > snap active pivot onto target  
- Retopo      > snap selected onto target in editmode  
- MidPoint    > snap selected onto target 
- Perpendic   > snap selected onto target 
- PlaceCursor > place 3D cursor onto a surface target  

 (*) Modal Tools  
- After execute the snap settings toggle to the needed modal preferences.  
- It finish the modal directly after an click and the settings switch back to the previous durable one.                          

- Grid*           > snap pivot with absolute grid alignment til release             
- Place*          > object mode: snap pivot to surface of other objects til release  
- Retopo*         > edit mode: snap selected onto target til release 
- MidPoint*       > snap selected onto target til release 
- Perpendic*      > snap selected onto target til release 
- PlaceCursor*    > snap 3d cursor onto surface target til release 
- Custom*         > customizable extra button


## Panel layout
![panel layout durable: ](./images/panel_layout.png)
![panel layout modals: ](./images/panel_layout2.png)

## Append to header snap settings
![header settings layout: ](./images/append_functions_to_snap_settings.png)
![header settings layout: ](./images/append_functions_preferences.png)
                                       
## Append to context menu, key [W]
![special context menu layout: ](./images/menu_context_special.png)    

## Custom context menu, key [customizable]
![custom context menu layout: ](./images/menu_context.png)  

## Custom pie menu, key [customizable]
![custom pie menu layout: ](./images/pie_menu_layouts.png) 

## Auxiliary addons for the pie menu
![addons for pie menu: ](./images/pie_menu_auxiliary_addons.png)  

## Align Mesh Addon
- comes not with blender by default and must be installed separatly!
- release download: https://github.com/mkbreuer/view3d_alignmesh/releases