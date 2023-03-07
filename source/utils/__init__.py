import bpy
from . import icon
from . import props
from . import manual


def register():
    icon.register()
    props.register()
    manual.register()


def unregister():
    icon.unregister()
    props.unregister()
    manual.unregister()
