import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Pango

class SearchDialog(Gtk.Dialog):

    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Search", parent,
            Gtk.DialogFlags.MODAL, buttons=(
            Gtk.STOCK_FIND, Gtk.ResponseType.OK,
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL))

        box = self.get_content_area()

        label = Gtk.Label("Insert text you want to search for:")
        box.add(label)

        self.entry = Gtk.Entry()
        box.add(self.entry)

        self.show_all()

class TextViewWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="CellRendererText Example")
        self.frame = Gtk.Frame()
        self.frame.set_label("Test")
        self.box = Gtk.Box()

        self.add(self.frame)
        self.frame.add(self.box)
        

        

        self.textview = Gtk.TextView()
        self.textbuffer = self.textview.get_buffer()
        self.textbuffer.set_text("This is some text inside of a Gtk.TextView. "
            )
        

        self.box.pack_start(self.textview,True,True,0)


    def getViewPacketStream(self):
        return self.box

      

    

 

win = TextViewWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()