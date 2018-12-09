import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Fereastra(Gtk.Window):

	def __init__(self):
		Gtk.Window.__init__(self, title="GTK BOX")

		self.box = Gtk.Box(spacing=6)
		self.add(self.box)

		self.button1 = Gtk.Button(label="salut")
		self.button1.connect("clicked", self.on_button1_clicked)
		self.box.pack_start(self.button1, True, True, 0)

		self.button2 = Gtk.Button(label="la revedere")
		self.button2.connect("clicked", self.on_button2_clicked)
		self.box.pack_start(self.button2, True, True, 0)

	def on_button1_clicked(self, widget):
		print("SALUT!")

	def on_button2_clicked(self, widget):
		print("LA REVEDERE!")

fereastra = Fereastra()
fereastra.connect("destroy", Gtk.main_quit)
fereastra.show_all()
Gtk.main()
