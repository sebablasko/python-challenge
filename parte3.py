#!/usr/bin/python3

import os.path
import re

def print_owners():
   relative_path = 'sociedades-texto'
   for f in os.listdir(relative_path):
      extract_comparecientes('%s/%s' % (relative_path, f))

def extract_comparecientes(pdf_path):
   print('-- %s --' % os.path.split(pdf_path)[-1])
   with open(pdf_path, 'r') as f:
      for line in f:
         base_pattern = r'(.*) comparece(.*).*'
         base_located = re.search(base_pattern, line, re.M|re.I)
         if base_located:
            # print(base_located.group(2))
            person_data = r'[:;] [\w -]*, Rut [\w.-]*'
            person_data_located = re.findall(person_data, base_located.group(2))
            for person in person_data_located:
               [name, rut] = person.split(', Rut ')
               print(name[2:], rut)

print_owners()

# extract_comparecientes('sociedades-texto/AC3VyaUIVXBc.txt')