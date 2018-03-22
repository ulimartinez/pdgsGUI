import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class ProjectExportWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Project Export")
        self.set_border_width(25)
        self.set_default_size(300, 100)

        # Layout
        grid = Gtk.Grid()
        self.add(grid)

        # Top Label
        label = Gtk.Label()
        label.set_label("Export a project to the local file system.")
        label.set_halign(Gtk.Align.CENTER)
        grid.attach(label, 1, 0, 1, 1)

        ###############################
        # Project Row
        ##############################

        # Project Label
        p_label = Gtk.Label()
        p_label.set_label("Project")
        # p_label.set_halign(Gtk.Align.RIGHT)
        grid.attach(p_label, 0, 1, 1, 1)

        # Entries
        self.p_name = Gtk.Entry()
        self.p_name.set_text("Project Name")
        grid.attach(self.p_name, 1, 1, 1, 1)

        # Browse Select Folder
        browse1 = Gtk.Button("Browse")
        browse1.connect("clicked", self.on_browse_clicked)
        grid.attach(browse1, 2, 1, 1, 1)

        ###############################
        # Export file Row
        ##############################

        # Export Label
        dir_label = Gtk.Label()
        dir_label.set_label("To export file")
        # dir_label.set_halign(Gtk.Align.RIGHT)
        grid.attach(dir_label, 0, 2, 1, 1)

        # Entries
        self.dir_name = Gtk.Entry()
        self.dir_name.set_text("Local File System Path")
        grid.attach(self.dir_name, 1, 2, 1, 1)

        # Browse Select Folder
        browse2 = Gtk.Button("Browse")
        browse2.connect("clicked", self.on_browse2_clicked)
        grid.attach(browse2, 2, 2, 1, 1)

        ###############################
        # Export & Cancel
        ##############################

        # Export btn
        export1 = Gtk.Button("Export")
        export1.connect("clicked", self.on_export_clicked)
        grid.attach(export1, 1, 3, 1, 1)

        # Cancel btn
        cancel1 = Gtk.Button("Cancel")
        cancel1.connect("clicked", self.on_cancel_clicked)
        grid.attach(cancel1, 2, 3, 1, 1)

    # Add Filters
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

    # Folder Selection
    def on_browse_clicked(self, widget):
        dialog = Gtk.FileChooserDialog("Please choose a folder", self,
            Gtk.FileChooserAction.SELECT_FOLDER,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             "Select", Gtk.ResponseType.OK))
        dialog.connect("selection-changed", self.on_file_selected)
        dialog.set_action(Gtk.FileChooserAction.SELECT_FOLDER)
        dialog.set_default_size(800, 400)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Selection made: ")
            path = dialog.get_filename()
            self.p_name.set_text(path)

            # self.gtk_entry_set_text(self.p_name, select1)
        elif response == Gtk.ResponseType.CANCEL:
            print("Action cancelled")
        dialog.destroy()

    # on File selected
    def on_file_selected(self, chooser):
        dir = chooser.get_current_folder()
        if dir is not None:
            self.p_name(dir)

    # Folder2 Selection
    def on_browse2_clicked(self, widget):
        dialog = Gtk.FileChooserDialog("Please choose a folder", self,
                                       Gtk.FileChooserAction.SELECT_FOLDER,
                                       (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                                        "Select", Gtk.ResponseType.OK))
        dialog.connect("selection-changed", self.on_file2_selected)
        dialog.set_action(Gtk.FileChooserAction.SELECT_FOLDER)
        dialog.set_default_size(800, 400)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Selection made: ")
            path = dialog.get_filename()
            self.dir_name.set_text(path)

            # self.gtk_entry_set_text(self.p_name, select1)
        elif response == Gtk.ResponseType.CANCEL:
            print("Action cancelled")
        dialog.destroy()

    # on File2 selected
    def on_file2_selected(self, chooser):
        dir = chooser.get_current_folder()
        if dir is not None:
            self.dir_name(dir)

    # Export file
    def on_export_clicked(self, widget):
        print("export action")

    # Export file
    def on_cancel_clicked(self, widget):
        print("cancel action")

win = ProjectExportWindow()

win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()

# python C:\Users\luui9\PycharmProjects\SE_gui\FileChooserWindow.py
