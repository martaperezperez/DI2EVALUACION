import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Ejemplo de interfaz compleja")
        self.set_default_size(600, 400)
        self.set_border_width(10)

        # Barra de menú
        menubar = Gtk.MenuBar()
        filemenu = Gtk.Menu()
        filem = Gtk.MenuItem("Archivo")
        filem.set_submenu(filemenu)
        exit = Gtk.MenuItem("Salir")
        exit.connect("activate", Gtk.main_quit)
        filemenu.append(exit)
        menubar.append(filem)

        # Caja principal
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(vbox)
        vbox.pack_start(menubar, False, False, 0)

        # Caja de entrada de texto
        hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        vbox.pack_start(hbox1, False, False, 0)

        label1 = Gtk.Label("Introduce tu nombre:")
        hbox1.pack_start(label1, False, False, 0)

        entry1 = Gtk.Entry()
        hbox1.pack_start(entry1, False, False, 0)

        # Caja de botones
        hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        vbox.pack_start(hbox2, False, False, 0)

        button1 = Gtk.Button("Saludar")
        button1.connect("clicked", self.on_greet_clicked, entry1)
        hbox2.pack_start(button1, False, False, 0)

        button2 = Gtk.Button("Limpiar")
        button2.connect("clicked", self.on_clear_clicked, entry1)
        hbox2.pack_start(button2, False, False, 0)

        # Área de texto
        scrolledwindow = Gtk.ScrolledWindow()
        scrolledwindow.set_hexpand(True)
        scrolledwindow.set_vexpand(True)
        vbox.pack_start(scrolledwindow, True, True, 0)

        textview = Gtk.TextView()
        textview.set_editable(False)
        scrolledwindow.add(textview)

    def on_greet_clicked(self, button, entry):
        name = entry.get_text()
        message = "Hola, {}!".format(name)
        buffer = textview.get_buffer()
        buffer.set_text(message)

    def on_clear_clicked(self, button, entry):
        entry.set_text("")
        buffer = textview.get_buffer()
        buffer.set_text("")

if __name__ == '__main__':
    window = MainWindow()
    window.connect("destroy", Gtk.main_quit)
    window.show_all()
    Gtk.main()
