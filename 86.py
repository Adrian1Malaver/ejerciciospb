"""Escribir un programa que escriba la lista de caracteres ASCII dentro de un archivo de texto."""

from io import open

#creamos archivo de texto para escribir caracteres
archivo_texto=open("codigo_ascii.txt" , "w", encoding="utf-8")

#creamos iteracion caracteres ascii
for i in range(0, 255):
    
#escribimos cada caracter en el archivo
    archivo_texto.write(str(i)+"="+chr(i))
    
#cerramos archivo
archivo_texto.close()

"""OBSERVACION:
1.el encoding="utf-8", se usa para que todos los caracteres ascii puedan ser reconocidos
2.luego de haber ejecutado el programa, en bloc de notas presiona abrir y busca el nombre del archivo "codigo_ascii"
3.los caracteres ascii se muestran en otro idioma en el bloc de notas debido al encoding=utf-8"""
