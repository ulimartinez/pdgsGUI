import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class ConsoleArea(Gtk.Window):

    def __init__(self):
       

        self.box = Gtk.Box()
        
        self.textview = Gtk.TextView()
        self.textbuffer = self.textview.get_buffer()
        self.textbuffer.set_text("This is the console area")
        

        self.box.pack_start(self.textview,True,True,0)


    def getConsoleView(self):
        return self.box

##
##win = FileChooserWindow()
##
##win.connect("delete-event", Gtk.main_quit)
##win.show_all()
##Gtk.main()
