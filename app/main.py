import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Meu botão")
        self.set_default_size(200, 200)

        btn = Gtk.Button(label="WAves")
        btn.set_halign(Gtk.Align.CENTER)
        btn.set_valign(Gtk.Align.CENTER)
        btn = Gtk.Button("Clique aqui")
        btn.connect("clicked", self.on_btn_clicked)

        self.add(btn)

    def on_btn_clicked(self, event):
        print("olá mundo")


    
win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
