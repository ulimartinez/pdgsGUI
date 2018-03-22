import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Menu(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")

        self.box = Gtk.Box(spacing=6)
        self.add(self.box)

        self.button1 = Gtk.Button(label="Create Project")
        self.button1.connect("clicked", self.on_button1_clicked)
        self.box.pack_start(self.button1, True, True, 0)

        self.button2 = Gtk.Button(label="Save Project")
        self.button2.connect("clicked", self.on_button2_clicked)
        self.box.pack_start(self.button2, True, True, 0)

        self.button3 = Gtk.Button(label="Close Project")
        self.button3.connect("clicked", self.on_button3_clicked)
        self.box.pack_start(self.button3, True, True, 0)

        self.button1 = Gtk.Button(label="Switch Workspace")
        self.button1.connect("clicked", self.on_button1_clicked)
        self.box.pack_start(self.button1, True, True, 0)

        self.button2 = Gtk.Button(label="Import Project")
        self.button2.connect("clicked", self.on_button2_clicked)
        self.box.pack_start(self.button2, True, True, 0)

        self.button3 = Gtk.Button(label="Export Project")
        self.button3.connect("clicked", self.on_button3_clicked)
        self.box.pack_start(self.button3, True, True, 0)

        self.button1 = Gtk.Button(label="Generate Dissector Script")
        self.button1.connect("clicked", self.on_button1_clicked)
        self.box.pack_start(self.button1, True, True, 0)

        self.button2 = Gtk.Button(label="Organize Views")
        self.button2.connect("clicked", self.on_button2_clicked)
        self.box.pack_start(self.button2, True, True, 0)

        self.button3 = Gtk.Button(label="Open PCAP")
        self.button3.connect("clicked", self.on_button3_clicked)
        self.box.pack_start(self.button3, True, True, 0)

    def on_button1_clicked(self, widget):
        print("Create Project")

    def on_button2_clicked(self, widget):
        print("Save Project")

    def on_button3_clicked(self, widget):
        print("Close Project")

    def on_button4_clicked(self, widget):
        print("Switch Workspace")

    def on_button5_clicked(self, widget):
        print("Import Project")

    def on_button6_clicked(self, widget):
        print("Export Project")

    def on_button7_clicked(self, widget):
        print("Generate Dissector Script")

    def on_button8_clicked(self, widget):
        print("Organize Views")

    def on_button9_clicked(self, widget):
        print("Open PCAP")
win = Menu()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()