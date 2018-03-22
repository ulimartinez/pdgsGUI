import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

class StartField(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Start Field [Protocol Name]")
        box_outer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(box_outer)

        listbox = Gtk.ListBox()
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        box_outer.pack_start(listbox, True, True, 10)

        protocolNameLabel = Gtk.Entry()
        protocolNameLabel.set_text("Protocol Name")
        protocolNameLabel.set_editable(False)
        protocolNameEntry = Gtk.Entry()
        
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        row.add(hbox)
       
        hbox.pack_start(protocolNameLabel, True, True, 0)
        hbox.pack_start(protocolNameEntry, True, True, 0)
 
        listbox.add(row)


        protocolDescriptionLabel = Gtk.Entry()
        protocolDescriptionLabel.set_text("Protocol Description")
        protocolDescriptionLabel.set_editable(False)
        protocolDescriptionEntry = Gtk.Entry()
        
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        row.add(hbox)
       
        hbox.pack_start(protocolDescriptionLabel, True, True, 0)
        hbox.pack_start(protocolDescriptionEntry, True, True, 0)
 
        listbox.add(row)

        dependentProtocolNameLabel = Gtk.Entry()
        dependentProtocolNameLabel.set_text("Dependent Protocol Name")
        dependentProtocolNameLabel.set_editable(False)
        dependentProtocolNameEntry = Gtk.Entry()
        
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        row.add(hbox)
       
        hbox.pack_start(dependentProtocolNameLabel, True, True, 0)
        hbox.pack_start(dependentProtocolNameEntry, True, True, 0)
 
        listbox.add(row)

        dependencyPatternLabel = Gtk.Entry()
        dependencyPatternLabel.set_text("Dependency Pattern")
        dependencyPatternLabel.set_editable(False)
        dependencyPatternEntry = Gtk.Entry()
        
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        row.add(hbox)
       
        hbox.pack_start(dependencyPatternLabel, True, True, 0)
        hbox.pack_start(dependencyPatternEntry, True, True, 0)
 
listbox.add(row)
