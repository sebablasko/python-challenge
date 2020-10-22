#!/usr/bin/python3

import os.path
import re

"""
pdf_path:string > path al archivo PDF
"""
def pdf_to_text(pdf_path):
   print('-- %s --' % os.path.split(pdf_path)[-1])
   with open(pdf_path, 'r') as f:
      for line in f:
         basePattern = r'(.*) comparece(.*).*'
         baseLocated = re.search(basePattern, line, re.M|re.I)
         if baseLocated:
            #print(baseLocated.group(2))
            personData = r'[\w ]*, Rut [\w.-]*'
            personDataLocated = re.findall(personData, baseLocated.group(2))
            for person in personDataLocated:
               [name, rut] = person.split(', Rut ')
               print(name, rut)


relativePath = 'sociedades-texto'
for f in os.listdir(relativePath):
   pdf_to_text('%s/%s' % (relativePath, f))
#pdf_to_text('sociedades-texto/AC0AV8Q7cIeH.txt')
#pdf_to_text('sociedades-texto/AC0J3roXRhPw.txt')