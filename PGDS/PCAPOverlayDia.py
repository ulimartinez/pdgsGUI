import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class PCAPOverlayDia(Gtk.Dialog):

    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "PCAP", parent, 0)

        self.set_default_size(350,170)
        self.parent = parent
        
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
        self.pcapNameE = Gtk.Entry()
        browseB = Gtk.Button("Browse")
        browseB.connect("clicked", self.on_browse_clicked)
        pcapNameBox.pack_start(pcapNameL,True,True,5)
        pcapNameBox.pack_start(self.pcapNameE,True,True,5)
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
        openButton.connect("clicked", self.on_open_clicked)
        cancelButton = Gtk.Button("Cancel")
        cancelButton.connect("clicked", self.on_cancel_clicked)
        emptyLabel02 = Gtk.Label("")
        buttonsBox.pack_start(emptyLabel02, True, True, 80)
        buttonsBox.pack_start(openButton, True, True, 5)
        buttonsBox.pack_start(cancelButton, True, True, 5)
        listBox.add(row03)

        self.show_all()

    def on_open_clicked(self, widget):
        dissector = self.parent.protocol.dissector
        self.parent.packetStreamWidget.textbuffer.set_text(dissector.get_packets(pcap=self.pcapNameE.get_text()))
        self.parent.dissectedStreamWidget.textbuffer.set_text(dissector.dissect_packet(pcap=self.pcapNameE.get_text()))
        self.destroy()

    def on_cancel_clicked(self, widget):
        print("Cancel button was clicked. Dialog window closing")
        self.destroy()

    def on_browse_clicked(self, widget):
        dialog = Gtk.FileChooserDialog("Please choose a file", self,
            Gtk.FileChooserAction.OPEN,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

        filter_pcap = Gtk.FileFilter()
        filter_pcap.set_name("Capture files")
        filter_pcap.add_pattern("*.pcap")
        dialog.add_filter(filter_pcap)
        self.add_filters(dialog)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            path = dialog.get_filename()
            self.pcapNameE.set_text(path)
            dialog.destroy()
            
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")
            dialog.destroy()

        dialog.destroy()

    def add_filters(self, dialog):
        filter_text = Gtk.FileFilter()
        filter_text.set_name("Text files")
        filter_text.add_mime_type("text/plain")
        dialog.add_filter(filter_text)

        filter_py = Gtk.FileFilter()
        filter_py.set_name("Python files")
        filter_py.add_mime_type("text/x-python")
        dialog.add_filter(filter_py)

        filter_any = Gtk.FileFilter()
        filter_any.set_name("Any files")
        filter_any.add_pattern("*")
        dialog.add_filter(filter_any)

            
##class PCAPOverlayWin(Gtk.Window):
##
##    def __init__(self):
##        Gtk.Window.__init__(self, title="New Project")
##
##        button = Gtk.Button("Open dialog")
##        button.connect("clicked", self.on_button_clicked)
##
##        self.add(button)
##
##    def on_button_clicked(self, widget):
##        dialog = PCAPOverlayDia(self)
##        response = dialog.run()
##
##        dialog.destroy()

##win = PCAPOverlayWin()
##win.connect("delete-event", Gtk.main_quit)
##win.show_all()
##Gtk.main()

