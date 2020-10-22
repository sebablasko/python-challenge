from os import listdir
from os.path import isfile, join
import PyPDF2

"""
pdf_path:string > path al archivo PDF
"""
def pdf_to_text(pdf_path):
   text = ""
   with open(pdf_path, 'rb') as f:
      fileReader = PyPDF2.PdfFileReader(f)
      for i in range(fileReader.numPages):
         pageObj = fileReader.getPage(i)
         text = text + pageObj.extractText()
   return text

# El procesamiento de los pdf del directorio 'sociedades-pdf' opera correctamente
customPath = 'sociedades-pdf'
pdfFiles = [join(customPath, f) for f in listdir(customPath) if isfile(join(customPath, f))]
for f in pdfFiles:
   print(pdf_to_text(f))

# El procesamiento de los pdf del directorio 'sociedades-b-pdf' no opera correctamente.
# Sólo se recupera el texto de los encabezados o pies de página.
# Sospecho que esto es pues estos pdf se diferencian de los primeros en que están construidos por capas,
# luego, la librería que estoy usando sólo es capaz de procesar una de las capas y es ese el contenido
# que se muestra.
customPath = 'sociedades-b-pdf'
pdfFiles = [join(customPath, f) for f in listdir(customPath) if isfile(join(customPath, f))]
for f in pdfFiles:
   print(pdf_to_text(f))
