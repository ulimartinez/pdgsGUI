import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class NewProjectDialog(Gtk.Dialog):

    def __init__(self, parent):
        Gtk.Dialog.__init__(self,"New Project", parent, 0,)

        self.set_default_size(350,170)
        
        self.set_border_width(5)
        createLabel = Gtk.Label("Create a new project")

        box = self.get_content_area()
        box.add(createLabel)
        listBox = Gtk.ListBox()
        listBox.set_selection_mode(Gtk.SelectionMode.NONE)
        box.add(listBox)
        
        # Entry for project name
        row01 = Gtk.ListBoxRow()
        projNameBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,spacing=0)
        row01.add(projNameBox)
        projNameL = Gtk.Label("Project Name:")
        projNameE = Gtk.Entry()
        projNameBox.pack_start(projNameL,True,True,0)
        projNameBox.pack_start(projNameE,True,True,0)
        listBox.add(row01)

        # Entry for project description
        row02 = Gtk.ListBoxRow()
        projDesBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,spacing=0)
        row02.add(projDesBox)
        projDesL = Gtk.Label("Description:")
        projDesE = Gtk.Entry()
        projDesBox.pack_start(projDesL,True,True,0)
        projDesBox.pack_start(projDesE,True,True,0)
        listBox.add(row02)
        
        row03 = Gtk.ListBoxRow()
        emptyLBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        row03.add(emptyLBox)
        emptyLabel01 = Gtk.Label("")
        emptyLBox.pack_start(emptyLabel01, False, True,0)
        listBox.add(row03)

        # Creates the cancel and create buttons
        row04 = Gtk.ListBoxRow()
        buttonsBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        row04.add(buttonsBox)
        createButton = Gtk.Button("Create")
        createButton.connect("clicked", self.on_create_clicked)
        cancelButton = Gtk.Button("Cancel")
        cancelButton.connect("clicked", self.on_cancel_clicked)
        emptyLabel02 = Gtk.Label("")
        buttonsBox.pack_start(emptyLabel02, False, True, 80)
        buttonsBox.pack_start(createButton, False, True, 5)
        buttonsBox.pack_start(cancelButton, False, True, 5)
        listBox.add(row04)

        self.show_all()

    def on_create_clicked(self, widget):
        print("Create button was clicked")
    def on_cancel_clicked(self, widget):
        print("Cancel button was clicked. Dialog window closing")
        self.destroy()
            

class NewProjectWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="New Project")

        button = Gtk.Button("Open dialog")
        button.connect("clicked", self.on_button_clicked)

        self.add(button)

    def on_button_clicked(self, widget):
        dialog = NewProjectDialog(self)
        response = dialog.run()

        dialog.destroy()

win = NewProjectWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()

