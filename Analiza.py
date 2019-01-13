#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd
import matplotlib.pyplot as plt
import ureditev as u


# V tej nalogi je moj namen analizirati predstave, ki se izvajajo na odrih ulice Broadway, predstave po ostalih zveznih državah Združenih držav Americe in Londona.

# In[20]:


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

# Spodnja tabela prikazuje podatke o predstavah na Broadway odru od leta 1984. Stoplci po vrsti prikazujejo bruto dobiček v milijonih ameriških dolarjev, število obiskovalcev v milijonih, sama produktivnost predstav in število novih predstav v vsakem letu. Produktivnost predstav se meri v tednih, predstavlja vsoto vseh tednov, kadar so se predstave izvajale. Kot pričakovano dobiček in število obiskovalcev skozi leta narašča, medtem ko graf produktivnost in število novih predstav nima posebnih značilnosti.

# In[21]:


#dobiček
bdobicek = u.broadway_statistika.plot(kind = 'line', x = 'year', y = 'gross')
#prisotnost
bprisotnost = u.broadway_statistika.plot(kind = 'line', x = 'year', y = 'attendance')
#nove produkcije
bnovo = u.broadway_statistika.plot(kind = 'line', x = 'year', y = 'newProductions')
#produktivnost
#bduration = u.broadway_statistika.plot(kind = 'line', x = 'year', y = 'duration')
u.broadway_statistika.head()


# In[85]:


#dobiček
rdobicek = regional_statistika.plot(kind = 'line', x = 'year', y = 'gross')
#prisotnost
rprisotnost = regional_statistika.plot(kind = 'line', x = 'year', y = 'attendance')
regional_statistika


# In[89]:


vsi['duration'] = vsi.c_year-vsi.o_year
nastopi = vsi[['o_year', 'performances']]
nastopi = nastopi.groupby(['o_year']).count()
gnastopi = nastopi.plot(kind = 'line', figsize=(20, 8))


dolzine = vsi[['o_year', 'duration']]
dolzine = dolzine.groupby(['o_year']).max()
gdolzine = dolzine.plot(kind = 'line', figsize=(20, 8))

tipi = vsi[['o_year', 'type']]
#tipi = tipi.pivot_table(index='o_year', columns='type',aggfunc='count')

#tipi = tipi.groupby(['o_year', 'type']).sum().sum(level=['o_year', 'type']).unstack('type')
##############################################33
#gtipi = tipi.plot.bar(stacked = True)

vsi


# In[87]:


import zemljevid
zemljevid.m


# In[ ]:




