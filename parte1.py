from datetime import datetime, timedelta
import urllib.request
from bs4 import BeautifulSoup

"""
path:string > path a la carpeta donde bajar los archivos
"""
def download_todays_constituciones(path):
   today = datetime.now().strftime('%d-%m-%Y')
   download_constituciones_by_date(path, today)

def download_constituciones_by_date(path, queriedDate):
   sourceUrl = 'https://www.diariooficial.interior.gob.cl/edicionelectronica/index.php?date=%s' % queriedDate
   page = urllib.request.urlopen(sourceUrl)
   soup = BeautifulSoup(page, 'html.parser')
   hasMultipleEditions = len(soup.findAll('a', href=True, text='Ver edición')) > 0
   if hasMultipleEditions:
      for link in soup.findAll('a', href=True, text='Ver edición'):
         queried = link['href'].split('edition=')[1]
         [edition, version] = queried.split("&v=")
         finalUrl = fullUrlBuilder(queriedDate, edition, version)
         extract_and_donwload_pdf(path, finalUrl)
   else:
      hasEdition = len(page.url.split('edition=')) > 1
      if hasEdition:
         edition = page.url.split('edition=')[1]
         finalUrl = fullUrlBuilder(queriedDate, edition)
         extract_and_donwload_pdf(path, finalUrl)
      else:
         print("nothing for %s" % queriedDate)

def fullUrlBuilder(queriedDate, edition = False, version = False):
   baseUrl = 'https://www.diariooficial.interior.gob.cl/edicionelectronica/empresas_cooperativas.php?date=%s' % queriedDate
   if edition:
      baseUrl = '%s&edition=%s' % (baseUrl, edition)
   if version:
      baseUrl = '%s&v=%s' % (baseUrl, version)
   return baseUrl

def extract_and_donwload_pdf(path, baseUrl):
   page = urllib.request.urlopen(baseUrl)
   soup = BeautifulSoup(page, 'html.parser')
   scanning = False
   for tr in soup.findAll('tr'):
      [firstTd, secondTd] = tr.findAll('td')
      if 'class' in firstTd.attrs and 'title3' in firstTd['class']:
         scanning = firstTd.text.strip() == 'CONSTITUCIÓN'
      if scanning:
         pdfLink = secondTd.find('a')
         if pdfLink:
            pdfName = pdfLink.text.replace('Ver PDF ', '').replace('(', '').replace(')', '')
            print(firstTd.text.strip(), pdfName, pdfLink['href'])
            urllib.request.urlretrieve(pdfLink['href'], '%s/%s.pdf' % (path, pdfName))

"""
path:string > path a la carpeta donde bajar los archivos
year:number > año a descargar (ej: 2019)
"""
def download_constituciones_from_year(year, path):
   queriedDate = datetime(year, 1, 1)
   while queriedDate.year == year:
      download_constituciones_by_date(path, queriedDate.strftime('%d-%m-%Y'))
      queriedDate = queriedDate + timedelta(days=1) 

download_todays_constituciones('pdfs_hoy')
#download_constituciones_from_year(2019, '.')

