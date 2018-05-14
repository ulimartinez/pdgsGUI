import gi

from CanvasView import CanvasView, DropArea, DragSourceIconView
from header_area import ButtonWindow
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk



class ListBoxWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Protocol Dissector Generator")
        self.set_border_width(10)

        self.box1 = Gtk.HBox()
        
        header = ButtonWindow()
        headerBox = header.getBox()
      
        self.box1.pack_start(headerBox, True, True, 0)

        self.box2 = Gtk.VBox()
        self.box2.pack_start(self.box1, True, True, 10)        
        
        layoutGrid = Gtk.Grid()
        listbox = Gtk.ListBox()
        row = Gtk.ListBoxRow()
       
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_start(vbox, True, True, 0)
        w_label = Gtk.Label("Workspace:", xalign=0)
        p_label = Gtk.Label()
        p_label.set_label("Project")


        # Entries
        p_name = Gtk.Entry()
        p_name.set_text("Project Name")
        vbox.pack_start(w_label, True, True, 0)
        vbox.pack_start(p_label, True, True, 0)
        vbox.pack_start(p_name, True, True, 0)
        
        
        
        listbox.add(row)
        layoutGrid.attach(listbox, 0,0,1,1)

        canvas = CanvasView()
        canvasBox = canvas.getBox()
        layoutGrid.attach(canvasBox, 3,0,1,1)
        drawArea = DropArea()
        drawWidget = drawArea.getDrawArea()
        layoutGrid.attach(drawWidget, 2,0,1,1)
        

        
        self.box2.pack_start(layoutGrid, True, True, 0)
        








      

        self.add(self.box2)
        


    def on_create_proj_clicked(self, button):
        print("\"Create Project\" button was clicked")
        dialog = NewProjectDialog(self)
        response = dialog.run()

        dialog.destroy()

    def on_save_proj_clicked(self, button):
        print("\"Save Project\" button was clicked")

    def on_close_proj_clicked(self, button):
        print("\"Close button\" button was clicked")
        Gtk.main_quit()

    def on_switch_wrkspace_clicked(self, button):
        print("\"Switch Workspace\" button was clicked")
        dialog = WorkspaceLauncher()
        response = dialog.show_all()

    def on_import_proj_clicked(self, button):
        print("\"Import Project\" button was clicked")
        dialog = ProjectImporter()
        response = dialog.show_all()

    def on_export_proj_clicked(self, button):
        print("\"Export Project\" button was clicked")
        dialog = ProjectExportWindow()
        response = dialog.show_all()

    def on_generate_ds_clicked(self, button):
        print("\"Generate Dissector Script\" button was clicked")

        dialog = DSOverlay(self)
        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            print("The OK button was clicked")
        elif response == Gtk.ResponseType.CANCEL:
            print("The Cancel button was clicked")
 
        dialog.destroy()

    def on_organize_views_clicked(self, button):
        print("\"Organize Views\" button was clicked")
        dialog = OrganizeView()
        response = dialog.show_all()

    def on_open_pcap_clicked(self, button):
        print("\"Open PCAP\" button was clicked")
        dialog = PCAPOverlayDia(self)
        response = dialog.run()

        dialog.destroy()
      

win = ListBoxWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()