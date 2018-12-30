#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib as plt

broadway = pd.read_csv('podatki/broadway.csv', encoding = 'cp1252')
offbroadway = pd.read_csv('podatki/offbroadway.csv', encoding = 'cp1252')
regional = pd.read_csv('podatki/regional.csv', encoding = 'cp1252')
london = pd.read_csv('podatki/london.csv', encoding = 'cp1252')


# In[3]:


#BROADWAY
#Trenutno se izvajajo te predstave:
broadway_trenutno = broadway[broadway['time'].str.contains(r'\d{10}')]
#Napovedane so te predstave:
broadway_prihodnje = broadway[broadway['time'].str.contains(r'2018-2019')]
#Najpopularnejše gledališče:
broadway.venue.describe()
broadway[broadway.venue.str.contains('American Airlines Theatre')]


# In[20]:


broadway_statistika = pd.read_csv('podatki/broadway_statistika.csv', encoding = 'utf-8')
broadway_statistika['year'], broadway_statistika['end'] =(
        broadway_statistika['season'].str.split('-', 1).str)

broadway_statistika
broadway_statistika = broadway_statistika.drop('season', 1)
broadway_statistika = broadway_statistika.drop('end', 1)
broadway_statistika = broadway_statistika[['year', 'gross', 'attendance', 'duration', 'newProductions']]
broadway_statistika.year = broadway_statistika.year.astype(int)
broadway_statistika.gross= broadway_statistika['gross'].str.replace(',', '')
broadway_statistika.gross = broadway_statistika.gross.astype(int)
broadway_statistika.attendance = broadway_statistika.attendance.astype(float)
broadway_statistika.newProductions = broadway_statistika.newProductions.astype(int)

#dobiček
bdobicek = broadway_statistika.plot(kind = 'line', x = 'year', y = 'gross')
#prisotnost
bprisotnost = broadway_statistika.plot(kind = 'line', x = 'year', y = 'attendance')
#nove produkcije
bnovo = broadway_statistika.plot(kind = 'line', x = 'year', y = 'newProductions')
broadway_statistika


# In[27]:


regional_statistika = pd.read_csv('podatki/regional_statistika.csv', encoding = 'utf-8')
regional_statistika['year'], regional_statistika['end'] =(
        regional_statistika['season'].str.split('-', 1).str)

regional_statistika
regional_statistika = regional_statistika.drop('season', 1)
regional_statistika = regional_statistika.drop('end', 1)
regional_statistika = regional_statistika[['year', 'gross', 'attendance', 'duration']]
regional_statistika.year = regional_statistika.year.astype(int)
regional_statistika.gross= regional_statistika['gross'].str.replace(',', '')
regional_statistika.gross = regional_statistika.gross.astype(int)
regional_statistika.attendance = regional_statistika.attendance.astype(float)

#dobiček
rdobicek = regional_statistika.plot(kind = 'line', x = 'year', y = 'gross')
#prisotnost
rprisotnost = regional_statistika.plot(kind = 'line', x = 'year', y = 'attendance')
regional_statistika


# In[ ]:




