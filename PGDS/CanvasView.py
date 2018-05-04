import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkPixbuf
from StartField import StartField, Field
from EndField import EndField
from ReferenceListWin import ReferenceListWin
from PackeInfoField import PacketInfoField


(TARGET_ENTRY_TEXT, TARGET_ENTRY_PIXBUF) = range(2)
(COLUMN_TEXT, COLUMN_PIXBUF) = range(2)

DRAG_ACTION = Gdk.DragAction.COPY


class CanvasView:

    def __init__(self):
       

        global hbox
        hbox = Gtk.Box(spacing=12)
        

        fields = Gtk.Expander()
        fields.set_label("Fields")
        fields.set_expanded(True)
        constructs = Gtk.Expander()
        constructs.set_label("Constructs")
        constructs.set_expanded(True)
        pallete = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        pallete.pack_start(fields, True, True, 0)
        pallete.pack_start(constructs, True, True, 0)

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
        self.construct_icon.add_item("Decision", "help-about", "StartField")
        self.construct_icon.add_item("Decision", "help-about", "StartField")
        self.construct_icon.add_item("Decision", "help-about", "StartField")
        self.drop_area = DropArea()
        self.drop_area.connect("draw", self.drop_area.on_draw)

        fields.add(self.field_icon)
        constructs.add(self.construct_icon)
        hbox.pack_start(self.drop_area, True, True, 0)
        hbox.pack_start(pallete, False, False, 0)

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
    def getBox(self):
        global hbox;
        return hbox;


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


class DropArea(Gtk.DrawingArea):

    def __init__(self):
        Gtk.DrawingArea.__init__(self)
        self.drag_dest_set(Gtk.DestDefaults.ALL, [], DRAG_ACTION)
        self.nodes = []
        self.connect("drag-data-received", self.on_drag_data_received)

    def getDrawArea(self):
        return self

    def on_drag_data_received(self, widget, drag_context, x,y, data,info, time):
        self.save_coords(x, y)
        self.queue_draw()
        text = data.get_text()
        if "Start" in text:
            field = StartField()
            field.show_all()
        elif "End" in text:
            field = EndField()
            field.show_all()
        elif "field" in text:
            field = Field()
            field.show_all()
        elif "list" in text:
            field = ReferenceListWin()
            field.show_all()
        elif "Info" in text:
            field = PacketInfoField()
            field.show_all()
        print("Received text: %s" % text)

    def on_draw(self, widget, context):
        context.set_source_rgb(0.9, 0, 0.1)  # rosso
        for x, y in self.nodes:
            context.rectangle(x, y, 80, 40)
        context.fill()

    def save_coords(self, x, y):
        self.nodes.append((x, y))


#win = CanvasView()
#in.connect("delete-event", Gtk.main_quit)
#win.show_all()
#Gtk.main()
