import bpy

from . import manual, preview, props
from .addon import *
from .icon import *

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
