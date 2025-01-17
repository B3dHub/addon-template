import bpy
from bpy.props import *
from bpy.types import AddonPreferences, PropertyGroup


class XX_AP_preference(AddonPreferences):
    bl_idname = __package__.partition(".")[0]

    def draw(self, context):
        layout = self.layout
        layout.use_property_decorate = False


classes = (XX_AP_preference,)


register, unregister = bpy.utils.register_classes_factory(classes)
