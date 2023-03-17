import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MainWindow:
    def __init__(self):
        self.window = Gtk.Window()
        self.window.set_default_size(400, 300)
        self.window.connect("delete-event", Gtk.main_quit)

        vbox = Gtk.VBox()
        self.window.add(vbox)

        self.treeview = Gtk.TreeView()
        self.liststore = Gtk.ListStore(str, str)
        self.treeview.set_model(self.liststore)

        renderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn("ID", renderer, text=0)
        self.treeview.append_column(column)

        renderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn("Nombre", renderer, text=1)
        self.treeview.append_column(column)

        vbox.pack_start(self.treeview, True, True, 0)

        hbox = Gtk.HBox()
        vbox.pack_start(hbox, False, False, 0)

        add_button = Gtk.Button("Añadir")
        add_button.connect("clicked", self.on_add_clicked)
        hbox.pack_start(add_button, True, True, 0)

        edit_button = Gtk.Button("Editar")
        edit_button.connect("clicked", self.on_edit_clicked)
        hbox.pack_start(edit_button, True, True, 0)

        delete_button = Gtk.Button("Eliminar")
        delete_button.connect("clicked", self.on_delete_clicked)
        hbox.pack_start(delete_button, True, True, 0)

        up_button = Gtk.Button("Subir")
        up_button.connect("clicked", self.on_up_clicked)
        hbox.pack_start(up_button, True, True, 0)

        down_button = Gtk.Button("Bajar")
        down_button.connect("clicked", self.on_down_clicked)
        hbox.pack_start(down_button, True, True, 0)

        scale = Gtk.Scale(orientation=Gtk.Orientation.HORIZONTAL, adjustment=Gtk.Adjustment(0, 0, 100, 1, 10, 0))
        scale.connect("value-changed", self.on_scale_changed)
        vbox.pack_start(scale, False, False, 0)

        self.label = Gtk.Label()
        vbox.pack_start(self.label, False, False, 0)

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
                model[iter_][0]
                model[iter_][0] = entry1.get_text()
                model[iter_][1] = entry2.get_text()
            dialog.destroy()

    def on_delete_clicked(self, widget):
        selection = self.treeview.get_selection()
        model, iter_ = selection.get_selected()
        if iter_:
            self.liststore.remove(iter_)

    def on_up_clicked(self, widget):
        selection = self.treeview.get_selection()
        model, iter_ = selection.get_selected()
        if iter_:
            path = model.get_path(iter_)
            if path[0] > 0:
                prev_iter = model.get_iter(path.prev())
                model.swap(iter_, prev_iter)

    def on_down_clicked(self, widget):
        selection = self.treeview.get_selection()
        model, iter_ = selection.get_selected()
        if iter_:
            path = model.get_path(iter_)
            if path.next():
                next_iter = model.get_iter(path.next())
                model.swap(iter_, next_iter)

    def on_scale_changed(self, scale):
        value = scale.get_value()
        self.label.set_text("Posición: {}".format(value))

if __name__ == '__main__':
    window = MainWindow()
    Gtk.main()
