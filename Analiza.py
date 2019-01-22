#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import ureditev as u


# V tej nalogi je moj namen analizirati predstave, ki se izvajajo na odrih ulice Broadway in predstave po ostalih zveznih državah Združenih držav Amerike. Moj namen je analizirati predstave npr. katera predstava je trajala najdle, na katerih lokacijah je izvedenih največ predstav, katera predstava je imela največ izvedb, v katerih zveznih državah se izvaja največ predstav, katera sezona je bila najbolj profitabilna in ali imamo v vsaki sezoni uspešno predstavo, ki lahko traja več let.

# In[2]:


#BROADWAY
#Trenutno se izvajajo te predstave:
broadway_trenutno = u.broadway[u.broadway['time'].str.contains(r'\d{10}')]

#Napovedane so te predstave:
broadway_prihodnje = u.broadway[u.broadway['time'].str.contains(r'2018-2019')]
#Najpopularnejše gledališče:
u.broadway.venue.describe()
u.broadway[u.broadway.venue.str.contains('American Airlines Theatre')]

broadway_trenutno.head()
broadway_prihodnje.head()
u.broadway[u.broadway.venue.str.contains('American Airlines Theatre')]


# Trenutno se na Broadwayu izvaja 11 predstav, za naslednje leto pa jih je napovedanih 26. Najpopularnejše gledališče je american Airlines Theatre, v katerem se v sezoni 2018-2019 izvajajo 3 predstave.

# Spodnja tabela in grafi prikazujejo podatke o predstavah na Broadway odru od leta 1984. Stoplci po vrsti prikazujejo bruto dobiček v milijonih ameriških dolarjev, število obiskovalcev v milijonih, sama produktivnost predstav in število novih predstav v vsakem letu. Produktivnost predstav se meri v tednih, predstavlja vsoto vseh tednov, kadar so se predstave izvajale. Kot pričakovano dobiček in število obiskovalcev skozi leta narašča, medtem ko graf produktivnost in število novih predstav nima posebnih značilnosti, le da je leta 2000 drastično upadlo, medtem ko se to ni poznalo pri dobičku ali obisku predstav.

# In[5]:


#dobiček
bdobicek = u.broadway_statistika.plot(kind = 'line', x = 'year', y = 'gross')
#prisotnost
bprisotnost = u.broadway_statistika.plot(kind = 'line', x = 'year', y = 'attendance')
#nove produkcije
bnovo = u.broadway_statistika.plot(kind = 'line', x = 'year', y = 'newProductions')
#produktivnost
#bduration = u.broadway_statistika.plot(kind = 'line', x = 'year', y = 'duration')
u.broadway_statistika.head()


# Spodnja tabela in grafi prikazujejo enake karakteristike kot zgornja, le da tu opazujemo predstave po celotni državi ZDA. Dobiček skozi leta narašča, upade na prelomu tisočletja in leta 2017 doseže vrh. Sama prisotnost narašče v zgodnjih in poznih devetdesetih, okoli leta 2008 in leta 2017, medtem ko v letu 2000 doseže oster padec.

# In[4]:


#dobiček
rdobicek = u.regional_statistika.plot(kind = 'line', x = 'year', y = 'gross')
#prisotnost
rprisotnost = u.regional_statistika.plot(kind = 'line', x = 'year', y = 'attendance')
u.regional_statistika.head()


# Poglejmo si natančnejše podatke o predstavah od leta 1800 naprej. Spodnji graf prikazuje število izvedb vseh predstav vsakega leta. Podatke imammo za več kot 7000 predstav. Predstava, ki je trajala najdlje, je imela naslov *Cats*, ki se je izvajala kar 18 let. Slednja je imela tudi največ nastopov v teh 18 letih, teh nastopov je bilo kar 7485. Najmanj nastopov pa je imela predstava z naslovom *Hamlet*, za katero nimamo podatkov o številu nastopov.
# 
# Spodnji graf prikazuje število nastopov skozi leta, vidimo da je bilo največ predstav izvajanih v tridesetih in štiridesetih letih 19. stoletja, od takrat pa se število zmanjšuje.

# In[13]:


u.vsi['duration'] = u.vsi.c_year-u.vsi.o_year
nastopi = u.vsi[['o_year', 'performances']]
nastopi = nastopi.groupby(['o_year']).count()
gnastopi = nastopi.plot(kind = 'line', figsize=(20, 8))
tipi = u.vsi[['o_year', 'type']]
u.vsi.head()

print('Najdlje trajajoča predstava \n', u.vsi.loc[u.vsi['duration'].idxmax()])
print('\n')
print('Največ nastopov je imela predstava \n', u.vsi.loc[u.vsi['performances'].idxmax()])
print('\n')
print('Najmanj nastopov je imela predstava \n', u.vsi.loc[u.vsi['performances'].idxmin()])


# Predstave se predvajajo različno dolgo, odvisno od priljubljenosti. Spodnji graf prikazuje število let, v katerih se bo še predvajala najuspešnejša predstava vsakega leta. Vidimo, da se dolžina najdaljše predstave razlikuje med leti, torej če imamo neko leto že zelo uspešno predstavo, je zelo malo verjetno, da bomo v letu ki sledi, dobili prav tako uspešno predstavo.

# In[9]:


dolzine = u.vsi[['o_year', 'duration']]
dolzine = dolzine.groupby(['o_year']).max()
gdolzine = dolzine.plot(kind = 'line', figsize=(20, 8))


# Poglejmo še mesece, v katerih se pogosto začenjajo predstave. Pričakujemo, da bodo meseci, v katerih se je začelo največ predstav, meseci proti koncu leta, saj predstave, ki se začnejo prevajati proti koncu leta pričakujejo večji obisk zaradi božičnih praznikov. V začetku februarja izidejo tudi nominacije za najprestižnejše nagrade v gledališkem krogu (Tony awards), kjer so največkrat nagrajene predstave, ki so se začele po poletju.

# In[10]:


mesec = u.vsi[['o_month']]
meseci = mesec.groupby('o_month')['o_month'].count()
meseci = meseci.reindex(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

print(meseci)
gmeseci = meseci.plot(kind = 'bar')


# Poleg glavnega odra v New Yorku, se v Združenih državah Amerike pogosto tudi po ostalih zveznih državah. Spodnji zemljevid prikazuje število predstav, ki se izvajajo v sezoni 2018-2019 po zveznih državah ZDA. Največ predstav zabeležimo v državi *California*, sledita *Florida* in *Texas*.

# In[11]:


import zemljevid
zemljevid.m


# Po zveznih državah je bila najpogosteje izvajana predstava *Finding Neverland*.

# In[29]:


u.regional.describe()


# ### Zaključek
# 
# Kot pričakovano sam dobiček predstav na vseh odrih po Združenih država narašča, medtem ko obisk predstav lahko kakšno leto upade. Največ predstav na odru Broadway se je izvajalo v tridesetih letih prejšnjega stoletja, od takrat pa število novih predstav upada. Največ predstav izven New Yorka pa se izvaja v zvezni državi *California*. Najdlje trajajoča predstava je bila *Cats*, ki se je izvajala 18 let, in sicer od leta 1982 do leta 2000.
