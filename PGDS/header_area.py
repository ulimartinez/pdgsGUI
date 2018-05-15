from DS_Overlay import DSOverlay
from NewProjectWindow import NewProjectDialog
from OrganizeOverlay import OrganizeView
from PCAPOverlayDia import PCAPOverlayDia
from ProjectExporter import ProjectExportWindow
from ProjectImporter import ProjectImporter
from WorkspaceLauncher import WorkspaceLauncher
from builder.LuaScript import LuaScript

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class ButtonWindow(Gtk.Box):

    def __init__(self):
        
        Gtk.Box.__init__(self, spacing=6)
        

        # Menu buttons
        button = Gtk.Button.new_with_label("Create Project")
        button.connect("clicked", self.on_create_proj_clicked)
        self.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_mnemonic("_Save Project")
        button.connect("clicked", self.on_save_proj_clicked)
        self.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_mnemonic("_Close Project")
        button.connect("clicked", self.on_close_proj_clicked)
        self.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_mnemonic("_Switch Workspace")
        button.connect("clicked", self.on_switch_wrkspace_clicked)
        self.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_mnemonic("_Import Project")
        button.connect("clicked", self.on_import_proj_clicked)
        self.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_mnemonic("_Export Project")
        button.connect("clicked", self.on_export_proj_clicked)
        self.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_mnemonic("_Generate Dissector Script")
        button.connect("clicked", self.on_generate_ds_clicked)
        self.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_mnemonic("_Organize Views")
        button.connect("clicked", self.on_organize_views_clicked)
        self.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_mnemonic("_Open PCAP")
        button.connect("clicked", self.on_open_pcap_clicked)
        self.pack_start(button, True, True, 0)

    def on_create_proj_clicked(self, button):
        print("\"Create Project\" button was clicked")
        dialog = NewProjectDialog(self)
        response = dialog.run()

        dialog.destroy()

    def on_save_proj_clicked(self, button):
        print("\"Save Project\" button was clicked")

    def on_close_proj_clicked(self, button):
        print("\"Close button\" button was clicked")
        Gtk.main_quit()

    def on_switch_wrkspace_clicked(self, button):
        print("\"Switch Workspace\" button was clicked")
        dialog = WorkspaceLauncher()
        response = dialog.show_all()

    def on_import_proj_clicked(self, button):
        print("\"Import Project\" button was clicked")
        dialog = ProjectImporter()
        response = dialog.show_all()

    def on_export_proj_clicked(self, button):
        print("\"Export Project\" button was clicked")
        dialog = ProjectExportWindow()
        response = dialog.show_all()

    def on_generate_ds_clicked(self, button):
        print("\"Generate Dissector Script\" button was clicked")
        lua = LuaScript(self.get_toplevel().protocol)
        print(lua.generate_script())

        dialog = DSOverlay(self)
        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            print("The OK button was clicked")
        elif response == Gtk.ResponseType.CANCEL:
            print("The Cancel button was clicked")

        dialog.destroy()

    def on_organize_views_clicked(self, button):
        print("\"Organize Views\" button was clicked")
        dialog = OrganizeView()
        response = dialog.show_all()

    def on_open_pcap_clicked(self, button):
        print("\"Open PCAP\" button was clicked")
        dialog = PCAPOverlayDia(self.get_toplevel())
        response = dialog.run()

        dialog.destroy()


# win = ButtonWindow()
# win.connect("delete-event", Gtk.main_quit)
# win.show_all()
# Gtk.main()
