import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import os

class MyWindow(Gtk.Window):
    def __init__(self):
        self.activeLoopback = False

        Gtk.Window.__init__(self, title="Meu botão")
        self.set_default_size(200, 300)

        btn = Gtk.Button(label="WAves")
        btn.set_halign(Gtk.Align.CENTER)
        btn.set_valign(Gtk.Align.CENTER)
        btn = Gtk.Button("Clique aqui")
        btn.connect("clicked", self.on_btn_clicked)

        self.add(btn)

    def on_btn_clicked(self, event):
        if (self.activeLoopback is True):
            self.activeLoopback = False
            os.system("pactl unload-module module-loopback")
            
        else:
            self.activeLoopback = True
            os.system("pactl load-module module-loopback latency_msec=1")
        

    
win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
