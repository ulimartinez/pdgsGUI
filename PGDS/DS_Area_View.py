import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class DissectedStream(Gtk.Box):

    def __init__(self):
        Gtk.Box.__init__(self, orientation=Gtk.Orientation.VERTICAL, spacing=0)

        self.add(Gtk.Label("Dissected Stream Area"))

        textview = Gtk.TextView()
        self.textbuffer = textview.get_buffer()
        self.add(textview)
