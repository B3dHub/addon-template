import bpy

from ... import __package__ as package
from ... import bl_info

__all__ = ["package", "preferences", "version", "version_str"]


version = bl_info["version"]
version_str = ".".join(map(str, bl_info["version"]))


def preferences() -> dict:
    """Get the preferences of the addon.

    Returns:
        dict: Returns the preferences of the addon.
    """
    return bpy.context.preferences.addons[package].preferences
