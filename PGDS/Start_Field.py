import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class CellRendererTextWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Start Field [Protocol Name]")

        self.set_default_size(400, 300)

        self.liststore = Gtk.ListStore(str, str)
        self.liststore.append(["Protocol Name", " Enter name "])
        self.liststore.append(["Protocol Description", " Enter description"])
        self.liststore.append(["Dependant Protocol Name", " Enter name "])
        self.liststore.append(["Dependancy Pattern", " Integer/Range/String "])

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

        self.add(treeview)

    def text_edited(self, widget, path, text):
        self.liststore[path][1] = text
