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
        protocolNameEntry.connect("changed", self.on_name_changed)

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
        protocolDescriptionEntry.connect("changed", self.on_description_changed)

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

        protocol_type_label = Gtk.Label()
        protocol_type_label.set_text("Data Type")
        protocol_type_entry = Gtk.Entry()
        protocol_type_entry.connect("changed", self.on_data_changed)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        row.add(hbox)

        hbox.pack_start(protocol_type_label, True, True, 0)
        hbox.pack_start(protocol_type_entry, True, True, 0)

        self.listbox.add(row)

        protocol_size_label = Gtk.Label()
        protocol_size_label.set_text("Size")
        protocol_size_entry = Gtk.Entry()
        protocol_size_entry.connect("changed", self.on_size_changed)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        row.add(hbox)

        hbox.pack_start(protocol_size_label, True, True, 0)
        hbox.pack_start(protocol_size_entry, True, True, 0)

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

    def on_name_changed(self, entry):
        self.get_toplevel().protocol.dissector.dtree.nodes[self.i].name = entry.get_text()
        self.label.set_text("Field [{}]".format(entry.get_text()))

    def on_description_changed(self, entry):
        self.get_toplevel().protocol.dissector.dtree.nodes[self.i].description = entry.get_text()

    def on_data_changed(self, entry):
        self.get_toplevel().protocol.dissector.dtree.nodes[self.i].data_type = entry.get_text()

    def on_size_changed(self, entry):
        self.get_toplevel().protocol.dissector.dtree.nodes[self.i].size = int(entry.get_text())


class StartField(CanvasElement):

    def __init__(self):
        CanvasElement.__init__(self, "Start Field")



        protocolNameLabel = Gtk.Entry()
        protocolNameLabel.set_text("Protocol Name")
        protocolNameLabel.set_editable(False)
        protocolNameEntry = Gtk.Entry()
        protocolNameEntry.connect("changed", self.on_name_changed)
        
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
        dependentProtocolNameEntry.connect("changed", self.on_dependency_changed)
        
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
        dependencyPatternEntry.connect("changed", self.on_pattern_changed)
        
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        row.add(hbox)
       
        hbox.pack_start(dependencyPatternLabel, True, True, 0)
        hbox.pack_start(dependencyPatternEntry, True, True, 0)
 
        self.listbox.add(row)

    def on_name_changed(self, entry):
        self.get_toplevel().protocol.name = entry.get_text()

    def on_dependency_changed(self, entry):
        self.get_toplevel().protocol.dissector.dtree.nodes[self.i].dependency = entry.get_text()
        print(self.get_toplevel().protocol.dissector.dtree.nodes)

    def on_pattern_changed(self, entry):
        self.get_toplevel().protocol.dissector.dtree.nodes[self.i].pattern = entry.get_text()

