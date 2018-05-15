import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkPixbuf
from StartField import StartField, Field
from EndField import EndField
from ReferenceListWin import ReferenceListWin
from PackeInfoField import PacketInfoField
from builder.Construct import *
from field.Field import *

(TARGET_ENTRY_TEXT, TARGET_ENTRY_PIXBUF) = range(2)
(COLUMN_TEXT, COLUMN_PIXBUF) = range(2)

DRAG_ACTION = Gdk.DragAction.COPY


class CanvasView(Gtk.Box):

    def __init__(self):
        Gtk.Box.__init__(self, spacing=0)
        self.selecting_src = False
        self.selecting_dest = False

        fields = Gtk.Expander()
        fields.set_label("Fields")
        fields.set_expanded(True)
        constructs = Gtk.Expander()
        constructs.set_label("Constructs")
        constructs.set_expanded(True)

        pallete = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        
        pallete.pack_start(fields, True, True, 0)
        pallete.pack_start(constructs, True, True, 0)
        connector = Gtk.Button("Connector")
        pallete.pack_end(connector, False, False, 0)
        connector.connect("clicked", self.on_connector_click)

            

        self.field_icon = DragSourceIconView()
        self.field_icon.add_item("Start field", "image-missing", "StartField")
        self.field_icon.add_item("1 byte field", "help-about", "StartField")
        self.field_icon.add_item("2 byte field", "help-about", "StartField")
        self.field_icon.add_item("4 byte field", "help-about", "StartField")
        self.field_icon.add_item("8 byte field", "help-about", "StartField")
        self.field_icon.add_item("16 byte field", "help-about", "StartField")
        self.field_icon.add_item("N byte field", "help-about", "StartField")
        self.field_icon.add_item("Reference list", "help-about", "StartField")
        self.field_icon.add_item("Packet Info", "help-about", "StartField")
        self.field_icon.add_item("End field", "edit-copy", "StartField")

        self.construct_icon = DragSourceIconView()
        self.construct_icon.add_item("Decision", "help-about", "StartField")
        self.construct_icon.add_item("Connector", "help-about", "StartField")
        self.construct_icon.add_item("Decision", "help-about", "StartField")
        self.construct_icon.add_item("Decision", "help-about", "StartField")
        self.drop_area = DropArea()
        self.drop_area.connect("draw", self.drop_area.on_draw)

        fields.add(self.field_icon)
        constructs.add(self.construct_icon)
        
        dropAreaFrame = Gtk.Frame()
        dropAreaFrame.add(self.drop_area)

        self.pack_start(dropAreaFrame, True, True, 0)
        self.pack_start(pallete, True, False, 0)

        self.add_text_targets()

    def add_image_targets(self, button=None):
        targets = Gtk.TargetList.new([])
        targets.add_image_targets(TARGET_ENTRY_PIXBUF, True)

        self.drop_area.drag_dest_set_target_list(targets)
        self.field_icon.drag_source_set_target_list(targets)

    def add_text_targets(self, button=None):
        self.drop_area.drag_dest_set_target_list(None)
        self.field_icon.drag_source_set_target_list(None)
        self.construct_icon.drag_source_set_target_list(None)

        self.drop_area.drag_dest_add_text_targets()
        self.field_icon.drag_source_add_text_targets()
        self.construct_icon.drag_source_add_text_targets()

    def on_connector_click(self, event):
        self.selecting_src = True
        print("Selecting src")


class DragSourceIconView(Gtk.IconView):

    def __init__(self):
        Gtk.IconView.__init__(self)
        self.set_text_column(COLUMN_TEXT)
        self.set_pixbuf_column(COLUMN_PIXBUF)

        model = Gtk.ListStore(str, GdkPixbuf.Pixbuf, str)
        self.set_model(model)

        self.enable_model_drag_source(Gdk.ModifierType.BUTTON1_MASK, [],
            DRAG_ACTION)
        self.connect("drag-data-get", self.on_drag_data_get)

    def on_drag_data_get(self, widget, drag_context, data, info, time):
        selected_path = self.get_selected_items()[0]
        selected_iter = self.get_model().get_iter(selected_path)
        text = self.get_model().get_value(selected_iter, COLUMN_TEXT)
        data.set_text(text, -1)

    def add_item(self, text, icon_name, func):
        pixbuf = Gtk.IconTheme.get_default().load_icon(icon_name, 16, 0)
        self.get_model().append([text, pixbuf, func])


class DropArea(Gtk.Fixed):

    def __init__(self):
        Gtk.Fixed.__init__(self)
        self.set_size_request(1500, 300)
     
        self.drag_dest_set(Gtk.DestDefaults.ALL, [], DRAG_ACTION)
        self.nodes = []
        self.connect("drag-data-received", self.on_drag_data_received)

    def getDrawArea(self):
        return self

    def on_drag_data_received(self, widget, drag_context, x,y, data,info, time):
        self.save_coords(x, y)
        self.queue_draw()
        text = data.get_text()
        field = None
        construct = None
        if "Start" in text:
            field = StartField()
            field.show_all()
            construct = StartConstruct()
        elif "End" in text:
            field = EndField()
            field.show_all()
            construct = EndConstruct()
        elif "field" in text:
            field = Field()
            field.show_all()
            construct = FieldConstruct()
        elif "list" in text:
            field = ReferenceListWin()
            field.show_all()
        elif "Info" in text:
            field = PacketInfoField()
            field.show_all()
        print("Received text: %s" % text)
        self.put(field, x, y)

        dtree = self.get_toplevel().protocol.dissector.dtree
        field.i = len(dtree.nodes)
        dtree.add_construct(construct)

    def on_draw(self, widget, context):
        dtree = self.get_toplevel().protocol.dissector.dtree

        context.set_source_rgb(0.9, 0, 0.1)  # rosso
        for link in dtree.links:
            if link.dest is not None:
                x1, y1 = link.src.translate_coordinates(
                    self, link.src.get_allocated_width() / 2,
                    link.src.get_allocated_height())
                x2, y2 = link.dest.translate_coordinates(self, link.dest.get_allocated_width() / 2, 10)
                context.move_to(x1, y1)
                context.line_to(x2, y2)
                context.stroke()

    def save_coords(self, x, y):
        self.nodes.append((x, y))


#win = CanvasView()
#in.connect("delete-event", Gtk.main_quit)
#win.show_all()
#Gtk.main()
