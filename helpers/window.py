import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import Gtk, Gdk


class BaseWindow():
    def __init__ (self):
        # initialize window
        self.win = Gtk.Window()
        self.win.set_type_hint(Gdk.WindowTypeHint.DIALOG)
        # self.win.set_size_request(600,25)
        self.win.set_title("i3utils - enter a command to execute:")
        self.win.set_position(Gtk.WindowPosition.CENTER)
        self.win.connect("destroy", Gtk.main_quit)
        self.win.connect("key-press-event", self.process_key_press_event)

    def process_key_press_event (self, win, event, data=None):
        if event.keyval == Gdk.KEY_Escape:
            Gtk.main_quit()

    def set_title (self, title):
        self.win.set_title("i3utils - "+title)

    def run (self):
        # subprocess.run(["i3-msg", "mode", "session"])
        self.win.show_all()
        Gtk.main()


class MessageWindow(BaseWindow):
    def __init__ (self, title, text):
        super().__init__()
        # adjust window title
        self.set_title(title)
        # entry
        self.entry = Gtk.TextView()
        self.entry.set_editable(False)
        self.entry.set_cursor_visible(False)
        self.entry.get_buffer().insert_at_cursor(text, len(text))
        self.win.add(self.entry)
