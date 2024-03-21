import bpy
from . import icon
from . import preview
from . import props
from . import manual


def register():
    icon.register()
    preview.register()
    props.register()
    manual.register()


def unregister():
    icon.unregister()
    preview.unregister()
    props.unregister()
    manual.unregister()
