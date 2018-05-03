import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class ReferenceListWin(Gtk.Window):

    def  __init__(self):
        Gtk.Window.__init__(self, title = "Reference List [Reference List Name]")
        self.set_default_size(350,200)
        self.set_border_width(5)

        box_outer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(box_outer)

        listBox = Gtk.ListBox()
        listBox.set_selection_mode(Gtk.SelectionMode.NONE)
        box_outer.pack_start(listBox, True, True, 10)

        # Reference List Name entry
        row01 = Gtk.ListBoxRow()
        listNameBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,spacing=0)
        row01.add(listNameBox)
        listRNameL = Gtk.Label("Reference List Name")
        listRNameE = Gtk.Entry()
        listNameBox.pack_start(listRNameL,True,True,0)
        listNameBox.pack_start(listRNameE,True,True,0)
        listBox.add(row01)

        # Value and Description Label
        row02 = Gtk.ListBoxRow()
        labelBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,spacing=0)
        row02.add(labelBox)
        valueLabel = Gtk.Label("Value")
        texDesLabel = Gtk.Label("Text Description")
        labelBox.pack_start(valueLabel,True,True,0)
        labelBox.pack_start(texDesLabel,True,True,0)
        listBox.add(row02)

        # Value and Description Entry
        row03 = Gtk.ListBoxRow()
        entryBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,spacing=0)
        row03.add(entryBox)
        valueEntry = Gtk.Entry()
        texDesEntry = Gtk.Entry()
        entryBox.pack_start(valueEntry,True,True,0)
        entryBox.pack_start(texDesEntry,True,True,0)
        listBox.add(row03)

        self.show_all()

##win = ReferenceListWin()
##win.connect("delete-event", Gtk.main_quit)
##win.show_all()
##Gtk.main()
