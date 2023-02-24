
from reportlab.pdfgen import canvas

texto = ['0 patio da miña casa', 'é particular', 'cando chove móllase', "como os demáis"]

aux = canvas.Canvas ('pdfTexto.pdf')

text = aux.beginText()
text.setTextOrigin(20,800)
## Fonte y tamaño
text.setFont("Courier", 12)
for linha in texto:
    text.textLine(linha)
text.setFillGray(0.5)

textoContinuo = '''Este é un texto multiliña
sod que se usan para marcar a socumentacion das
funcións en Python.
Esta forma de facer comentaros tamén nos permite
escribir varioas liñas de texto.
'''
text.textLines(textoContinuo)

for tipoLetra in aux.getAvailableFonts():
    ##Todos los tiposde letras
    text.textLine(tipoLetra)
 
for tipoLetra in aux.getAvailableFonts():
    text.setFont(tipoLetra,14)
    ##Te aparece el nombre y el tipo de letra
    text.textLine(tipoLetra + ': Este tipo de letra está dispoñible en reportLab')
    ##Desplazamento de x y de y
    text.moveCursor(20, 10)

## Poner el texto en color azul
text.setFillColorRGB(0 ,0 , 1)
text.setFont('Helvetica', 12)
text.textLine('Texto en cor azul')

aux.drawText(text)
aux.showPage()
aux.save()