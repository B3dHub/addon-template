bl_info = {
    "name": "Addon",
    "description": "Description",
    "blender": (3, 3, 0),
    "version": (0, 1, 0),
    "category": "Category",
    "location": "3D Viewport > Sidebar(N-Panel) > Addon",
    "author": "Karan",
    "support": "COMMUNITY",
    "warning": "",
    "doc_url": "",
    "tracker_url": "https://discord.gg/sdnHHZpWbT",
}


import bpy

# Built-in modules
from contextlib import suppress

# Local modules
from . import source
from . import preferences
from . import changelog


def register():
    source.register()
    preferences.register()
    changelog.register()


def unregister():
    source.unregister()
    preferences.unregister()
    with suppress(RuntimeError):  # to avoid crash
        changelog.unregister()
