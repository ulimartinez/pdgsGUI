import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

class ProjectImporter(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Project Import")
        box_outer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(box_outer)

        listbox = Gtk.ListBox()
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        box_outer.pack_start(listbox, True, True, 0)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_start(vbox, True, True, 100)
        label = Gtk.Label("Import a project into the current workspace")
        vbox.pack_start(label, True, True, 20)
        listbox.add(row)





        projectLabel = Gtk.Label("Project")
        projectEntry = Gtk.Entry();
        projectEntry.set_text("Project Name")
        browseButton = Gtk.Button("Browse")
        browseButton.connect("clicked", self.on_file_clicked)


        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        hbox.pack_start(projectLabel, True, True, 0)
        hbox.pack_start(projectEntry, True, True, 0)
        hbox.pack_start(browseButton, False, True, 10)
        listbox.add(row)



        importButton = Gtk.Button("Import")
        cancelButton = Gtk.Button("Cancel")
        emptyLabel = Gtk.Label("")
        importButton.connect("clicked", self.on_import_clicked)
        cancelButton.connect("clicked", self.on_cancel_clicked)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        row.add(hbox)
        hbox.pack_start(emptyLabel, False, True, 60)
        hbox.pack_start(importButton, False, True, 5)
        hbox.pack_start(cancelButton, False, True, 5)

        listbox.add(row)






    def on_file_clicked(self, widget):
        dialog = Gtk.FileChooserDialog("Please choose a file", self,
            Gtk.FileChooserAction.OPEN,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

        self.add_filters(dialog)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Open clicked")
            print("File selected: " + dialog.get_filename())
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()

    def add_filters(self, dialog):
        filter_text = Gtk.FileFilter()
        filter_text.set_name("Text files")
        filter_text.add_mime_type("text/plain")
        dialog.add_filter(filter_text)

        filter_py = Gtk.FileFilter()
        filter_py.set_name("Python files")
        filter_py.add_mime_type("text/x-python")
        dialog.add_filter(filter_py)

        filter_any = Gtk.FileFilter()
        filter_any.set_name("Any files")
        filter_any.add_pattern("*")
        dialog.add_filter(filter_any)

    def on_import_clicked(self, widget):
       print "Import Clicked"
       self.hide()

    def on_cancel_clicked(self, widget):
       self.hide()

# win = ProjectImporter()
# win.connect("delete-event", Gtk.main_quit)
# win.show_all()
# Gtk.main()
