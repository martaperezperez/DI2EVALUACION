from reportlab.pdfgen import canvas

aux = canvas.Canvas("documento.pdf")

aux.drawString(0, 0, "Posicion orixe(X, Y) = (0,0)")
aux.drawString(50, 100, "Posicion (X, Y) = (50,100)")
aux.drawString(150, 500, "Posiciom (X, Y) = (100,500)")

aux.drawImagen("/home/dam2a/Imágenes/Capturas de pantalla/DI.PNG", 700,300,225,225)

aux.showPage()
aux.save

