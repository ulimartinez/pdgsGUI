import gi

from CanvasElement import CanvasElement

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk


class Field(CanvasElement):

    def __init__(self):
        CanvasElement.__init__(self, "Field")

        protocolNameLabel = Gtk.Label()
        protocolNameLabel.set_text("Name")
        protocolNameEntry = Gtk.Entry()

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        row.add(hbox)

        hbox.pack_start(protocolNameLabel, True, True, 0)
        hbox.pack_start(protocolNameEntry, True, True, 0)

        self.listbox.add(row)

        protocolAbvLabel = Gtk.Label()
        protocolAbvLabel.set_text("Abreviation")
        protocolAbvEntry = Gtk.Entry()

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        row.add(hbox)

        hbox.pack_start(protocolAbvLabel, True, True, 0)
        hbox.pack_start(protocolAbvEntry, True, True, 0)

        self.listbox.add(row)

        protocolDescriptionLabel = Gtk.Label()
        protocolDescriptionLabel.set_text("Description")
        protocolDescriptionEntry = Gtk.Entry()

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        row.add(hbox)

        hbox.pack_start(protocolDescriptionLabel, True, True, 0)
        hbox.pack_start(protocolDescriptionEntry, True, True, 0)

        self.listbox.add(row)

        dependentProtocolNameLabel = Gtk.Label()
        dependentProtocolNameLabel.set_text("Reference List")
        dependentProtocolNameEntry = Gtk.Entry()

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        row.add(hbox)

        hbox.pack_start(dependentProtocolNameLabel, True, True, 0)
        hbox.pack_start(dependentProtocolNameEntry, True, True, 0)

        self.listbox.add(row)

        dependencyPatternLabel = Gtk.Label()
        dependencyPatternLabel.set_text("Data Type")
        dependencyPatternEntry = Gtk.Entry()

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        row.add(hbox)

        hbox.pack_start(dependencyPatternLabel, True, True, 0)
        hbox.pack_start(dependencyPatternEntry, True, True, 0)

        self.listbox.add(row)

        dependencyPatternLabel = Gtk.Label()
        dependencyPatternLabel.set_text("Size")
        dependencyPatternEntry = Gtk.Entry()

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        row.add(hbox)

        hbox.pack_start(dependencyPatternLabel, True, True, 0)
        hbox.pack_start(dependencyPatternEntry, True, True, 0)

        self.listbox.add(row)

        protocolAbvLabel = Gtk.Label()
        protocolAbvLabel.set_text("Base")
        protocolAbvEntry = Gtk.Entry()

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        row.add(hbox)

        hbox.pack_start(protocolAbvLabel, True, True, 0)
        hbox.pack_start(protocolAbvEntry, True, True, 0)

        self.listbox.add(row)

        protocolAbvLabel = Gtk.Label()
        protocolAbvLabel.set_text("Mask")
        protocolAbvEntry = Gtk.Entry()

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        row.add(hbox)

        hbox.pack_start(protocolAbvLabel, True, True, 0)
        hbox.pack_start(protocolAbvEntry, True, True, 0)

        self.listbox.add(row)

        protocolAbvLabel = Gtk.Label()
        protocolAbvLabel.set_text("Constraint")
        protocolAbvEntry = Gtk.Entry()

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        row.add(hbox)

        hbox.pack_start(protocolAbvLabel, True, True, 0)
        hbox.pack_start(protocolAbvEntry, True, True, 0)

        self.listbox.add(row)


class StartField(CanvasElement):

    def __init__(self):
        CanvasElement.__init__(self, "Start Field")



        protocolNameLabel = Gtk.Entry()
        protocolNameLabel.set_text("Protocol Name")
        protocolNameLabel.set_editable(False)
        protocolNameEntry = Gtk.Entry()
        
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        row.add(hbox)
       
        hbox.pack_start(protocolNameLabel, True, True, 0)
        hbox.pack_start(protocolNameEntry, True, True, 0)
 
        self.listbox.add(row)


        protocolDescriptionLabel = Gtk.Entry()
        protocolDescriptionLabel.set_text("Protocol Description")
        protocolDescriptionLabel.set_editable(False)
        protocolDescriptionEntry = Gtk.Entry()
        
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        row.add(hbox)
       
        hbox.pack_start(protocolDescriptionLabel, True, True, 0)
        hbox.pack_start(protocolDescriptionEntry, True, True, 0)
 
        self.listbox.add(row)

        dependentProtocolNameLabel = Gtk.Entry()
        dependentProtocolNameLabel.set_text("Dependent Protocol Name")
        dependentProtocolNameLabel.set_editable(False)
        dependentProtocolNameEntry = Gtk.Entry()
        
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        row.add(hbox)
       
        hbox.pack_start(dependentProtocolNameLabel, True, True, 0)
        hbox.pack_start(dependentProtocolNameEntry, True, True, 0)
 
        self.listbox.add(row)

        dependencyPatternLabel = Gtk.Entry()
        dependencyPatternLabel.set_text("Dependency Pattern")
        dependencyPatternLabel.set_editable(False)
        dependencyPatternEntry = Gtk.Entry()
        
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        row.add(hbox)
       
        hbox.pack_start(dependencyPatternLabel, True, True, 0)
        hbox.pack_start(dependencyPatternEntry, True, True, 0)
 
        self.listbox.add(row)


# win = StartField()
# win.connect("delete-event", Gtk.main_quit)
# win.show_all()
# Gtk.main()