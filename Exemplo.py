
class Aplicacion:
     def __init__(self):
         builder = Gtk.Builder()
         builder.add_from_file("listatarefaTreeView.glade")


         wndfiestraPrincipal = builder.get_object("GtkWindow")
         self.tvwTarefas = builder.get_object("tvwTarefas")
         self.tvcTarefa = builder.get_object("tvcTarefa")
         self.tvcFeito = builder.get_object("tvcFaito")
         self.txtTarefa = builder.get_object("txtTarefa")
         self.btnEngadir = builder.get_object("btnEngadir")
         self.btnModificar = builder.get_object("btnEngadir")
         self.btnBorrar = builder.get_object("btnBorrar")

         #modeloLista = Gtk.ListaStore(str, bool)
         #self.tvwTarefas.set_model(modeloLista)

         sinais ={ "on_wndFiestraPrincipal_destroy": Gtk.main_quit,
                   "on_btnEngadior_clicked": self.on_btnEngadir_clicked,
                   "on_txtTarefa_activate": self.on_txtTarefa_activate,
                   "on_btnModificar_clicked": self.on_btnModificar_cliked,
                   "on_btnBorrar_cicker": self.onbtnBorrar_clickerd

         }

         builder.connect_signal(sinais)

         wndfiestraPrincipal.show_all()

         def on_btnEngadir_clicked(self, boton):
             self.engadirTarefa()



         def on_btnFeito_clicked(self, boton):
             seleccion = self.tvwTarefas.get_selection()
             modelo, fila = seleccion.get_selected()
             if fila is not None:
                 modelo.set(fila, (0,), (True,))
                 print(modelo[fila][0])

         def on_btnBorrar_clicked(self, boton):
             seleccion = self.tvwTarefas.get_selection()
             modelo, fila = seleccion.get_selected()
             if fila is not None:
                 modelo.remove(fila)




         def on_txtTarefa_activate(self, cadroTexto):
             self.engadirTarefa()

         def engadirTarefa(self):
             modelo = self.twtTarefas.get_model()
             print(self.txtTarefas.get_text())
             pos = modelo.append ((False, self.txtTarefa.get_text()))
             #modelo.set(pos,(0,1),(False, self.txtTarefa.get_text()))

             self.txtTarefa.set_text("")



     if __name__ == "__main__"




