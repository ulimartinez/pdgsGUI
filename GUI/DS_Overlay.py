## https://developer.gnome.org/pygtk/stable/class-gtkdialog.html#method-gtkdialog--add-action-widget
## https://developer.gnome.org/pygtk/stable/class-gtkdialog.html#method-gtkdialog--set-has-separator
## http://python-gtk-3-tutorial.readthedocs.io/en/latest/index.html

from FileChooserWindow import browse_button
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class DSOverlay(Gtk.Dialog):

    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Dissector Script", parent, 0, (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OK, Gtk.ResponseType.OK))

        self.set_default_size(400, 180)
        self.set_border_width(5)

        label = Gtk.Label("Generate a custom dissector script from a selected project.")

        box = self.get_content_area()
        box.add(label)
        listBox = Gtk.ListBox()
        listBox.set_selection_mode(Gtk.SelectionMode.NONE)
        box.add(listBox)

        #project selection area
        row0 = Gtk.ListBoxRow()
        projBox = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing=0)
        row0.add(projBox)
        projName = Gtk.Label("Project ")
        projEntry = Gtk.Entry()
        browse1 = Gtk.Button("Browse")
        browse1.connect("clicked", self.on_browse_clicked)
        projBox.pack_start(projName,True,True,5)
        projBox.pack_start(projEntry,True,True,5)
        projBox.pack_start(browse1,True,True,5)
        listBox.add(row0)

        #Dissector Format Area
        format = Gtk.Label("Dissector Format ")
        vbox = Gtk.Box(spacing=0)
        options = Gtk.ListStore(int, str)
        options.append([1, "LUA"])
        decision = Gtk.ComboBox.new_with_model_and_entry(options)
        decision.connect("changed", self.on_decision_changed)
        decision.set_entry_text_column(1)
        vbox.pack_start(format,True,True,5)
        vbox.pack_start(decision, False, False, 0)
        listBox.add(vbox)

        #Save Location area
        row2 = Gtk.ListBoxRow()
        saveBox = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing=10)
        row2.add(saveBox)
        saveLoc = Gtk.Label("Save Location ")
        saveEntry = Gtk.Entry()
        browse2 = Gtk.Button("Browse")
        browse2.connect("clicked", self.on_browse_clicked)
        saveBox.pack_start(saveLoc,True,True,5)
        saveBox.pack_start(saveEntry,True,True,5)
        saveBox.pack_start(browse2,True,True,5)
        listBox.add(row2)

        self.show_all()

    def on_browse_clicked(self, widget):
        dialog = Gtk.FileChooserDialog("Please choose a file", self,
            Gtk.FileChooserAction.OPEN,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            print("Open clicked")
            print("File selected: " + dialog.get_filename())
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()

    def on_decision_changed(self, combo):
        tree_iter = combo.get_active_iter()
        if tree_iter is not None:
            model = combo.get_model()
            row_id, name = model[tree_iter][:2]
            print("Selected: ID=%d, name=%s" % (row_id, name))
        else:
            entry = combo.get_child()
            print("Entered: %s" % entry.get_text())
