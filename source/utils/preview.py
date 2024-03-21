import bpy
from bpy.props import (
    StringProperty,
    EnumProperty,
)
import bpy.utils.previews
import os
import re


def enum_previews(self, context):
    """EnumProperty callback"""
    enum_items = []

    if context is None:
        return enum_items

    directory = os.path.join(os.path.dirname(__file__), "../../previews")

    # Get the preview collection (defined in register func).
    pcoll = preview_collections["previews"]

    if directory == pcoll.previews_dir:
        return pcoll.previews

    # print("Scanning directory: %s" % directory)

    if directory and os.path.exists(directory):
        image_paths = [fn for fn in os.listdir(directory) if fn.lower().endswith(".png")]
        for i, name in enumerate(image_paths):
            # generates a thumbnail preview for a file.
            filepath = os.path.join(directory, name)
            icon = pcoll.get(name)
            thumb = pcoll[name] if icon else pcoll.load(name, filepath, "IMAGE")
            enum_items.append((re.sub(r"\d+ ", "", name).replace(".png", ""), re.sub(r"\d+ ", "", name).replace(".png", ""), "", thumb.icon_id, i))

    pcoll.previews = enum_items
    pcoll.previews_dir = directory
    return pcoll.previews


# We can store multiple preview collections here,
# however in this example we only store "main"
preview_collections = {}


def register():
    # Example Previews
    pcoll = bpy.utils.previews.new()
    pcoll.previews_dir = ""
    pcoll.previews = ()
    preview_collections["previews"] = pcoll


def unregister():
    for pcoll in preview_collections.values():
        bpy.utils.previews.remove(pcoll)
    preview_collections.clear()
