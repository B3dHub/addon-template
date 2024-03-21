import bpy
import os
import bpy.utils.previews


preview_collections = {}
icon = {}


def load_icons_from_dir(pcoll, directory):
    for entry in os.scandir(directory):
        if entry.is_file() and entry.name.endswith(".png"):
            name = os.path.splitext(entry.name)[0]
            pcoll.load(name, entry.path, "IMAGE")
        elif entry.is_dir():
            load_icons_from_dir(pcoll, entry.path)


def register():
    pcoll = bpy.utils.previews.new()
    icons_dir = os.path.join(os.path.dirname(__file__), "../../icons")
    load_icons_from_dir(pcoll, icons_dir)
    for key, value in pcoll.items():
        icon[key] = value.icon_id
    if preview_collections.get("icons"):
        unregister()
    preview_collections["icons"] = pcoll


def unregister():
    for pcoll in preview_collections.values():
        bpy.utils.previews.remove(pcoll)
    preview_collections.clear()
