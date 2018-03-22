import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class RawDataArea(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Raw Data Area")
        box_outer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(box_outer)

        hbox = Gtk.Box(spacing=10)
        hbox.set_homogeneous(False)
        vbox_left = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox_left.set_homogeneous(False)
        vbox_right = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox_right.set_homogeneous(False)

        label = Gtk.Label("Raw data shall be displayed here")
        vbox_left.pack_start(label, True, True, 0)
      

       
win = RawDataArea()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()