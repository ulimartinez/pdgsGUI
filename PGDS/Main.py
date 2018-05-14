import gi
from header_area import ButtonWindow
from CanvasView import  CanvasView
from ProjectNavigator import ProjectNavigatorWindow
from RawDataArea import RawDataArea
from PacketStreamAreaGUI import  PacketStreamAreaGUI
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

win = ButtonWindow()

win.connect("delete-event", Gtk.main_quit)
win.show_all()
canvas = CanvasView()
canvas.show_all()
projnav = ProjectNavigatorWindow()
projnav.show_all()
raw = RawDataArea()
raw.show_all()
stream = PacketStreamAreaGUI()
stream.show_all()

Gtk.main()