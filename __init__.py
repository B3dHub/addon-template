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

from . import preferences, source


def register():
    source.register()
    preferences.register()


def unregister():
    source.unregister()
    preferences.unregister()
