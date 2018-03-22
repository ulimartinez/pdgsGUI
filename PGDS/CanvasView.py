import gi
gi.require_version('Gtk', '3.0')
gi.require_version('GooCanvas', '2.0')
from gi.repository import Gtk, Gdk, GdkPixbuf, GooCanvas

(TARGET_ENTRY_TEXT, TARGET_ENTRY_PIXBUF) = range(2)
(COLUMN_TEXT, COLUMN_PIXBUF) = range(2)

DRAG_ACTION = Gdk.DragAction.COPY


class CanvasView(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Dissector Builder Area")

        hbox = Gtk.Box(spacing=12)
        self.add(hbox)

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
        self.field_icon.add_item("Start Field", "image-missing")
        self.field_icon.add_item("1 byte", "help-about")
        self.field_icon.add_item("2 byte", "help-about")
        self.field_icon.add_item("4 byte", "help-about")
        self.field_icon.add_item("8 byte", "help-about")
        self.field_icon.add_item("16 byte", "help-about")
        self.field_icon.add_item("N byte", "help-about")
        self.field_icon.add_item("Reference List", "help-about")
        self.field_icon.add_item("Packet Info", "help-about")
        self.field_icon.add_item("End Field", "edit-copy")

        self.construct_icon = DragSourceIconView()
        self.construct_icon.add_item("Decision", "help-about")
        self.construct_icon.add_item("Decision", "help-about")
        self.construct_icon.add_item("Decision", "help-about")
        self.construct_icon.add_item("Decision", "help-about")
        self.drop_area = DropArea()
        self.drop_area.connect("draw", self.drop_area.on_draw)

        fields.add(self.field_icon)
        constructs.add(self.construct_icon)
        hbox.pack_start(self.drop_area, True, True, 0)
        hbox.pack_start(pallete, False, False, 0)

        self.add_image_targets()

    def add_image_targets(self, button=None):
        targets = Gtk.TargetList.new([])
        targets.add_image_targets(TARGET_ENTRY_PIXBUF, True)

        self.drop_area.drag_dest_set_target_list(targets)
        self.field_icon.drag_source_set_target_list(targets)

    def add_text_targets(self, button=None):
        self.drop_area.drag_dest_set_target_list(None)
        self.field_icon.drag_source_set_target_list(None)

        self.drop_area.drag_dest_add_text_targets()
        self.field_icon.drag_source_add_text_targets()


class DragSourceIconView(Gtk.IconView):

    def __init__(self):
        Gtk.IconView.__init__(self)
        self.set_text_column(COLUMN_TEXT)
        self.set_pixbuf_column(COLUMN_PIXBUF)

        model = Gtk.ListStore(str, GdkPixbuf.Pixbuf)
        self.set_model(model)

        self.enable_model_drag_source(Gdk.ModifierType.BUTTON1_MASK, [],
            DRAG_ACTION)
        self.connect("drag-data-get", self.on_drag_data_get)

    def on_drag_data_get(self, widget, drag_context, data, info, time):
        selected_path = self.get_selected_items()[0]
        selected_iter = self.get_model().get_iter(selected_path)

        if info == TARGET_ENTRY_TEXT:
            text = self.get_model().get_value(selected_iter, COLUMN_TEXT)
            data.set_text(text, -1)
        elif info == TARGET_ENTRY_PIXBUF:
            pixbuf = self.get_model().get_value(selected_iter, COLUMN_PIXBUF)
            data.set_pixbuf(pixbuf)

    def add_item(self, text, icon_name):
        pixbuf = Gtk.IconTheme.get_default().load_icon(icon_name, 16, 0)
        self.get_model().append([text, pixbuf])


class DropArea(Gtk.Label):

    def __init__(self):
        GooCanvas.Canvas.__init__(self)
        self.drag_dest_set(Gtk.DestDefaults.ALL, [], DRAG_ACTION)
        self.nodes = []
        self.connect("drag-data-received", self.on_drag_data_received)

    def on_drag_data_received(self, widget, drag_context, x,y, data,info, time):
        self.save_coords(x, y)
        self.queue_draw()

    def on_draw(self, widget, context):
        context.set_source_rgb(0.9, 0, 0.1)  # rosso
        for x, y in self.nodes:
            context.rectangle(x, y, 20, 20)
        context.fill()

    def save_coords(self, x, y):
        self.nodes.append((x, y))


win = CanvasView()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()