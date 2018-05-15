import gi
from builder.Protocol import Protocol
from CanvasView import CanvasView, DropArea, DragSourceIconView
from ConsoleArea import ConsoleArea
from DS_Area_View import DissectedStream
from ProjectNavigator import ProjectNavigatorWindow
from PacketStreamAreaGUI import PacketStreamAreaGUI
from RawDataArea import RawDataArea
from header_area import ButtonWindow
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk



class ListBoxWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Protocol Dissector Generator System")
        self.protocol = Protocol("Awesome")
        self.set_border_width(10)

        self.box1 = Gtk.HBox()
        
        headerBox = ButtonWindow()

        self.box2 = Gtk.VBox()
        self.box2.pack_start(headerBox, True, True, 0)
       
        self.box2.pack_start(self.box1, True, True, 0)        

        layoutGrid = Gtk.Grid()
        listbox = Gtk.ListBox()
        row = Gtk.ListBoxRow()
       
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
       
        self.box2.pack_start(hbox, True, True, 0)
        
        navigator = ProjectNavigatorWindow()
        navigatorWidget = navigator.getGrid()
        
        navigatorFrame = Gtk.Frame()
        navigatorFrame.set_label("Project Navigator")
        
        navigatorFrame.add(navigatorWidget)
        hbox.pack_start(navigatorFrame, True, True, 0)        

        canvasBox = CanvasView()
       


        dissectorFrame = Gtk.Frame()
        dissectorFrame.set_label("Dissector Builder Area")
        dissectorFrame.set_size_request(300,300)
        dissectorFrame.add(canvasBox)
        
        vbox.pack_start(dissectorFrame, True, True, 0)
        hbox.pack_start(vbox,True,True,0)




        dissectedStream = DissectedStream()
        dissectedStreamWidget = dissectedStream.getDissectedStreamBox()
        
        areaHbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        
        
        

        packetStream = PacketStreamAreaGUI()
        packetStreamWidget = packetStream.getPacketArea()
        
        areaHbox.pack_start(packetStreamWidget, True, True, 0)


        areaHbox.pack_start(dissectedStreamWidget, True, True, 0)
        
        rawData = RawDataArea()
        rawDataWidget = rawData.getRawDataBox()
            
        consoleArea = ConsoleArea()
        consoleWidget = consoleArea.getConsoleView()
        
    

        areaHbox.pack_start(rawDataWidget,True,True,0)
        areaHbox.pack_start(consoleWidget,True,True,0)
        
        infoLayoutFrame = Gtk.Frame()
        infoLayoutFrame.add(areaHbox)
        infoLayoutFrame.set_size_request(-1,100)
        vbox.pack_start(infoLayoutFrame,True,True,0)


      
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