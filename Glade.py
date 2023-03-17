##Ahora imaginate que debo de usar Glade para hacer la misma interfaz que el codigo anterior

#Para crear la misma interfaz que el código anterior utilizando Glade, se puede seguir los siguientes pasos:

# 1-Abrir Glade y crear una nueva ventana.
# 2-Agregar un contenedor GtkBox a la ventana y configurar su orientación vertical.
# 3-Agregar un GtkScrolledWindow al contenedor vertical.
# 4-Agregar un GtkTreeView al GtkScrolledWindow.
# 5-Agregar dos columnas al GtkTreeView. La primera columna tendrá un GtkCellRendererText con el texto "ID" y la segunda columna tendrá un GtkCellRendererText con el texto "Nombre".
# 6-Agregar cinco botones al contenedor vertical. Configurar sus etiquetas como "Agregar", "Editar", "Eliminar", "Buscar" y "Salir".
# 7-Agregar dos GtkCheckButton al contenedor vertical. Configurar sus etiquetas como "Filtrar por género" y "Filtrar por edad".
# 8-Configurar los botones y los GtkCheckButton con sus correspondientes señales y manejadores de señales, de acuerdo con el código anterior.
# Una vez que se ha creado la interfaz en Glade, se puede cargar la interfaz desde el código Python utilizando la clase Gtk.Builder. El código Python para cargar la interfaz y conectar las señales de los botones y los GtkCheckButton podría ser similar al siguiente:


import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MainWindow:
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("interfaz.glade")

        self.window = builder.get_object("window")
        self.treeview = builder.get_object("treeview")
        self.add_button = builder.get_object("add_button")
        self.edit_button = builder.get_object("edit_button")
        self.delete_button = builder.get_object("delete_button")
        self.search_button = builder.get_object("search_button")
        self.gender_filter_check = builder.get_object("gender_filter_check")
        self.age_filter_check = builder.get_object("age_filter_check")

        self.liststore = Gtk.ListStore(str, str)
        self.treeview.set_model(self.liststore)

        renderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn("ID", renderer, text=0)
        self.treeview.append_column(column)

        renderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn("Nombre", renderer, text=1)
        self.treeview.append_column(column)

        self.add_button.connect("clicked", self.on_add_clicked)
        self.edit_button.connect("clicked", self.on_edit_clicked)
        self.delete_button.connect("clicked", self.on_delete_clicked)
        self.search_button.connect("clicked", self.on_search_clicked)
        self.gender_filter_check.connect("toggled", self.on_gender_filter_toggled)
        self.age_filter_check.connect("toggled", self.on_age_filter_toggled)

        self.window.connect("delete-event", Gtk.main_quit)
        self.window.show_all()

    def on_add_clicked(self, widget):
        pass

    def on_edit_clicked(self, widget):
        pass

    def on_delete_clicked(self, widget):
        pass

    def on_search_clicked(self, widget):
        pass

    def on_gender_filter_toggled(self, widget):
        pass

    def on_age_filter_toggled(self, widget):
        pass

if __name__ == "__main__":
    window = MainWindow()
    Gtk.main()
