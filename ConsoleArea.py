import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class FileChooserWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Console Area")
        self.set_border_width(25)
        self.set_size_request(800, 150)

        # Layout
        grid = Gtk.Grid()
        self.add(grid)

##
##win = FileChooserWindow()
##
##win.connect("delete-event", Gtk.main_quit)
##win.show_all()
##Gtk.main()
