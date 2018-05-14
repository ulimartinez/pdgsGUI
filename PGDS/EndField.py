import gi
from CanvasElement import CanvasElement
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class EndField(CanvasElement):
    def __init__(self):
        CanvasElement.__init__(self, "End Field")
        self.set_border_width(25)
        self.set_size_request(800, 100)

        # Layout
        grid = Gtk.Grid()
        self.listbox.add(grid)

##
##win = FileChooserWindow()
##
##win.connect("delete-event", Gtk.main_quit)
##win.show_all()
##Gtk.main()
