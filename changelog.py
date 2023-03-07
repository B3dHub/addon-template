import bpy
from bpy.types import Operator
from . import bl_info
from collections import defaultdict
import re


class XX_OT_changelog(Operator):
    '''Get latest changelog'''
    bl_label = 'Changelog'
    bl_idname = 'xx.changelog'

    def draw(self, context):
        layout = self.layout
        layout.scale_y = 1.2
        layout.scale_x = 1.2

        layout.label(
            text=f"Changelog - v{bl_info['version'][0]}.{bl_info['version'][1]}.{bl_info['version'][2]}",
            icon='RECOVER_LAST',
        )

        if self.changes['added']:
            layout.label(text='ADDED')
            box = layout.box()
            col = box.column(align=True)
            for added in self.changes['added']:
                row = col.row()
                if 'https://discord.com' in added:
                    thread = re.search('\/(\d*)\)', added).group(1)
                    row.label(text=added.replace(f'(https://discord.com/channels/959138815602229389/{thread})', ''), icon='MODIFIER_DATA')
                    row.operator('wm.url_open', icon='LINKED').url=f'https://discord.com/channels/959138815602229389/{thread}'
                else:
                    row.label(text=added, icon='ADD')
        if self.changes['changed']:
            layout.label(text='CHANGED')
            box = layout.box()
            col = box.column(align=True)
            for changed in self.changes['changed']:
                row = col.row()
                if 'https://discord.com' in changed:
                    thread = re.search('\/(\d*)\)', changed).group(1)
                    row.label(text=changed.replace(f'(https://discord.com/channels/959138815602229389/{thread})', ''), icon='MODIFIER_DATA')
                    row.operator('wm.url_open', icon='LINKED').url=f'https://discord.com/channels/959138815602229389/{thread}'
                else:
                    row.label(text=changed, icon='TRACKING_FORWARDS_SINGLE')
        if self.changes['fixed']:
            layout.label(text='FIXED')
            box = layout.box()
            col = box.column(align=True)
            for fixed in self.changes['fixed']:
                row = col.row()
                if 'https://discord.com' in fixed:
                    thread = re.search('\/(\d*)\)', fixed).group(1)
                    row.label(text=fixed.replace(f'(https://discord.com/channels/959138815602229389/{thread})', ''), icon='MODIFIER_DATA')
                    row.operator('wm.url_open', icon='LINKED', emboss=False).url=f'https://discord.com/channels/959138815602229389/{thread}'
                else:
                    row.label(text=fixed, icon='MODIFIER_DATA')
        if self.changes['improved']:
            layout.label(text='IMPROVED')
            box = layout.box()
            col = box.column(align=True)
            for improved in self.changes['improved']:
                row = col.row()
                if 'https://discord.com' in improved:
                    thread = re.search('\/(\d*)\)', improved).group(1)
                    row.label(text=improved.replace(f'(https://discord.com/channels/959138815602229389/{thread})', ''), icon='MODIFIER_DATA')
                    row.operator('wm.url_open', icon='LINKED').url=f'https://discord.com/channels/959138815602229389/{thread}'
                else:
                    row.label(text=improved, icon='SHADERFX')
        if self.changes['removed']:
            layout.label(text='REMOVED')
            box = layout.box()
            col = box.column(align=True)
            for removed in self.changes['removed']:
                row = col.row()
                if 'https://discord.com' in removed:
                    thread = re.search('\/(\d*)\)', removed).group(1)
                    row.label(text=removed.replace(f'(https://discord.com/channels/959138815602229389/{thread})', ''), icon='MODIFIER_DATA')
                    row.operator('wm.url_open', icon='LINKED').url=f'https://discord.com/channels/959138815602229389/{thread}'
                else:
                    row.label(text=removed, icon='REMOVE')

    def invoke(self, context, event):
        self.execute(context)
        return context.window_manager.invoke_popup(self, width=500)

    def execute(self, context):
        self.changes = defaultdict(list)

        with open('README.md', 'r') as file:
            changlog_start = False
            key = None

            for line in file:
                line = line.strip()

                if line.startswith("## Changelog"):
                    changlog_start = True
                elif line.startswith("##"):
                    changlog_start = False

                if not changlog_start:
                    continue

                if line.startswith("**"):
                    key = line.split("**")[1].lower()

                if key is None:
                    continue

                if line.startswith("-"):
                    line = line.strip("- ")
                    self.changes[key].append(line)

        return {'FINISHED'}


classes = (
    XX_OT_changelog,
)

register, unregister = bpy.utils.register_classes_factory(classes)