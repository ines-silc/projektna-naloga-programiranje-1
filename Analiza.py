#!/usr/bin/env python
# coding: utf-8

# In[82]:


import pandas as pd
import matplotlib.pyplot as plt
import ureditev


# In[83]:


#BROADWAY
#Trenutno se izvajajo te predstave:
broadway_trenutno = broadway[broadway['time'].str.contains(r'\d{10}')]
#Napovedane so te predstave:
broadway_prihodnje = broadway[broadway['time'].str.contains(r'2018-2019')]
#Najpopularnejše gledališče:
broadway.venue.describe()
broadway[broadway.venue.str.contains('American Airlines Theatre')]


# In[84]:


#dobiček
bdobicek = broadway_statistika.plot(kind = 'line', x = 'year', y = 'gross')
#prisotnost
bprisotnost = broadway_statistika.plot(kind = 'line', x = 'year', y = 'attendance')
#nove produkcije
bnovo = broadway_statistika.plot(kind = 'line', x = 'year', y = 'newProductions')
broadway_statistika


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




