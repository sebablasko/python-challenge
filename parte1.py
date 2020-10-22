#!/usr/bin/python3

from datetime import datetime, timedelta
import urllib.request
from bs4 import BeautifulSoup

"""
path:string > path a la carpeta donde bajar los archivos
"""
def download_todays_constituciones(path):
   today = datetime.now().strftime('%d-%m-%Y')
   download_constituciones_by_date(path, today)

def download_constituciones_by_date(path, queried_date):
   source_url = 'https://www.diariooficial.interior.gob.cl/edicionelectronica/index.php?date=%s' % queried_date
   page = urllib.request.urlopen(source_url)
   soup = BeautifulSoup(page, 'html.parser')
   has_multiple_editions = len(soup.findAll('a', href=True, text='Ver edición')) > 0
   if has_multiple_editions:
      for link in soup.findAll('a', href=True, text='Ver edición'):
         queried = link['href'].split('edition=')[1]
         [edition, version] = queried.split("&v=")
         final_url = full_url_builder(queried_date, edition, version)
         locate_and_donwload_pdfs(path, final_url)
   else:
      hasEdition = len(page.url.split('edition=')) > 1
      if hasEdition:
         edition = page.url.split('edition=')[1]
         final_url = full_url_builder(queried_date, edition)
         locate_and_donwload_pdfs(path, final_url)
      else:
         print("nothing for %s" % queried_date)

def full_url_builder(queried_date, edition = False, version = False):
   base_url = 'https://www.diariooficial.interior.gob.cl/edicionelectronica/empresas_cooperativas.php?date=%s' % queried_date
   if edition:
      base_url = '%s&edition=%s' % (base_url, edition)
   if version:
      base_url = '%s&v=%s' % (base_url, version)
   return base_url

def locate_and_donwload_pdfs(path, base_url):
   page = urllib.request.urlopen(base_url)
   soup = BeautifulSoup(page, 'html.parser')
   scanning = False
   for tr in soup.findAll('tr'):
      [first_td, second_td] = tr.findAll('td')
      if 'class' in first_td.attrs and 'title3' in first_td['class']:
         scanning = first_td.text.strip() == 'CONSTITUCIÓN'
      if scanning:
         pdfLink = second_td.find('a')
         if pdfLink:
            pdfName = pdfLink.text.replace('Ver PDF ', '').replace('(', '').replace(')', '')
            # print(first_td.text.strip(), pdfName, pdfLink['href'])
            urllib.request.urlretrieve(pdfLink['href'], '%s/%s.pdf' % (path, pdfName))

"""
path:string > path a la carpeta donde bajar los archivos
year:number > año a descargar (ej: 2019)
"""
def download_constituciones_from_year(year, path):
   queried_date = datetime(year, 1, 1)
   while queried_date.year == year:
      download_constituciones_by_date(path, queried_date.strftime('%d-%m-%Y'))
      queried_date = queried_date + timedelta(days=1) 

download_todays_constituciones('pdfs_hoy')
#download_constituciones_from_year(2019, '.')

