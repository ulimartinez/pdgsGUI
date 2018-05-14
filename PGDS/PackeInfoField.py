import gi
from CanvasElement import CanvasElement
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

class PacketInfoField(CanvasElement):

    def __init__(self):
        CanvasElement.__init__(self, "Packet Information")

        valueLabel = Gtk.Entry()
        valueLabel.set_text("Value")
        valueLabel.set_editable(False)
        textDescriptionLabel = Gtk.Entry()
        textDescriptionLabel.set_text("Text Description")
        textDescriptionLabel.set_editable(False)
        
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        row.add(hbox)
       
        hbox.pack_start(valueLabel, True, True, 0)
        hbox.pack_start(textDescriptionLabel, True, True, 0)
 
        self.listbox.add(row)


        valueEntry = Gtk.Entry()
        valueEntry.set_text("")
        valueEntry.set_editable(False)
        TextDescriptionEntry = Gtk.Entry()
        TextDescriptionEntry.set_text("")
        TextDescriptionEntry.set_editable(False)
        
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        row.add(hbox)
       
        hbox.pack_start(valueEntry, True, True, 0)
        hbox.pack_start(TextDescriptionEntry, True, True, 0)
 
        self.listbox.add(row)

        addButton = Gtk.Button("+")
        emptyLabel = Gtk.Label("")
        
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        row.add(hbox)
        hbox.pack_start(emptyLabel, True, True, 100)
        hbox.pack_start(addButton, False, False, 0)
 
 
        self.listbox.add(row)
