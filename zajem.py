import requests
import re
import os
import csv
import sys

def preberi_datoteko(directory, filename):
    '''Funkcija vzame datoteko in jo pretvori v niz'''
    with open(filename, encoding='utf-8') as datoteka:
        return datoteka.read()

def razdelitev(directory, datoteka):
    '''funkcija razdeli surov niz na podatke o posamezni predstavi'''
    vsebina = preberi_datoteko(directory, datoteka)
    match = []
    vzorec = r'<td data-label="" class="col-1">' + r'(\n|.)*?' + r'<td data-label="" class="col-6">'
    for ujemanje in re.finditer(vzorec, vsebina, re.DOTALL):
        ena_vrstica = ujemanje.group(0)
        match.append(ena_vrstica)
    return match

vzorec1 = re.compile(
    r'<a href="/production/.*-(?P<time>(?:(?:\d\d\d\d-\d\d\d\d)|(?:\d{10})))?"\s*'
#    r'(?:\w|")" data-cms-ai="0">\s*(?P<show>(?:\w|\'|\ |–|:|/|,)*?)\s*</a>\s*</td>'
#    r'<td data-label="" class="col-2">\s*(?P<venue>.*?)\s*</td>'
#    r'<td data-label="" class="col-3">\s*(?P<genre>.*?)\s*</td>\s*'
#    r'<td data-label="" class="col-4">\s*(?P<location>.*?)\s*</td>'
#    r'<td data-label="" class="col-5">\s*(?P<type>.*?)\s*</td>'
    )

def izloci_podatke(ujemanje):
    podatki = ujemanje.groupdict()
    podatki['time'] = podatki['time'].strip()
    podatki['show'] = podatki['show'].strip()
    podatki['genre'] = podatki['genre'].strip()
    podatki['location'] = podatki['location'].strip()
    podatki['type'] = podatki['type'].strip()
    return podatki

podatki_predstav = []

def pridobi_slovar(directory, datoteka):
    '''Naredi slovar z časom, naslovom, žanrom, lokacijo in tipom predstave'''
    seznam = razdelitev(directory, datoteka) 
    for predstava in seznam:
        for ujemanje in vzorec.finditer(predstava):
            podatki_predstav.append(izloci_podatke(ujemanje))
    return podatki_predstav

#with open('podatki/broadway.csv', 'w') as datoteka:
#    writer = csv.writer(datoteka)
#    writer.writerow(('time'))
#    for x in re.finditer(vzorec, preberi_datoteko('podatki', 'podatki/broadway.html'), re.DOTALL):
#        writer.writerow(x.group(1))


with open('podatki/broadway.csv', 'w') as datoteka:
    vzorec = r'<a href="/production/.*-(?P<time>(?:(?:\d\d\d\d-\d\d\d\d)|(?:\d{10})))?"\s*'+ '.*'+ r'(?:\w|")" data-cms-ai="0">\s*(?P<show>(?:\w|\'|\ |–|:|/|,)*?)\s*</a>\s*</td>\s*<td data-label="" class="col-2">\s*(?P<venue>.*?)\s*</td>\s*<td data-label="" class="col-3">\s*(?P<genre>.*?)\s*</td>\s*<td data-label="" class="col-4">\s*(?P<location>.*?)\s*</td>\s*<td data-label="" class="col-5">\s*(?P<type>.*?)\s*</td>'
    writer = csv.writer(datoteka)
    writer.writerow(['time', 'show', 'venue', 'genre', 'location', 'type'])
    for x in re.finditer(vzorec, preberi_datoteko('podatki', 'podatki/broadway.html')):
        writer.writerow([x.group(1), x.group(2), x.group(3), x.group(4), x.group(5), x.group(6)])

with open('podatki/offbroadway.csv', 'w') as datoteka:
    vzorec = r'<a href="/production/.*-(?P<time>(?:(?:\d\d\d\d-\d\d\d\d)|(?:\d{10})))?"\s*'+ '.*'+ r'(?:\w|")" data-cms-ai="0">\s*(?P<show>(?:\w|\'|\ |–|:|/|,)*?)\s*</a>\s*</td>\s*<td data-label="" class="col-2">\s*(?P<venue>.*?)\s*</td>\s*<td data-label="" class="col-3">\s*(?P<genre>.*?)\s*</td>\s*<td data-label="" class="col-4">\s*(?P<location>.*?)\s*</td>\s*<td data-label="" class="col-5">\s*(?P<type>.*?)\s*</td>'
    writer = csv.writer(datoteka)
    writer.writerow(['time', 'show', 'venue', 'genre', 'location', 'type'])
    for x in re.finditer(vzorec, preberi_datoteko('podatki', 'podatki/offbroadway.html')):
        writer.writerow([x.group(1), x.group(2), x.group(3), x.group(4), x.group(5), x.group(6)])

with open('podatki/regional.csv', 'w') as datoteka:
    vzorec = r'<a href="/production/.*-(?P<time>(?:(?:\d\d\d\d-\d\d\d\d)|(?:\d{10})))?"\s*'+ '.*'+ r'(?:\w|")" data-cms-ai="0">\s*(?P<show>(?:\w|\'|\ |–|:|/|,)*?)\s*</a>\s*</td>\s*<td data-label="" class="col-2">\s*(?P<venue>.*?)\s*</td>\s*<td data-label="" class="col-3">\s*(?P<genre>.*?)\s*</td>\s*<td data-label="" class="col-4">\s*(?P<location>.*?)\s*</td>\s*<td data-label="" class="col-5">\s*(?P<type>.*?)\s*</td>'
    writer = csv.writer(datoteka)
    writer.writerow(['time', 'show', 'venue', 'genre', 'location', 'type'])
    for x in re.finditer(vzorec, preberi_datoteko('podatki', 'podatki/regional.html')):
        writer.writerow([x.group(1), x.group(2), x.group(3), x.group(4), x.group(5), x.group(6)])

with open('podatki/london.csv', 'w') as datoteka:
    vzorec = r'<a href="/production/.*-(?P<time>(?:(?:\d\d\d\d-\d\d\d\d)|(?:\d{10})))?"\s*'+ '.*'+ r'(?:\w|")" data-cms-ai="0">\s*(?P<show>(?:\w|\'|\ |–|:|/|,)*?)\s*</a>\s*</td>\s*<td data-label="" class="col-2">\s*(?P<venue>.*?)\s*</td>\s*<td data-label="" class="col-3">\s*(?P<genre>.*?)\s*</td>\s*<td data-label="" class="col-4">\s*(?P<location>.*?)\s*</td>\s*<td data-label="" class="col-5">\s*(?P<type>.*?)\s*</td>'
    writer = csv.writer(datoteka)
    writer.writerow(['time', 'show', 'venue', 'genre', 'location', 'type'])
    for x in re.finditer(vzorec, preberi_datoteko('podatki', 'podatki/london.html')):
        writer.writerow([x.group(1), x.group(2), x.group(3), x.group(4), x.group(5), x.group(6)])

###############################################################################

def zapisi_csv(fieldnames, rows, directory, filename):
    '''Write a CSV file to directory/filename. The fieldnames must be a list of
    strings, the rows a list of dictionaries each mapping a fieldname to a
    cell-value.'''
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    with open(path, 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    return None

def zapisi_data_csv(directory, filename, csv):
    rows =  pridobi_slovar(directory, filename)
    fieldnames = ["time","show", "venue", "genre", "location", "type"]
    zapisi_csv(fieldnames, rows, directory, csv)

#zapisi_data_csv('podatki', 'podatki/broadway.html', 'broadway.csv')
#zapisi_data_csv('podatki', 'podatki/offbroadway.html', 'offbroadway.csv')
#zapisi_data_csv('podatki', 'podatki/london.html', 'london.csv')
#zapisi_data_csv('podatki', 'podatki/regional.html', 'regional.csv')
