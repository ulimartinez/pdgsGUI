import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class ProjectNavigatorWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Project Navigator")
        self.set_border_width(25)
        self.set_default_size(100, 500)

        # Layout
        grid = Gtk.Grid()
        self.add(grid)

        # Workspace Label
        label = Gtk.Label()
        label.set_label("Workspace: ")
        grid.attach(label, 0, 0, 1, 1)

        # Workspace name
        workspace = Gtk.Label()
        workspace.set_label("X")
        grid.attach(workspace, 1, 0, 1, 1)


        ###############################
        # Project Row
        ##############################

        # Project Label
        p_label = Gtk.Label()
        p_label.set_label("Project")
        # p_label.set_halign(Gtk.Align.RIGHT)
        grid.attach(p_label, 0, 1, 1, 1)

        # Entries
        self.p_name = Gtk.Entry()
        self.p_name.set_text("Project Name")
        grid.attach(self.p_name, 1, 1, 1, 1)


win = ProjectNavigatorWindow()

win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
