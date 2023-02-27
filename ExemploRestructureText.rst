Un paráfo en un Restructure text é o bloque mais basico e non necesitamos marcalo de ninguna maneira.

So tenemos que respetar a tabulación. Para remarcar utilizamos  *italica* cun só aterisco. Tenemos outras opcións como a **negriña** con dobre asterisco ou con dobre copmilla para codigo: `èste seria o tipo de texto``.

Para facer unha lista

*O primeiro elemento
*O segundo elemento

Este elemento usa mais dunha liña

    #. Lista autonumerada
    #. Segundo elemento

1. Primer Elemento
2. Segundo Elemento

Termin (na parte de arriba do texto)

    Definicion do termo, que ten que ser tabulado.

    Pode ter varios parrafos

Outro termo
    Definicion doutro termo

Este é un texto de `parrafo.O seguinte parragrafo é un exemplo de código::

    def funcionNumeroParametrosVariable(parametro1, parametro2, *outro):
        print(parametro1)
        print(parametro2)
        for parametro in outro:
            print(parametro)
    funcionNumeroParametrosVariable(1, 2, 3, 4, 5)

Xa continuamos con texto normal

>>> 1 + 1
2

===== ===== =======
A     B     A and B
===== ===== =======
False False False
True  False False
False True  False
True  True  True
===== ===== ======

+-----------------------------+----------------------------+----------------------------+-----------------------------+
| Filade cabeceira, columna1  | Cabeceira 2                | Cabeceira 3                | Cabeceira 4                 |
| Cabeceira Opcional          |                            |                            |                             |
+-----------------------------+----------------------------+----------------------------+-----------------------------+
