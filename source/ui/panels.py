import bpy
from bpy.types import Panel
from ..utils.icon import icon


class Addon:
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Addon"

    def draw_list(self, layout, listtype_name, dataptr, propname, active_propname, rows=4):
        row = layout.row()
        row.scale_y = 1.2
        row.template_list(
            listtype_name,
            "",
            dataptr=dataptr,
            active_dataptr=dataptr,
            propname=propname,
            active_propname=active_propname,
            rows=rows,
        )
        col = row.column(align=True)
        col.scale_x = 1.1
        return col


class XX_PT_object_mode(Panel, Addon):
    bl_label = "Object Mode"

    @classmethod
    def poll(cls, context):
        return context.mode == "OBJECT"

    def draw(self, context):
        layout = self.layout
        layout.use_property_decorate = False
        layout.scale_x = 1.2
        layout.scale_y = 1.2

        prop = context.scene.test

        layout.prop(prop, "name")
        layout.template_icon_view(prop, "preview", show_labels=True, scale=6.0, scale_popup=6.0)
        layout.operator("xx.test")


class XX_PT_edit_mode(Panel, Addon):
    bl_label = "Edit Mode"

    @classmethod
    def poll(cls, context):
        return context.mode == "EDIT_MESH"

    def draw(self, context):
        layout = self.layout
        layout.use_property_decorate = False
        layout.scale_x = 1.2
        layout.scale_y = 1.2

        prop = context.scene.test

        layout.prop(prop, "name")
        layout.operator("xx.test")


class XX_PT_help(Panel, Addon):
    bl_label = "Help"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        layout.use_property_decorate = False
        layout.scale_x = 1.2
        layout.scale_y = 1.2

        col = layout.column()
        col.operator("xx.changelog", icon="RECOVER_LAST")
        col.operator("wm.url_open", text="Documentation", icon="HELP").url = ""
        col.operator("wm.url_open", text="Report a Bug", icon="URL").url = "https://discord.gg/sdnHHZpWbT"
        col.operator("wm.url_open", text="Blender Market", icon_value=icon["B_MARKET"]).url = "https://blendermarket.com/account/orders"
        col.operator("wm.url_open", text="Gumroad", icon_value=icon["GUMROAD"]).url = "https://app.gumroad.com/library"


classes = (
    XX_PT_object_mode,
    XX_PT_edit_mode,
    XX_PT_help,
)


register, unregister = bpy.utils.register_classes_factory(classes)
