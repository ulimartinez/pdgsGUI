import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class WorkspaceLauncher(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Workspace Launcher")
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        self.set_default_size(200, 100)

        tit = Gtk.Label("Select a directory as a workspace")
        vbox.pack_start(tit, False, False, 0)

        text_box= Gtk.Box()
        self.text = Gtk.Entry()
        text_box.pack_start(self.text, True, True, 0)

        browse = Gtk.Button.new_with_label("Browse")
        browse.connect("clicked", self.on_click_browse)
        text_box.pack_end(browse, False, False, 0)
        vbox.pack_start(text_box, False, True, 0)

        hbox = Gtk.Box()
        confirm = Gtk.Button.new_with_label("Launch")
        hbox.pack_end(confirm, False, False, 10)
        cancel = Gtk.Button.new_with_label("Cancel")
        cancel.connect("clicked", self.on_cancel_browse)
        hbox.pack_end(cancel, False, False, 10)
        vbox.pack_start(hbox, False, False, 0)

        self.add(vbox)

    def on_click_restore(self, button):
        for row in self.liststore:
            row[1] = True
            row[2] = False

    def on_cancel_browse(self, widget):
        self.hide()

    def on_click_browse(self, button):
        fc = Gtk.FileChooserDialog()
        fc.connect("selection-changed", self.on_file_selected)
        fc.set_action(Gtk.FileChooserAction.SELECT_FOLDER)
        fc.show_all()

    def on_file_selected(self, chooser):
        dir = chooser.get_current_folder()
        if dir is not None:
            self.text.set_text(dir)
