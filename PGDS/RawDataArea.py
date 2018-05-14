import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class RawDataArea(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="CellRendererText Example")

        self.set_default_size(400, 200)

        hb = Gtk.HeaderBar()
        hb.set_show_close_button(True)
        hb.props.title = "Dissected Stream Area"
        self.set_titlebar(hb)

        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=0)
        
        self.liststore = Gtk.ListStore(str, str)
        self.liststore.append(["Raw Data Area",""])
        self.liststore.append(["", " "])

        treeview = Gtk.TreeView(model=self.liststore)

        renderer_text = Gtk.CellRendererText()
        column_text = Gtk.TreeViewColumn(" ", renderer_text, text=0)
        treeview.append_column(column_text)

        renderer_editabletext = Gtk.CellRendererText()

        renderer_editabletext.set_property("editable", True)

        column_editabletext = Gtk.TreeViewColumn(" ",
            renderer_editabletext, text=1)
        treeview.append_column(column_editabletext)

        renderer_editabletext.connect("edited", self.text_edited)
        self.box.pack_start(treeview, True,True,0)
        

    def text_edited(self, widget, path, text):
        self.liststore[path][1] = text
    
    def getRawDataBox(self):
        return self.box





