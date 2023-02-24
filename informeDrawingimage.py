

from reportlab.graphics.shapes import Image, Drawing
from reportlab.graphics import renderPDF
from reportlab.lib.pagesizes import A4

operacions = []

imaxe = Image (0, 0, 500, 102, "/home/dam2a/Imágenes/Capturas de pantalla/DI.png")

debuxo = Drawing (30,30)
debuxo.add(imaxe)
debuxo.translate(0, 700)

operacions.append(debuxo)

debuxo2 = Drawing(30,30)
debuxo2.add(imaxe)
debuxo2.rotate(30)
debuxo2.scale(0.5,1.5)
operacions.append(debuxo2)

debuxoF = Drawing(A4[0], A4[1])
for imaxe in operacions:
    debuxoF.add(imaxe)


renderPDF.drawToFile(debuxoF, "documentoLogo.pdf")