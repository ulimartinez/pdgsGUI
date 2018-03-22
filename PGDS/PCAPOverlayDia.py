import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class PCAPOverlayDia(Gtk.Dialog):

    def __init__(self, parent):
        Gtk.Dialog.__init__(self,"PCAP", parent, 0,)

        self.set_default_size(350,170)
        
        self.set_border_width(5)
        createLabel = Gtk.Label("Open a PCAP file")

        box = self.get_content_area()
        box.add(createLabel)
        listBox = Gtk.ListBox()
        listBox.set_selection_mode(Gtk.SelectionMode.NONE)
        box.add(listBox)
        
        # Entry for PCAP name
        row01 = Gtk.ListBoxRow()
        pcapNameBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,spacing=0)
        row01.add(pcapNameBox)
        pcapNameL = Gtk.Label("PCAP Name:")
        pcapNameE = Gtk.Entry()
        browseB = Gtk.Button("Browse")
        pcapNameBox.pack_start(pcapNameL,True,True,5)
        pcapNameBox.pack_start(pcapNameE,True,True,5)
        pcapNameBox.pack_start(browseB,True,True,5)
        listBox.add(row01)
        
        row02 = Gtk.ListBoxRow()
        emptyLBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        row02.add(emptyLBox)
        emptyLabel01 = Gtk.Label("")
        emptyLBox.pack_start(emptyLabel01, False, True,0)
        listBox.add(row02)

        # Creates the cancel and open buttons
        row03 = Gtk.ListBoxRow()
        buttonsBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        row03.add(buttonsBox)
        openButton = Gtk.Button("Open")
        #openButton.connect("clicked", self.on_create_clicked)
        cancelButton = Gtk.Button("Cancel")
        cancelButton.connect("clicked", self.on_cancel_clicked)
        emptyLabel02 = Gtk.Label("")
        buttonsBox.pack_start(emptyLabel02, False, True, 80)
        buttonsBox.pack_start(openButton, False, True, 5)
        buttonsBox.pack_start(cancelButton, False, True, 5)
        listBox.add(row03)

        self.show_all()

    def on_create_clicked(self, widget):
        print("Create button was clicked")
    def on_cancel_clicked(self, widget):
        print("Cancel button was clicked. Dialog window closing")
        self.destroy()
            

class PCAPOverlayWin(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="New Project")

        button = Gtk.Button("Open dialog")
        button.connect("clicked", self.on_button_clicked)

        self.add(button)

    def on_button_clicked(self, widget):
        dialog = PCAPOverlayDia(self)
        response = dialog.run()

        dialog.destroy()

win = PCAPOverlayWin()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()

