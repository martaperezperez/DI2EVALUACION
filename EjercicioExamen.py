import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from conexionBD import ConexionBD


class App(Gtk.Window):

    def __init__(self):
        super().__init__(title="Example Treeview XellRendererCombo")

        v_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)

        model = Gtk.ListStore(str, str, int, str)
        perfil_model = Gtk.ListStore(str, str)

        trv_perfil_usuarios = Gtk.TreeView(model=model)

        cell = Gtk.CellRendererText()
        col = Gtk.TreeViewColumn("DNI", cell, text=0)
        trv_perfil_usuarios.append_column(col)

        cell2 = Gtk.CellRendererText()
        col2 = Gtk.TreeViewColumn("Nome", cell, text=1)
        trv_perfil_usuarios.append_column(col2)

        cell3 = Gtk.CellRendererText()
        col3 = Gtk.TreeViewColumn("Perfil", cell, text=3)
        trv_perfil_usuarios.append_column(col3)

        db = ConexionBD("perfisUsuarios.bd")
        conexionBD = db.conectaBD()
        cursor = db.creaCursor()

        # query = "SELECT u.dni, u.nome, pu.idPerfil FROM usuarios u join perfisUsuario pu on u.dni = pu.dniUsuario"

        query_m = "select dni, nome from usuarios"
        query_m2 = "select idPerfil from perfisUsuario where dniUsuario=?"
        query_m3 = "select descricion from perfis where idPefil=?"

        lista_usuarios = db.consultaSenParametros(query_m)
        usuarios_perfil = list()

        for usuario in lista_usuarios:
            id_pefil = db.consultaConParametros(query_m2, usuario[0])  # usuario[0] is dni
            desc = db.consultaConParametros(query_m3, id_pefil[0][0])  # id_pefil[0] is descricion
            element = list(usuario)
            element.append(id_pefil[0][0])
            element.append(desc[0][0])
            model.append(element)

        v_box.pack_start(trv_perfil_usuarios, True, True, 0)

        self.add(v_box)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()


if __name__ == "__main__":
    App()
    Gtk.main()
