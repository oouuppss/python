#!/usr/bin/env  python3
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit', '3.0')
from gi.repository import Gtk, WebKit, Gdk

appname = "webkiss"
url_home_page= "http://www.debian-facile.org"

class NavigateurMain(Gtk.Window):

    def __init__(self):

        Gtk.Window.__init__(self, title=appname)

        self.hbox = Gtk.HBox()
        self.web_view = WebKit.WebView()
        self.web_view.open(url_home_page)
        self.hbox.pack_start(self.web_view, True, True, 0)

        self.add(self.hbox)
        self.connect("key-press-event", self.on_key_press)
        
    def on_key_press(self, widget, event):
        ''' keyboard shortcut  ctrl+letter '''
        mapping = {Gdk.KEY_q: Gtk.main_quit,
                    Gdk.KEY_g: self.web_cmd_home,
                        Gdk.KEY_r: self.web_cmd_reload,
                            Gdk.KEY_b: self.web_cmd_last,
                                Gdk.KEY_n: self.web_cmd_next}
        if event.state & Gdk.ModifierType.CONTROL_MASK:
            if event.keyval in mapping:
                mapping[event.keyval]()

    # Webkit command
    def web_cmd_home(self):
        self.web_view.open(url_home_page)
    def web_cmd_reload(self):
        self.web_view.reload()
    def web_cmd_last(self):
        self.web_view.go_back()
    def web_cmd_next(self):
        self.web_view.go_forward()

if __name__ == '__main__':
    window = NavigateurMain()
    window.initial_show()
    Gtk.main()
    
quit()
