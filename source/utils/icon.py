import bpy
import os
import bpy.utils.previews


preview_collections = {}
icon = {}


def register():
    pcoll = bpy.utils.previews.new()
    icons_dir = os.path.join(os.path.dirname(__file__), '../../icons')
    for entry in os.scandir(icons_dir):
        if entry.name.endswith('.png'):
            name = os.path.splitext(entry.name)[0]
            pcoll.load(name.upper(), entry.path, 'IMAGE')
    for key, value in pcoll.items():
        icon[key] = value.icon_id
    if preview_collections.get('icons'):
        unregister()
    preview_collections['icons'] = pcoll


def unregister():
    for pcoll in preview_collections.values():
        bpy.utils.previews.remove(pcoll)
    preview_collections.clear()