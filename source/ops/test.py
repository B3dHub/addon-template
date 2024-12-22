import bpy
from bpy.types import Operator


class XX_OT_test(Operator):
    bl_label = "Test"
    bl_idname = "xx.test"
    bl_options = {"REGISTER", "INTERNAL"}

    @classmethod
    def poll(cls, context):
        return True

    @classmethod
    def description(cls, context, properties):
        return "Lorem Ipsum.\n\nShift  •  Lorem Ipsum.\nCtrl    •  Lorem Ipsum.\nAlt   •  Lorem Ipsum"

    def invoke(self, context, event):
        return {"FINISHED"}

    def execute(self, context):
        return {"FINISHED"}

    def modal(self, context, event):
        return {"FINISHED"}


classes = (XX_OT_test,)


register, unregister = bpy.utils.register_classes_factory(classes)
