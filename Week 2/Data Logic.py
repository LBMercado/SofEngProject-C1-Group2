import sqlite3
import os

from pathlib import Path
dirname = "D:/Documents/COE125/Data Logic"
filename = "Main"
suffix = ".db"
Path(dirname).joinpath(filename).with_suffix(suffix)
os.path.join('D:/Documents/COE125/Data Logic/Main.db')


#OY DITO NYO ILALAGAY YUNG VARIABLE 
#BAHALA KAYO JAN 
#AAAAAAAAAAAAAA DITOOOO
adminNAME="Glenn"
adminID=2015100194
adminPW="admin1234"


candidatePOSITION="President"
candidateNAME="Glenn Sioson"
candidateID=2015100194
candidatePARTY="Glenn Partylist"

voterID=201510019444
voterNAME="Glenn Dela Cruz"
voterEMAIL="gcdsioson@gmail.com"
voterPW="glenn"
voteCOUNT=1

#end AAAAAAAAAAAAAAAAAAAAAAAA

connection = sqlite3.connect('Main.db')
dl = connection.cursor()


dl.execute("INSERT INTO admin_info values(?,?,?)",(adminNAME,adminID,adminPW))
dl.execute("COMMIT")

dl.execute("INSERT INTO candidate_info values(?,?,?,?)",(candidatePOSITION,candidateNAME,candidateID,candidatePARTY))
dl.execute("COMMIT")

dl.execute("INSERT INTO vote_tally values(?,?,?,?)",(voterID,candidateID,voteCOUNT,candidatePOSITION))
dl.execute("COMMIT")

dl.execute("INSERT INTO voter_info values(?,?,?,?)",(voterNAME,voterEMAIL,voterPW,voterID))
dl.execute("COMMIT")



