import gi
from CanvasElement import CanvasElement
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class ReferenceListWin(CanvasElement):

    def  __init__(self):
        CanvasElement.__init__(self, "Reference List [Reference List Name]")

        # Reference List Name entry
        row01 = Gtk.ListBoxRow()
        listNameBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,spacing=0)
        row01.add(listNameBox)
        listRNameL = Gtk.Label("Reference List Name")
        listRNameE = Gtk.Entry()
        listNameBox.pack_start(listRNameL,True,True,0)
        listNameBox.pack_start(listRNameE,True,True,0)
        self.listbox.add(row01)

        # Value and Description Label
        row02 = Gtk.ListBoxRow()
        labelBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,spacing=0)
        row02.add(labelBox)
        valueLabel = Gtk.Label("Value")
        texDesLabel = Gtk.Label("Text Description")
        labelBox.pack_start(valueLabel,True,True,0)
        labelBox.pack_start(texDesLabel,True,True,0)
        self.listbox.add(row02)

        # Value and Description Entry
        row03 = Gtk.ListBoxRow()
        entryBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,spacing=0)
        row03.add(entryBox)
        valueEntry = Gtk.Entry()
        texDesEntry = Gtk.Entry()
        entryBox.pack_start(valueEntry,True,True,0)
        entryBox.pack_start(texDesEntry,True,True,0)
        self.listbox.add(row03)

        self.show_all()

##win = ReferenceListWin()
##win.connect("delete-event", Gtk.main_quit)
##win.show_all()
##Gtk.main()
