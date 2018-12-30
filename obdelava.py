#BROADWAY
#Trenutno se izvajajo te predstave:
broadway_trenutno = broadway[broadway['time'].str.contains(r'\d{10}')]
#Napovedane so te predstave:
broadway_prihodnje = broadway[broadway['time'].str.contains(r'2018-2019')]
#Najpopularnejše gledališče:
broadway.venue.describe()
broadway[broadway.venue.str.contains('American Airlines Theatre')]
