import requests
import re
import os
import csv

###############################################################################
# Najprej definirajmo nekaj pomožnih orodij za pridobivanje podatkov s spleta.
###############################################################################

# mapa, v katero bomo shranili podatke
#data_directory = 'podatki'
# ime datoteke v katero bomo shranili glavno stran
#frontpage_filename = 'frontpage.html'
# ime CSV datoteke v katero bomo shranili podatke
#csv_filename = 'cat_data.csv'


def download_url_to_string(url):
    '''This function takes a URL as argument and tries to download it
    using requests. Upon success, it returns the page contents as string.'''
    try:
        # del kode, ki morda sproži napako
        r = requests.get(url)
    except requests.exceptions.ConnectionError:
        # koda, ki se izvede pri napaki
        print('stran'+ url + 'ne obstaja!')
        # dovolj je če izpišemo opozorilo in prekinemo izvajanje funkcije
        return 
    # nadaljujemo s kodo če ni prišlo do napake
    return r.text


def save_string_to_file(text, directory, filename):
    '''Write "text" to the file "filename" located in directory "directory",
    creating "directory" if necessary. If "directory" is the empty string, use
    the current directory.'''
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    with open(path, 'w', encoding='utf-8') as file_out:
        file_out.write(text)
    return None

# Definirajte funkcijo, ki prenese glavno stran in jo shrani v datoteko.


def save_frontpage(url, ime_datoteke):
    try:
        r = requests.get(url)
    except requests.exceptions.ConnectionError:
        print('stran ' + url + ' ne obstaja!')
    else:
        with open(ime_datoteke, 'w', encoding='utf-8') as datoteka:
            datoteka.write(r.text)
            print('shranjeno!')

###############################################################################
# Po pridobitvi podatkov jih želimo obdelati.
###############################################################################


def read_file_to_string(directory, filename):
    '''Return the contents of the file "directory"/"filename" as a string.'''
    with open(filename, encoding='utf-8') as datoteka:
        return datoteka.read()


# Definirajte funkcijo, ki sprejme niz, ki predstavlja vsebino spletne strani,
# in ga razdeli na dele, kjer vsak del predstavlja en oglas. To storite s
# pomočjo regularnih izrazov, ki označujejo začetek in konec posameznega
# oglasa. Funkcija naj vrne seznam nizov.

#Primer vrstice:
#<td data-label="" class="col-1">
#<a href="/production/act-s-of-god-lookingglass-theatre-company-2018-2019" title="" data-cms-ai="0">
#Act(s) of God</a></td>
#<td data-label="" class="col-2">Lookingglass Theatre Company</td>
#<td data-label="" class="col-3">Play</td>
#<td data-label="" class="col-4">Chicago, IL</td>
#<td data-label="" class="col-5">Regional/ National Tours</td>
#<td data-label="" class="col-6"></td>
#</tr><tr class="row-9">

vzorec_vrstice = re.compile(
    r'<td data-label="" class="col-1">.*<td data-label="" class="col-6">',
    re.DOTALL)

def page_to_ads(directory, datoteka):
#razdelimo po vrsticah
    vsebina = read_file_to_string(directory, datoteka)
    match = []
    vzorec = vzorec_vrstice
    for ujemanje in re.finditer(vzorec_podatkov, vsebina, re.DOTALL):
        nas_oglas = ujemanje.group(0)
        match.append(nas_oglas)
    return match


# Definirajte funkcijo, ki sprejme niz, ki predstavlja oglas, in izlušči
# podatke o imenu, ceni in opisu v oglasu.

vzorec_podatkov = re.compile(
    r'<a href="\/production\/.*-(?P<time>\d?\d?\d?\d?-\d?\d?\d?\d?)?"'
    r'title="" data-cms-ai="0">(?P<show>.*?)<\/a><\/td>'
    r'<td data-label="" class="col-2">(?P<venue>.*?)<\/td>'
    r'<td data-label="" class="col-3">(?P<genre>.*?)<\/td>'
    r'<td data-label="" class="col-4">(?P<location>.*?)<\/td>'
    r'<td data-label="" class="col-5">(?P<type>.*?)<\/td>',
    re.DOTALL
)

def izloci_podatke(ujemanje):
    podatki = ujemanje.groupdict()
    podatki['time'] = podatki['time'].strip()
    podatki['show'] = podatki['show'].strip()
    podatki['genre'] = podatki['genre'].strip()
    podatki['location'] = podatki['location'].strip()
    podatki['type'] = podatki['type'].strip()
    return podatki

podatki_oglasov = []
#to bo seznam slovarjev

def get_dict_from_ad_block(directory, datoteka):
    '''Build a dictionary containing the name, description and price
    of an ad block.'''
    seznam = page_to_ads(directory, datoteka)
    for oglas in seznam:
        for ujemanje in vzorec_podatkov.finditer(oglas):
            podatki_oglasov.append(izloci_podatke_oglasa(ujemanje))
    return podatki_oglasov


# Definirajte funkcijo, ki sprejme ime in lokacijo datoteke, ki vsebuje
# besedilo spletne strani, in vrne seznam slovarjev, ki vsebujejo podatke o
# vseh oglasih strani.


def ads_from_file(directory, filename):
    '''Parse the ads in filename/directory into a dictionary list.'''
    oglasi = get_dict_from_ad_block(directory, filename)
    return oglasi


###############################################################################
# Obdelane podatke želimo sedaj shraniti.
###############################################################################


def write_csv(fieldnames, rows, directory, filename):
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

# Definirajte funkcijo, ki sprejme neprazen seznam slovarjev, ki predstavljajo
# podatke iz oglasa mačke, in zapiše vse podatke v csv datoteko. Imena za
# stolpce [fieldnames] pridobite iz slovarjev.


def write_data_csv(directory, filename, csv):
    rows =  ads_from_file(directory, filename)
    fieldnames = ["time","show", "venue", "genre", "location", "type"]
    write_csv(fieldnames, rows, directory, csv)

write_data_csv('podatki', 'podatki/broadway.html', 'broadway.csv')
write_data_csv('podatki', 'podatki/offbroadway.html', 'offbroadway.csv')
write_data_csv('podatki', 'podatki/london.html', 'london.csv')
write_data_csv('podatki', 'podatki/regional.html', 'regional.csv')
