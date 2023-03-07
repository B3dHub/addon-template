import bpy
from bpy.types import PropertyGroup
from bpy.props import *


class XX_PG_test(PropertyGroup):

    name : StringProperty(default='Test')


classes = (
    XX_PG_test,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.test = bpy.props.PointerProperty(type=XX_PG_test)


def unregister():
    del bpy.types.Scene.test

    for cls in classes:
        bpy.utils.unregister_class(cls)