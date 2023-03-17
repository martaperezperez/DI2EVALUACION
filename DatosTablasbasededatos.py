##Ahora haz que los datos los coja de diferentes tablas en la base de datos y que de cada una de esas tablas solo coja 2 campos

#Para obtener los datos de diferentes tablas en la base de datos y solo seleccionar 2 campos de cada una, se pueden hacer cambios en la consulta SQL dentro del método __init__ de la clase MainWindow. Por ejemplo, si la base de datos tiene dos tablas llamadas perfiles1 y perfiles2 y solo se quieren seleccionar los campos id y nombre de cada tabla, la consulta SQL se puede modificar de la siguiente manera:

import gi


gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import sqlite3

#Crear una base de datos que herede de Gtk.Window para la ventana principal

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Perfiles")
        self.set_default_size(600, 400)

#Conectar a la base de datos y ejecutar una consulta para obtener los datos:
        conn = sqlite3.connect('perfiles.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM perfiles')
        data = cursor.fetchall()

#Crear un ListStore que contenga los datos obtenidos de la base de datos:

        liststore = Gtk.ListStore(str, str, str, str, str, str, str)
        for item in data:
            liststore.append(item)

#Crear un TreeView y añadirle las columnas correspondientes

        treeview = Gtk.TreeView.new_with_model(liststore)

        for i, column_title in enumerate(["ID", "Nombre", "Apellido", "Edad", "Género", "Email", "Teléfono"]):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title, renderer, text=i)
            treeview.append_column(column)

#Añadir el TreeView a la ventana principal y mostrarla

        self.add(treeview)
        self.show_all()




# Conectar a la base de datos y ejecutar una consulta para obtener los datos
        conn = sqlite3.connect('perfiles.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, nombre FROM perfiles1 UNION SELECT id, nombre FROM perfiles2')
        data = cursor.fetchall()

# Crear un ListStore que contenga los datos obtenidos de la base de datos
        self.liststore = Gtk.ListStore(str, str)
        for row in data:
            self.liststore.append(list(row))

# Crear un TreeView que muestre los datos del ListStore
        treeview = Gtk.TreeView(model=self.liststore)
        for i, column_title in enumerate(["ID", "Nombre"]):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title, renderer, text=i)
            treeview.append_column(column)

        vbox.pack_start(treeview, True, True, 0)

# Crear botones y checkboxes
        add_button = Gtk.Button.new_with_label("Agregar")
        add_button.connect("clicked", self.on_add_clicked)
        vbox.pack_start(add_button, False, False, 0)

        edit_button = Gtk.Button.new_with_label("Editar")
        edit_button.connect("clicked", self.on_edit_clicked)
        vbox.pack_start(edit_button, False, False, 0)

        delete_button = Gtk.Button.new_with_label("Eliminar")
        delete_button.connect("clicked", self.on_delete_clicked)
        vbox.pack_start(delete_button, False, False, 0)

        search_button = Gtk.Button.new_with_label("Buscar")
        search_button.connect("clicked", self.on_search_clicked)
        vbox.pack_start(search_button, False, False, 0)

        filter_box = Gtk.Box(spacing=6)
        vbox.pack_start(filter_box, False, False, 0)

        gender_filter_check = Gtk.CheckButton(label="Filtrar por género")
        gender_filter_check.connect("toggled", self.on_gender_filter_toggled)
        filter_box.pack_start(gender_filter_check, False, False, 0)

        age_filter_check = Gtk.CheckButton(label="Filtrar por edad")
        age_filter_check.connect("toggled", self.on_age_filter_toggled)
        filter_box.pack_start(age_filter_check, False, False, 0)

# Mostrar la ventana
        self.show_all()
