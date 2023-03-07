import bpy
from . import props
from . import manual


def register():
    props.register()
    manual.register()


def unregister():
    props.unregister()
    manual.unregister()
