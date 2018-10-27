import requests
import re
import os
import csv


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

vzorec = re.compile(
    r'<a href="/production/.*-(?P<time>\d?\d?\d?\d?-\d?\d?\d?\d?)?"'
    r'title="" data-cms-ai="0">(?:\n|\s)*(.*)(?:\n|\s)*</a>(?:\n|\s)*</td>'
    r'<td data-label="" class="col-2">(?:\n|\s)*(?P<venue>.*?)(?:\n|\s)*</td>'
    r'<td data-label="" class="col-3">(?:\n|\s)*(?P<genre>.*?)(?:\n|\s)*</td>'
    r'<td data-label="" class="col-4">(?:\n|\s)*(?P<location>.*?)(?:\n|\s)*</td>'
    r'<td data-label="" class="col-5">(?:\n|\s)*(?P<type>.*?)(?:\n|\s)*</td>',
    re.DOTALL
)

def izloci_podatke(ujemanje):
    podatki = []
    for expression in vzorec.finditer(ujemanje):
        podatki = expression.groupdict()
#    podatki['time'] = podatki['time'].strip()
#    podatki['show'] = podatki['show'].strip()
#    podatki['genre'] = podatki['genre'].strip()
#    podatki['location'] = podatki['location'].strip()
#    podatki['type'] = podatki['type'].strip()
    return podatki

def pridobi_slovar(directory, datoteka):
    '''Naredi slovar z časom, naslovom, žanrom, lokacijo in tipom predstave'''
    seznam = razdelitev(directory, datoteka)
    podatki_predstav = []
    for i in range(0, len(seznam)):
        podatki_predstav.append(izloci_podatke(seznam[i]))
    return podatki_predstav

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

zapisi_data_csv('podatki', 'podatki/broadway.html', 'broadway.csv')
#zapisi_data_csv('podatki', 'podatki/offbroadway.html', 'offbroadway.csv')
#zapisi_data_csv('podatki', 'podatki/london.html', 'london.csv')
#zapisi_data_csv('podatki', 'podatki/regional.html', 'regional.csv')
