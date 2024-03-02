import bpy


manual = (("bpy.ops.xx.test", "test.html"),)


def manual_hook():
    return ("(doc_url)", manual)


def register():
    bpy.utils.register_manual_map(manual_hook)


def unregister():
    bpy.utils.unregister_manual_map(manual_hook)
