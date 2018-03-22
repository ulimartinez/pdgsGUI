import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class OrganizeView(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Organize Views")
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        self.set_default_size(200, 200)

        self.liststore = Gtk.ListStore(str, bool, bool)
        self.liststore.append(["Project Navigation", True, False])
        self.liststore.append(["Dissector Building Area", True, False])
        self.liststore.append(["Pallete", True, False])
        self.liststore.append(["Packet Stream Area", True, False])
        self.liststore.append(["Dissected Stream Area", True, False])
        self.liststore.append(["Raw Data Area", True, False])
        self.liststore.append(["Console Area", True, False])

        tit = Gtk.Label("Customize the views")
        vbox.pack_start(tit, False, False, 0)
        treeview = Gtk.TreeView(model=self.liststore)
        vbox.pack_start(treeview, True, True, 0)

        renderer_text = Gtk.CellRendererText()
        column_text = Gtk.TreeViewColumn("", renderer_text, text=0)
        treeview.append_column(column_text)

        renderer_toggle = Gtk.CellRendererToggle()
        renderer_toggle.set_radio(True)
        renderer_toggle.connect("toggled", self.on_cell_radio_toggled)

        column_toggle = Gtk.TreeViewColumn("Show", renderer_toggle, active=1)
        treeview.append_column(column_toggle)

        renderer_radio = Gtk.CellRendererToggle()
        renderer_radio.set_radio(True)
        renderer_radio.connect("toggled", self.on_cell_radio_toggled)

        column_radio = Gtk.TreeViewColumn("Hide", renderer_radio, active=2)
        treeview.append_column(column_radio)

        hbox = Gtk.Box()
        restore = Gtk.Button.new_with_label("Default")
        restore.connect("clicked", self.on_click_restore)
        hbox.pack_end(restore, False, False, 10)
        confirm = Gtk.Button.new_with_label("Confirm")
        hbox.pack_end(confirm, False, False, 10)
        cancel = Gtk.Button.new_with_label("Cancel")
        cancel.connect("clicked", Gtk.main_quit)
        hbox.pack_end(cancel, False, False, 10)
        vbox.pack_start(hbox, False, False, 0)

        self.add(vbox)

    def on_click_restore(self, button):
        for row in self.liststore:
            row[1] = True
            row[2] = False

    def on_cell_radio_toggled(self, widget, path):
        if not widget.get_active():
            tmp = self.liststore[path][2]
            self.liststore[path][2] = self.liststore[path][1]
            self.liststore[path][1] = tmp
        # self.liststore[path][2] = not self.liststore[path][1]

        # selected_path = Gtk.TreePath(path)
        # print(path)
        # print(self.liststore[path].path)
        # for row in self.liststore:
        #     row[2] = (row.path == selected_path)
