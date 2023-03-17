##Hazme un treeview de 7 columnas en python con GTK que coja los datos de una base de datos llamada perfiles

#importar las librerias necesarias
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

win = MainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()


