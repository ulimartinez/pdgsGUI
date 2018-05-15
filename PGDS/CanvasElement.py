from builder.Construct import ConnectorConstruct
import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk


class CanvasElement(Gtk.Box):

    def __init__(self, title):
        Gtk.Box.__init__(self, orientation=Gtk.Orientation.VERTICAL, spacing=6)

        self.i = 0
        title_box = Gtk.Box()
        del_button = Gtk.Button.new_with_label("X")
        mini_button = Gtk.Button.new_with_label("-")
        mini_button.connect("clicked", self.hide_content)
        del_button.connect("clicked", self.remove_node)
        title_box.pack_end(del_button, False, False, 5)
        title_box.pack_end(mini_button, False, False, 5)
        label_box = Gtk.EventBox()
        label_box.connect("button-press-event", self.on_elem_click)
        label = Gtk.Label(title)
        label_box.add(label)
        title_box.pack_start(label_box, True, True, 10)
        self.pack_start(title_box, True, False, 0)

        self.listbox = Gtk.ListBox()
        self.listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        self.pack_start(self.listbox, True, True, 1)

    def hide_content(self, event):
        if self.listbox.get_visible():
            self.listbox.hide()
        else:
            self.listbox.show()

    def remove_node(self, event):
        self.destroy()

    def on_elem_click(self, event, event2):
        canvas_view = self.get_parent().get_parent().get_parent()
        dtree = self.get_toplevel().protocol.dissector.dtree
        if canvas_view.selecting_src:
            connector = ConnectorConstruct()
            connector.src = self
            dtree.links.append(connector)
            canvas_view.selecting_src = False
            canvas_view.selecting_dest = True
        elif canvas_view.selecting_dest:
            connector = dtree.links[-1]
            connector.dest = self
            canvas_view.selecting_dest = False
            print(dtree.links)
