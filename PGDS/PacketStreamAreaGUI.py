import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class PacketStreamAreaGUI(Gtk.Box):

    def __init__(self):
        Gtk.Box.__init__(self, orientation=Gtk.Orientation.VERTICAL, spacing=0)

        self.add(Gtk.Label("Packet Stream Area"))

        textview = Gtk.TextView()
        self.textbuffer = textview.get_buffer()
        self.add(textview)
##
##win = PacketStreamAreaGUI()
##win.connect("delete-event", Gtk.main_quit)
##win.show_all()
##Gtk.main()
