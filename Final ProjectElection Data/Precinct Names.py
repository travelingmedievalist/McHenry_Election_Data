infile = open("McHenry_County_Precinct_Names.txt", "rt", encoding = 'utf-8')
PrecinctNameList= infile.read()
infile.close()



print(PrecinctNameList)
