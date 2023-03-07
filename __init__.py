bl_info = {
    'name': 'Addon',
    'description': 'Description',
    'author': 'Author',
    'blender': (3, 3, 0),
    'version': (0, 1, 0),
    'category': 'Category',
    'location': '3D View > N-Panel > Addon',
    'support': 'COMMUNITY',
    'warning': '',
    'doc_url': '',
    'tracker_url': 'https://discord.gg/sdnHHZpWbT'
}


import bpy
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
    changelog.unregister()