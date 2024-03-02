import bpy
from bpy.types import Operator


class XX_OT_test(Operator):
    """Lorem Ipsum.

    Shift              •  Lorem Ipsum.
    Ctrl               •  Lorem Ipsum.
    Alt                •  Lorem Ipsum"""

    bl_label = "Test"
    bl_idname = "xx.test"
    bl_options = {"REGISTER"}

    def invoke(self, context, event):
        return {"FINISHED"}

    def execute(self, context):
        return {"FINISHED"}

    def modal(self, context, event):
        return {"FINISHED"}


classes = (XX_OT_test,)


register, unregister = bpy.utils.register_classes_factory(classes)
