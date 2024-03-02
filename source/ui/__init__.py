import bpy
from . import lists
from . import menus
from . import panels


def register():
    lists.register()
    menus.register()
    panels.register()


def unregister():
    lists.unregister()
    menus.unregister()
    panels.unregister()
