##Ahora tengo que hacer que uno de los 5 botones hechos con glade añada una nueva fila al treeview, que otro boton elimine, que otro boton suba y que otro boton la baje

#Para implementar las funciones de agregar, eliminar, subir y bajar filas en el TreeView usando Glade, primero se debe conectar cada botón a su señal correspondiente en el archivo .glade. Luego, se debe escribir el código que define lo que hace cada señal en Python. A continuación, se muestra un ejemplo de cómo se puede hacer esto:


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
        self.up_button = builder.get_object("up_button")
        self.down_button = builder.get_object("down_button")

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
        self.up_button.connect("clicked", self.on_up_clicked)
        self.down_button.connect("clicked", self.on_down_clicked)

        self.window.connect("delete-event", Gtk.main_quit)
        self.window.show_all()

    def on_add_clicked(self, widget):
        self.liststore.append(["Nuevo ID", "Nuevo nombre"])

    def on_edit_clicked(self, widget):
        selection = self.treeview.get_selection()
        model, iter_ = selection.get_selected()
        if iter_:
            dialog = Gtk.MessageDialog(self.window, 0, Gtk.MessageType.INFO,
                Gtk.ButtonsType.OK_CANCEL, "Editar entrada")
            dialog.format_secondary_text("Introduzca los nuevos valores:")
            dialog.add_buttons("Guardar", Gtk.ResponseType.OK, "Cancelar", Gtk.ResponseType.CANCEL)
            entry1 = Gtk.Entry()
            entry1.set_text(model[iter_][0])
            entry2 = Gtk.Entry()
            entry2.set_text(model[iter_][1])
            box = Gtk.Box(spacing=6)
            box.pack_start(Gtk.Label("ID:"), False, False, 0)
            box.pack_start(entry1, True, True, 0)
            box.pack_start(Gtk.Label("Nombre:"), False, False, 0)
            box.pack_start(entry2, True, True, 0)
            dialog.get_content_area().add(box)
            dialog.show_all()
            response = dialog.run()
            if response == Gtk.ResponseType.OK:
                model[iter_][0] = entry1.get_text()
                model[iter_][1] = entry2.get_text()
            dialog.destroy()

    def on_delete_clicked(self, widget):
        selection = self.treeview.get_selection()
        model, iter_ = selection.get_selected()
        if iter_:
            model.remove(iter_)

    def on_up_clicked(self, widget):
        selection = self.treeview.get_selection()
        model, iter_ = selection.get_selected()
        if iter_:
            index = model.get_path(iter_)[0]
            if index > 0:
                model.swap(model.get_iter)
