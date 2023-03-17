##Ahora coge el treeview y metelo e una interfaz donde haya 5 botones en la parte inferior y dos checkbox

#Importar librerias necesarias
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import sqlite3

#Crear una clase que herede de Gtk.Window para la ventana principal:
class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Perfiles")
        self.set_default_size(600, 400)

        # Crear una caja vertical para organizar los elementos
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        # Conectar a la base de datos y ejecutar una consulta para obtener los datos
        conn = sqlite3.connect('perfiles.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM perfiles')
        data = cursor.fetchall()

        # Crear un ListStore que contenga los datos obtenidos de la base de datos
        liststore = Gtk.ListStore(str, str, str, str, str, str, str)
        for item in data:
            liststore.append(item)

        # Crear un TreeView y añadirle las columnas correspondientes
        treeview = Gtk.TreeView.new_with_model(liststore)
        for i, column_title in enumerate(["ID", "Nombre", "Apellido", "Edad", "Género", "Email", "Teléfono"]):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title, renderer, text=i)
            treeview.append_column(column)

        # Agregar el TreeView a la caja vertical
        vbox.pack_start(treeview, True, True, 0)

        # Crear un botón para agregar un perfil
        add_button = Gtk.Button(label="Agregar")
        add_button.connect("clicked", self.on_add_clicked)
        vbox.pack_start(add_button, False, False, 0)

        # Crear un botón para editar un perfil
        edit_button = Gtk.Button(label="Editar")
        edit_button.connect("clicked", self.on_edit_clicked)
        vbox.pack_start(edit_button, False, False, 0)

        # Crear un botón para eliminar un perfil
        delete_button = Gtk.Button(label="Eliminar")
        delete_button.connect("clicked", self.on_delete_clicked)
        vbox.pack_start(delete_button, False, False, 0)

        # Crear un botón para buscar un perfil
        search_button = Gtk.Button(label="Buscar")
        search_button.connect("clicked", self.on_search_clicked)
        vbox.pack_start(search_button, False, False, 0)

        # Crear un botón para salir de la aplicación
        quit_button = Gtk.Button(label="Salir")
        quit_button.connect("clicked", Gtk.main_quit)
        vbox.pack_start(quit_button, False, False, 0)

        # Crear dos checkboxes para filtrar los perfiles por género y edad
        self.gender_filter = Gtk.CheckButton(label="Filtrar por género")
        self.gender_filter.connect("toggled", self.on_gender_filter_toggled)
        vbox.pack_start(self.gender_filter, False, False, 0)

        self.age_filter = Gtk.CheckButton(label="Filtrar por edad")
        self.age_filter.connect("toggled", self.on_age_filter_toggled)
        vbox.pack_start(self.age_filter, False, False, 0)


# Agregar código para abrir una ventana
    def on_add_clicked(self, button):
# Crear una nueva ventana para agregar un perfil
    dialog = Gtk.Dialog(title="Agregar perfil", parent=self, flags=0)
    dialog.add_button("Cancelar", Gtk.ResponseType.CANCEL)
    dialog.add_button("Guardar", Gtk.ResponseType.OK)

# Crear una caja vertical para organizar los elementos de la ventana
    vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
    dialog.get_content_area().add(vbox)

# Crear campos de entrada de texto para cada campo de la tabla
    id_entry = Gtk.Entry()
    id_entry.set_placeholder_text("ID")
    vbox.pack_start(id_entry, False, False, 0)

    name_entry = Gtk.Entry()
    name_entry.set_placeholder_text("Nombre")
    vbox.pack_start(name_entry, False, False, 0)

    last_name_entry = Gtk.Entry()
    last_name_entry.set_placeholder_text("Apellido")
    vbox.pack_start(last_name_entry, False, False, 0)

    age_entry = Gtk.Entry()
    age_entry.set_placeholder_text("Edad")
    vbox.pack_start(age_entry, False, False, 0)

    gender_entry = Gtk.Entry()
    gender_entry.set_placeholder_text("Género")
    vbox.pack_start(gender_entry, False, False, 0)

    email_entry = Gtk.Entry()
    email_entry.set_placeholder_text("Email")
    vbox.pack_start(email_entry, False, False, 0)

    phone_entry = Gtk.Entry()
    phone_entry.set_placeholder_text("Teléfono")
    vbox.pack_start(phone_entry, False, False, 0)

    dialog.show_all()

    # Esperar hasta que el usuario cierre la ventana
    response = dialog.run()

    # Si el usuario hizo clic en "Guardar", agregar el nuevo perfil a la base de datos
    if response == Gtk.ResponseType.OK:
        conn = sqlite3.connect('perfiles.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO perfiles VALUES (?, ?, ?, ?, ?, ?, ?)",
                       (id_entry.get_text(), name_entry.get_text(), last_name_entry.get_text(),
                        age_entry.get_text(), gender_entry.get_text(), email_entry.get_text(),
                        phone_entry.get_text()))
        conn.commit()

    dialog.destroy()
