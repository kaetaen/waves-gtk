import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import os


class MyWindow(Gtk.Window):
    def __init__(self):
        self.verify_pulseaudio_installation()
        self.activeLoopback = False

        Gtk.Window.__init__(self, title="Waves")
        self.set_default_size(200, 300)

        btn = Gtk.Button(label="Listen")
        btn.set_halign(Gtk.Align.CENTER)
        btn.set_valign(Gtk.Align.CENTER)
        btn = Gtk.Button("Click Here")
        btn.connect("clicked", self.on_btn_clicked)

        self.add(btn)

    def on_btn_clicked(self, event):
        if (self.activeLoopback is True):
            self.activeLoopback = False
            os.system("pactl unload-module module-loopback")
            
        else:
            self.activeLoopback = True
            os.system("pactl load-module module-loopback latency_msec=1")
        

    def verify_pulseaudio_installation(self):
        if not (os.path.exists('/usr/bin/pactl') or os.path.exists('/bin/pactl')):
            message_dialog = Gtk.MessageDialog(parent=None,
                                  flags=0,
                                  message_type=Gtk.MessageType.WARNING,
                                  buttons=Gtk.ButtonsType.OK,
                                  text="PulseAudio is not installed!")
            message_dialog.run()
            exit()
    
win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
