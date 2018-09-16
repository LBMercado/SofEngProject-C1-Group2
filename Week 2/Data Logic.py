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
adminNAME="Gl21enn"
adminID=201510330194
adminPW="admin3121234"


candidatePOSITION="Presi21dent"
candidateNAME="Glenn Si312oson"
candidateID=201510031194
candidatePARTY="Glenn Pa312rtylist"

voterID=2015100194313144
voterNAME="Glenn De312312la Cruz"
voterEMAIL="gcdsioso3213n@gmail.com"
voterPW="gle21nn"
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



