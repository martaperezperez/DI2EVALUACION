import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk
from conexionBD import ConexionBD

class TreeViewBD(Gtk.Window):
    def __init__(self):
        super().__init__(title="Exemplo TreeView CellRendererCombo")

        caixaV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=4)
        modelo = Gtk.ListStore(str,str,int,str)
        modeloPerfis = Gtk.ListStore(str,int)

        trvPerfilesUsuarios = Gtk.TreeView(model=modelo)

        celda = Gtk.CellRendererText()
        columna = Gtk.TreeViewColumn("DNI", celda, text=0)
        trvPerfilesUsuarios.append_column(columna)

        celda2 = Gtk.CellRendererText()
        columna2 = Gtk.TreeViewColumn("Nome", celda2, text=1)
        trvPerfilesUsuarios.append_column(columna2)

        celda3 = Gtk.CellRendererText()
        columna3 = Gtk.TreeViewColumn("Perfil ID", celda3, text=2)
        trvPerfilesUsuarios.append_column(columna3)

        celda4 = Gtk.CellRendererText()
        columna4 = Gtk.TreeViewColumn("Descripcion", celda4, text=3)
        trvPerfilesUsuarios.append_column(columna4)

        bd = ConexionBD("perfisUsuarios.bd")
        conectBD = bd.conectaBD()
        cursor = bd.creaCursor()
        sqlDniNome = "SELECT dni, nome FROM usuarios" # Consulta del dni y el nombre
        sqlPerfisUsuario = "SELECT idPerfil FROM perfisUsuario WHERE dniUsuario=?" #Consulta del id de perfil segun DNI
        sqlPerfis = "SELECT descricion FROM perfis WHERE idPefil=?" #Consulta de descricion de perfil segun id de perfil
        sqlTodosPerfis = "SELECT descricion, idPefil FROM perfis"

        lUsuarios = bd.consultaSenParametros(sqlDniNome)

        for usuario in lUsuarios:
            idPerfil = bd.consultaConParametros(sqlPerfisUsuario,usuario[0])
            descripcionPerfil = bd.consultaConParametros(sqlPerfis,idPerfil[0][0])
            elemento = list(usuario)
            elemento.append(idPerfil[0][0])
            elemento.append(descripcionPerfil[0][0])
            print(elemento)
            modelo.append(elemento)

        lTodosPerfis = bd.consultaSenParametros(sqlTodosPerfis)
        for perfil in lTodosPerfis:
            modeloPerfis.append(perfil)

        celda5 = Gtk.CellRendererCombo()
        celda5.set_property("editable",True)
        celda5.set_property("model", modeloPerfis)
        celda5.set_property("text-column", 0)
        celda5.set_property("has-entry",False)
        columna5 = Gtk.TreeViewColumn("Perfil", celda5, text=3)
        trvPerfilesUsuarios.append_column(columna5)

        caixaV.pack_start(trvPerfilesUsuarios,True,True,0)

        self.add(caixaV)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()

if __name__ == "__main__":
    TreeViewBD()
    Gtk.main()

