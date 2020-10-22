#!/usr/bin/python3

from os import listdir
from os.path import isfile, join
import PyPDF2

"""
pdf_path:string > path al archivo PDF
"""
def pdf_to_text(pdf_path):
   text = ""
   with open(pdf_path, 'rb') as f:
      file_reader = PyPDF2.PdfFileReader(f)
      for i in range(file_reader.numPages):
         page_obj = file_reader.getPage(i)
         text = text + page_obj.extractText()
   return text

# El procesamiento de los pdf del directorio 'sociedades-pdf' opera correctamente
custom_path = 'sociedades-pdf'
pdf_files = [join(custom_path, f) for f in listdir(custom_path) if isfile(join(custom_path, f))]
for f in pdf_files:
   print(pdf_to_text(f))

# El procesamiento de los pdf del directorio 'sociedades-b-pdf' no opera correctamente.
# Sólo se recupera el texto de los encabezados o pies de página.
# Sospecho que esto es pues estos pdf se diferencian de los primeros en que están construidos por capas,
# luego, la librería que estoy usando sólo es capaz de procesar una de las capas y es ese el contenido
# que se muestra.
custom_path = 'sociedades-b-pdf'
pdf_files = [join(custom_path, f) for f in listdir(custom_path) if isfile(join(custom_path, f))]
for f in pdf_files:
   print(pdf_to_text(f))
