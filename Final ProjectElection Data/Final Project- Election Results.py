import pandas as pd
import numpy as np #not sure why this wont import as I have added numpy package to the interpreter via the preferences for this project

pd.set_option('display.max_columns',8) # I wasn't seeing all my columns and I needed to in order to make sure my added columns happened
pd.set_option('display.max_row',10) # I was getting too much that I didn't need to make sure things were working, so I limited the number displayed

McH2018GE_RAW = pd.read_csv('McHENRY2018GE.csv', header= 0) #reading in my data
McH2016GE_RAW = pd.read_csv('McHENRY2016GE.csv', header= 0)
McH2014GE_RAW = pd.read_csv('McHENRY2014GE.csv', header= 0)

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

def pullprecinctdata(df, precinctname ): # function to pull out specified precinct

    precinctdataname = df[df['PrecinctName'].str.contains(precinctname)]
    # precinctdataname = pd.DataFrame(precinctdataname, columns = ['PrecinctName', 'ContestName', 'CandidateName', 'PartyName', 'Registration', 'VoteCount','VoterTurnout' ]
    precinctdataname.to_csv(precinctname + precinctdataname['ElectionYear'].str + ".csv", encoding='utf-8', index=False)
    return

pullprecinctdata(McH2014GE_RAW, "Riley")

infile = open("McHenry_County_Precinct_Names.txt", "rt", encoding = 'utf-8')
namelist= infile.read()
infile.close()

PrecinctNameList= namelist.split('\n')
# print(PrecinctNameList)

# for precinct in PrecinctNameList:
#     pullprecinctdata(McH2014GE_RAW, precinct)

