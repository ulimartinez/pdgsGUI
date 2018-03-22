import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class PacketStreamAreaGUI(Gtk.Window):

    def  __init__(self):
        Gtk.Window.__init__(self, title = "Packet Stream Area")
        self.set_default_size(200,200)
        self.set_border_width(5)

        self.show_all()
##
##win = PacketStreamAreaGUI()
##win.connect("delete-event", Gtk.main_quit)
##win.show_all()
##Gtk.main()
