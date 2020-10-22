# Desafío Legalbot

## Parte 1: Web Scraping

Utilicé `urllib.request` para las peticiones http y `BeautifulSoup` para el parseo y naavegación en el cuerpo http. Adjunto los pdf descargados y tambièn el còdigo del bonus.

Para los días que disponibilizaban más de una versión, se están inspeccionando todas las disponibles.

## Parte 2: Extracción de información

Utilicé `PyPDF2` para procesar los pdf y extraer el texto. Tal cual como indicaban no los convertí a imagen. Algunas notas que incluí en el archivo mismo de la solución respecto a las preguntas de esta parte:
- El procesamiento de los pdf del directorio 'sociedades-pdf' opera correctamente
- El procesamiento de los pdf del directorio 'sociedades-b-pdf' no opera correctamente. Sólo se recupera el texto de los encabezados o pies de página. Sospecho que esto es pues estos pdf se diferencian de los primeros en que están construidos por capas, luego, la librería que estoy usando sólo es capaz de procesar una de las capas y es ese el contenido que se muestra.

## Parte 3: Procesamiento de Lenguaje

Utilicé `re` para evaluación de expresiones regulares.

En archivos como:

- `AC2MEl0zlPQR.txt`
- `AC1C4BWIEJ0V.txt`
- `AC2Snj6m14ka.txt`
- `AC4fmEBOGWY1.txt`
- `AC5YCopU0Btz.txt`
- `AC0Dubcu9VxL.txt`
- `AC5HJF1StK8y.txt`
- `AC4aBjGYeT8m.txt`

mi script no consiguió lo pedido pues el archivo no respetaba la estructura indicada del tercer párrafo.
