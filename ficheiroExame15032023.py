import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from conexionBD import ConexionBD


class Exame(Gtk.Window):
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("ExamenDI.glade")

        Gtk.Window.__init__(self, title="Exame 15-04-2023")
        self.set_border_width(10)

        self.box = builder.get_object("box")
        self.frame = builder.get_object("frame")
        self.label = builder.get_object("label")
        self.box2 = builder.get_object("box2")
        self.box3 = builder.get_object("box3")
        self.labelDNI = builder.get_object("labelDNI")
        self.comboBox = builder.get_object("comboBox")
        self.box4 = builder.get_object("box4")
        self.labelNome = builder.get_object("labelNome")
        self.entry = builder.get_object("entry")

        boxinferior = Gtk.VBox()
        frmPerfis = Gtk.Frame(label="Perfís usuario")
        boxinferior.add(frmPerfis)
        trvPerfis = Gtk.TreeView()

        caixaVBotons = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)

        btnNovo = Gtk.Button(label="Novo")
        btnEditar = Gtk.Button(label="Editar")
        btnBorrar = Gtk.Button(label="Borrar")

        lblNomePerfil = Gtk.Label(label="Nome perfíl")
        txtNomePerfil = Gtk.Entry()
        lblDescripcionPerfil = Gtk.Label(label="Descripción")
        txtDescripcionPerfil = Gtk.Entry()
        lblPermisos = Gtk.Label(label="Permisos")
        cmbPermisos = Gtk.ComboBox()

        boxMain = Gtk.VBox()
        boxMain.add(self.box)
        boxMain.add(boxinferior)

        # bd = ConexionBD("perfisUsuarios.bd")
        # conectBD = bd.conectaBD()
        # cursor = bd.creaCursor()
        # sqlDni= "SELECT dni FROM usuarios"

        self.connect("delete-event", Gtk.main_quit)
        self.show_all()


if __name__ == "__main__":
    Exame()
    Gtk.main()
