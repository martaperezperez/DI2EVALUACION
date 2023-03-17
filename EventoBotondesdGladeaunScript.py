##como puedo conectar un evento de botón desde glade a un script de Python usando señales

#Para conectar un evento de botón en Glade a un script de Python usando señales, puedes seguir los siguientes pasos:

# 1-Abre el archivo .glade de la interfaz que estás trabajando.
# 2-Selecciona el botón al que deseas agregar la señal.
# 3-Haz clic en la pestaña "Señales" en el panel de propiedades del botón.
# 4-Haz clic en el botón "+" para agregar una nueva señal.
# 5-En el cuadro de diálogo "Editar señal", ingresa el nombre de la señal en el campo "Nombre" (por ejemplo, "on_button_clicked").
# 6-En el campo "Handler" ingresa el nombre de la función de Python que deseas llamar cuando se produzca la señal (por ejemplo, "on_button_clicked_handler").
# 7-Haz clic en el botón "Aceptar" para guardar los cambios y cerrar el cuadro de diálogo.
# 8-Guarda el archivo .glade.
#Luego, en tu script de Python, debes conectar la señal que agregaste en Glade a una función de Python. Para hacerlo, puedes usar el método connect de la instancia de Gtk.Builder que estás usando para cargar la interfaz desde el archivo .glade. Aquí te mostramos un ejemplo de cómo podrías hacerlo:

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Mi Interfaz Glade")
        self.builder = Gtk.Builder()
        self.builder.add_from_file("mi_interfaz.glade")
        self.builder.connect_signals(self)

        self.box_principal = self.builder.get_object("box_principal")
        self.button1 = self.builder.get_object("button1")

        self.add(self.box_principal)

    def on_button_clicked_handler(self, button):
        print("Se hizo clic en el botón")

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()


