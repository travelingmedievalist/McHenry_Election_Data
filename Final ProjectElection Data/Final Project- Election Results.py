import pandas as pd
import numpy as np
import re

pd.set_option('display.max_columns',8) # I wasn't seeing all my columns and I needed to in order to make sure my added columns happened
pd.set_option('display.max_row',10) # I was getting too much that I didn't need to make sure things were working, so I limited the number displayed

McH2018GE_RAW = pd.read_csv('McHENRY2018GE.csv') #reading in my data
McH2016GE_RAW = pd.read_csv('McHENRY2016GE.csv')
McH2014GE_RAW = pd.read_csv('McHENRY2014GE.csv')

def deletecolumns (df):     #cleaning up my data by deleting columns that I wasn't using
    del df['JurisdictionID']
    del df['JurisName']   #Because all of my data is for McHenry Co. I do not need this now.  If I expand my data to other counties I will put this column back in
    del df['EISCandidateID']
    del df['EISContestID']
    del df['EISPartyID']

deletecolumns(McH2014GE_RAW)
deletecolumns(McH2016GE_RAW)
deletecolumns(McH2018GE_RAW)

McH2014GE_RAW["ElectionYear"] = "2014_General Election"  #Added a column so each line notes which election year, will come in handy when comparing between datasets
McH2016GE_RAW["ElectionYear"] = "2016_General Election"
McH2018GE_RAW["ElectionYear"] = "2018_General Election"

McH2014GE_RAW["VoterTurnout"]= round((McH2014GE_RAW['VoteCount'] /McH2014GE_RAW['Registration']) *100)  #knowing the percentage turnout is always helpful
McH2016GE_RAW["VoterTurnout"]= round((McH2016GE_RAW['VoteCount'] /McH2016GE_RAW['Registration']) *100)
McH2018GE_RAW["VoterTurnout"]= round((McH2018GE_RAW['VoteCount'] /McH2018GE_RAW['Registration']) *100)

McH2014GE_reordered= McH2014GE_RAW[["ContestName", "CandidateName", "PartyName", "Registration", "VoteCount", "VoterTurnout", "PrecinctName", "ElectionYear"]]
McH2016GE_reordered= McH2016GE_RAW[["ContestName", "CandidateName", "PartyName", "Registration", "VoteCount", "VoterTurnout", "PrecinctName", "ElectionYear"]]
McH2018GE_reordered= McH2018GE_RAW[["ContestName", "CandidateName", "PartyName", "Registration", "VoteCount", "VoterTurnout", "PrecinctName", "ElectionYear"]]

McH2018GE_cleaned= McH2018GE_reordered.dropna(subset=["ContestName", "CandidateName", "PrecinctName"])

McH2014GE_Sorted = McH2014GE_reordered.sort_values(by= ["ContestName", "VoteCount"], ascending=(True, False))
McH2016GE_Sorted = McH2016GE_reordered.sort_values(by= ["ContestName", "VoteCount"], ascending=(True, False))
McH2018GE_Sorted = McH2018GE_cleaned.sort_values(by= ["ContestName", "VoteCount"], ascending=(True, False))




# McH2014GE_RAW ["FileName"] = McH2014GE_RAW["PrecinctName"] + McH2014GE_RAW["ElectionYear"] + ".csv" #because Pandas is bad at allowing you to set-up a filenaming system
# McH2016GE_RAW ["FileName"] = McH2016GE_RAW["PrecinctName"] + McH2016GE_RAW["ElectionYear"] + ".csv" #at least according to what I can find on StackOverflow and Google searching
# McH2018GE_RAW ["FileName"] = McH2018GE_RAW["PrecinctName"] + McH2018GE_RAW["ElectionYear"] + ".csv"

def pullprecinctdata14(precinctname): # function to pull out specified precinct
    PRECINCTNAME= precinctname.upper()
    precinctdataname = McH2014GE_Sorted[McH2014GE_Sorted['PrecinctName'].str.contains(PRECINCTNAME)]
    fileout= precinctname + "_2014-General" + ".csv"   #I was having problems getting the file name to come out of the info in dataframe, so I opted for 3 functions instead of 1,
    filename= fileout.lower()                         # I want to combine the 3 functions in the future
    precinctdataname.to_csv (filename, index = 0)  # Eventually I would like to figure out how to have the data save to a subdirectory
    return



def pullprecinctdata16(precinctname):
    PRECINCTNAME= precinctname.upper()
    precinctdataname = McH2016GE_Sorted[McH2016GE_Sorted['PrecinctName'].str.contains(PRECINCTNAME)]
    fileout= precinctname + "_2016-General" + ".csv"
    filename= fileout.lower()
    precinctdataname.to_csv (filename, index = 0)
    return

def pullprecinctdata18(precinctname):
    PRECINCTNAME= precinctname.upper()
    precinctdataname = McH2018GE_Sorted[McH2018GE_Sorted['PrecinctName'].str.contains(PRECINCTNAME)]
    fileout= precinctname + "_2018-General" + ".csv"
    filename= fileout.lower()
    precinctdataname.to_csv (filename)
    return


infile = open("McHenry_County_Precinct_Names.txt", "rt", encoding = 'utf-8')
namelist= infile.read()
infile.close()

PrecinctNameList= namelist.split('\n')



for precinct in PrecinctNameList:
    pullprecinctdata14(precinct)
    pullprecinctdata16(precinct)
    pullprecinctdata18(precinct)


####OMG It totally worked!!!  I am so proud of myself####


