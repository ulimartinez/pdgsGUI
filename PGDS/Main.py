import gi
from header_area import ButtonWindow
from ProjectNavigator import ProjectNavigatorWindow
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

win = ButtonWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()