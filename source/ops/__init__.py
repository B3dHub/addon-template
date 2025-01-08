import bpy

from . import changelog, test


def register():
    changelog.register()
    test.register()


def unregister():
    changelog.unregister()
    test.unregister()
