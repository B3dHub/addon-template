import bpy
from bpy.types import Menu


class XX_MT_preset_menu(Menu):
    '''Presets'''
    bl_label = 'Presets'
    preset_subdir = 'Preset Location'
    preset_operator = 'script.execute_preset'
    preset_operator_defaults = {'menu_idname' : 'XX_MT_preset_menu'}
    draw = Menu.draw_preset


classes = (
    XX_MT_preset_menu,
)


register, unregister = bpy.utils.register_classes_factory(classes)