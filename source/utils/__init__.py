import bpy

# Local modules
from .addon import *
from .icon import *
from . import preview
from . import props
from . import manual


__all__ = ["icons"]


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
