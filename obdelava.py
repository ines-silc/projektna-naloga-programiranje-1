import pandas as pd
import matplotlib as plt

broadway = pd.read_csv('podatki/broadway.csv', encoding = 'cp1252')
offbroadway = pd.read_csv('podatki/offbroadway.csv', encoding = 'cp1252')
regional = pd.read_csv('podatki/regional.csv', encoding = 'cp1252')
london = pd.read_csv('podatki/london.csv', encoding = 'cp1252')

#BROADWAY
#Trenutno se izvajajo te predstave:
broadway_trenutno = broadway[broadway['time'].str.contains(r'\d{10}')]

#Napovedane so te predstave:
broadway_prihodnje = broadway[broadway['time'].str.contains(r'2018-2019')]

#Najpopularnejše gledališče:
broadway.venue.describe()
broadway[broadway.venue.str.contains('American Airlines Theatre')]

#OFFBROADWAY
#Najpopularnejše gledališče:
offbroadway.venue.describe()
offbroadway[offbroadway.venue.str.contains('St. Luke&#x27;s Theatre')]

broadway_statistika = pd.read_csv('podatki/broadway_statistika.csv', encoding = 'utf-8')
