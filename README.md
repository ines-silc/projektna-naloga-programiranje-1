# Analiza gledaliških predstav in muziklov 

Avtor: Ines Šilc

Podatke bom črpala s strani:
 - http://www.playbill.com/
 - https://www.ibdb.com/
 - https://www.broadwayleague.com/home/

Zajeti podatki o posameznih predstavah: 
- `Mesec in leto začetka predstave`
- `Leto konca predstave`
- `Naslov predstave`
- `Prizorišče`
- `Zvrst`
- `Lokacija`
- `Vrsta predstave`
- `Število nastopov`

Zajeti statistični podatki o predstavah:
- `Sezona`
- `Bruto dobiček`
- `Obisk`
- `Skupna dolžina predstav`
- `Število novih predstav v sezoni`

Moj namen je analizirati predstave npr. katera predstava je trajala najdle, na katerih lokacijah je izvedenih največ predstav, katera predstava je imela največ izvedb, v katerih zveznih državah se izvaja največ predstav, katera sezona je bila najbolj profitabilna in ali imamo v vsaki sezoni uspešno predstavo, ki lahko traja več let.

Podatke imam zbrane v mapi `podatki`, v sedmih datotekah s končnico `.csv`. V isti mapi se nahajajo še pomožne datoteke za risanje zemljevida in originalne `.html` datoteke, ki vsebujejo surove podatke. Iz spletnih strani sem podatke izluščila s pomočjo regularnih izrazov, ta koda se nahaja v datoteki `zajem.py`. V datoteki `ureditev.py` se nahaja osnovno čiščenje podatkov, v datoteki `zemljevid.py` pa se nahaja koda za zemljevid, ki je vključen v poročilo.

Glavno poročilo se nahaja v datoteki `Analiza.ipynb`. Za prevod celotnega poročila so potrebni paketi: `pandas`, `matplotlib.pyplot`, `requests`, `re`, `os`, `csv`, `sys`, ter paketa `folium` in `warnings` za lep izpis zemljevida.
