import requests
import re
import os
import csv
import sys

def pripravi_imenik(ime_datoteke):
    '''Če še ne obstaja, pripravi prazen imenik za dano datoteko.'''
    imenik = os.path.dirname(ime_datoteke)
    if imenik:
        os.makedirs(imenik, exist_ok=True)

def shrani_spletno_stran(url, ime_datoteke, kodiranje, vsili_prenos=False):
    '''Vsebino strani na danem naslovu shrani v datoteko z danim imenom.'''
    try:
        print('Shranjujem {} ...'.format(url), end='')
        sys.stdout.flush()
        if os.path.isfile(ime_datoteke) and not vsili_prenos:
            print('shranjeno že od prej!')
            return
        r = requests.get(url)
    except requests.exceptions.ConnectionError:
        print('stran ne obstaja!')
    else:
        pripravi_imenik(ime_datoteke)
        with open(ime_datoteke, 'w', encoding=kodiranje) as datoteka:
            datoteka.write(r.text)
            print('shranjeno!')



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

def izloci_podatke(ujemanje):
    podatki = ujemanje.groupdict()
    podatki['time'] = podatki['time'].strip()
    podatki['show'] = podatki['show'].strip()
    podatki['genre'] = podatki['genre'].strip()
    podatki['location'] = podatki['location'].strip()
    podatki['type'] = podatki['type'].strip()
    return podatki

shrani_spletno_stran("http://www.playbill.com/productions?q=&venue-type=offbroadway&state=all&genre=all", 'podatki/offbroadway.html', 'unicode_internal')

with open('podatki/broadway.csv', 'w') as datoteka:
    vzorec = r'<a href="/production/.*-(?P<time>(?:(?:\d\d\d\d-\d\d\d\d)|(?:\d{10})))?"\s*.*(?:\w|")" data-cms-ai="0">\s*(?P<show>(?:\w|\'|\ |–|:|/|,)*?)\s*</a>\s*</td>\s*<td data-label="" class="col-2">\s*(?P<venue>.*?)\s*</td>\s*<td data-label="" class="col-3">\s*(?P<genre>.*?)\s*</td>\s*<td data-label="" class="col-4">\s*(?P<location>.*?)\s*</td>\s*<td data-label="" class="col-5">\s*(?P<type>.*?)\s*</td>'
    writer = csv.writer(datoteka)
    writer.writerow(['time', 'show', 'venue', 'genre', 'location', 'type'])
    for x in re.finditer(vzorec, preberi_datoteko('podatki', 'podatki/broadway.html')):
        writer.writerow([x.group(1), x.group(2), x.group(3), x.group(4), x.group(5), x.group(6)])


with open('podatki/offbroadway.csv', 'w') as datoteka:
    vzorec = '<a  href="/production/.*-(?P<leto>(?:\d\d\d\d-\d\d\d\d)|(?:\d{10}))" title data-cms-ai="0" >\s*(?P<show>(?:\w|\'|\ |–|:|/|,)*)\s*</a>\s*</td>\s*<td data-label="" class="col-2">\s*(?P<venue>.*)\s*</td>\s*<td data-label="" class="col-3">\s*(?P<genre>.*)\s*</td>\s*<td data-label="" class="col-4">\s*(?P<location>.*)\s*</td>\s*<td data-label="" class="col-5">\s*(?P<type>.*)\s*</td>'
    writer = csv.writer(datoteka)
    writer.writerow(['time', 'show', 'venue', 'genre', 'location', 'type'])
    for x in re.finditer(vzorec, preberi_datoteko('podatki', 'podatki/offbroadway.html')):
        writer.writerow([x.group(1), x.group(2), x.group(3), x.group(4), x.group(5), x.group(6)])


with open('podatki/regional.csv', 'w') as datoteka:
    vzorec = r'<a href="/production/.*-(?P<time>(?:(?:\d\d\d\d-\d\d\d\d)|(?:\d{10})))?" title=""(?: data-cms-ai="0">|><span class="data-value">)\s*(?P<show>(?:\w|\'|\ |–|:|/|,)*?)\s*(?:</a>|</span></a>)\s*</td>\s*<td (?:ss="")? data-label=".*" class="col-2">(?:\s*<span class="data-value">)?\s*(?P<venue>.*?)\s*(?:</span>?\s*</td>|</td>)\s*<td(?: ss="")? data-label=".*" class="col-3">(?:\s*<span class="data-value">)?\s*(?P<genre>.*?)(?:\s*</span>)?\s*</td>\s*<td(?: ss="")? data-label="\w*" class="col-4">\s*(?P<location>.*?)\s*</td>\s*<td(?: ss="")? data-label=".*" class="col-5">\s*(?:\s*<span class="data-value">)*(?P<type>.*?)\s*(?:</span>)?\s*</td>'
    writer = csv.writer(datoteka)
    writer.writerow(['time', 'show', 'venue', 'genre', 'location', 'type'])
    for x in re.finditer(vzorec, preberi_datoteko('podatki', 'podatki/regional.html')):
        writer.writerow([x.group(1), x.group(2), x.group(3), x.group(4), x.group(5), x.group(6)])


with open('podatki/london.csv', 'w') as datoteka:
    vzorec = r'<a href="/production/.*-(?P<time>(?:(?:\d\d\d\d-\d\d\d\d)|(?:\d{10})))?"\s*.*(?:\w|")" data-cms-ai="0">\s*(?P<show>(?:\w|\'|\ |–|:|/|,)*?)\s*</a>\s*</td>\s*<td data-label="" class="col-2">\s*(?P<venue>.*?)\s*</td>\s*<td data-label="" class="col-3">\s*(?P<genre>.*?)\s*</td>\s*<td data-label="" class="col-4">\s*(?P<location>.*?)\s*</td>\s*<td data-label="" class="col-5">\s*(?P<type>.*?)\s*</td>'
    writer = csv.writer(datoteka)
    writer.writerow(['time', 'show', 'venue', 'genre', 'location', 'type'])
    for x in re.finditer(vzorec, preberi_datoteko('podatki', 'podatki/london.html')):
        writer.writerow([x.group(1), x.group(2), x.group(3), x.group(4), x.group(5), x.group(6)])


shrani_spletno_stran('https://www.broadwayleague.com/research/statistics-broadway-nyc/', 'podatki/broadway_statistika.html', 'utf-8')

with open('podatki/broadway_statistika.csv', 'w', encoding = 'utf-8') as datoteka:
    vzorec = r'<td>(?P<Season>(?:\d\d\d\d-\d\d)).*</td>\s*<td>\$(?P<Gross>(?:\d,\d\d\d)|(?:\d\d\d))</td>\s*<td>(?P<Attendance>\d*\.?\d*)</td>\s*<td>(?P<Playing_Weeks>(?:\d,\d\d\d)|(?:\d\d\d))</td>\s*<td>(?P<New_Productions>(?:\d+))</td>'
    writer = csv.writer(datoteka)
    writer.writerow(['season', 'gross', 'attendance', 'duration', 'newProductions'])
    for x in re.finditer(vzorec, preberi_datoteko('podatki', 'podatki/broadway_statistika.html')):
        writer.writerow([x.group(1), x.group(2), x.group(3), x.group(4), x.group(5)])


shrani_spletno_stran('https://www.broadwayleague.com/research/statistics-touring-broadway/', 'podatki/regional_statistika.html', 'utf-8')

with open('podatki/regional_statistika.csv', 'w', encoding = 'utf-8') as datoteka:
    vzorec = r'<td>(?P<Season>(?:\d\d\d\d-\d\d)).*</td>\s*<td>\$?(?P<Gross>(?:\d,\d\d\d)|(?:\d\d\d))</td>\s*<td>(?P<Attendance>(?:\d*\.?\d*))</td>\s*<td>(?P<Playing_Weeks>(?:\d,\d\d\d)|(?:\d\d\d))</td>'
    writer = csv.writer(datoteka)
    writer.writerow(['season', 'gross', 'attendance', 'duration'])
    for x in re.finditer(vzorec, preberi_datoteko('podatki', 'podatki/regional_statistika.html')):
        writer.writerow([x.group(1), x.group(2), x.group(3), x.group(4)])

shrani_spletno_stran('https://www.ibdb.com/shows', 'podatki/all_shows.html', 'utf-8')

with open('podatki/all_shows.csv', 'w', encoding = 'utf-8') as datoteka:
    vzorec = r'<li>\s*<a href="/broadway.production/(?:\w|-)*">(?P<show>.*)</a> \[(?P<type>\w*)\] <br />\s*(?P<genre>\w*,?\s*\w*)<br />\s*Opening: (?P<opening>.*)<br />\s*Closing: (?P<closing>.*)<br />\s*(?:Performance Count: (?P<performances>\d*)\s*<br />)'
    writer = csv.writer(datoteka)
    writer.writerow(['show', 'type', 'genre', 'opening', 'closing', 'performances'])
    for x in re.finditer(vzorec, preberi_datoteko('podatki', 'podatki/all_shows.html')):
        writer.writerow([x.group(1), x.group(2), x.group(3), x.group(4), x.group(5), x.group(6)])
