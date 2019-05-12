infile = open("McHenry_County_Precinct_Names.txt", "rt", encoding = 'utf-8')
namelist= infile.read()
infile.close()
processednamelist= namelist.replace(" ","")

PrecinctNameList= processednamelistnamelist.split('\n')





