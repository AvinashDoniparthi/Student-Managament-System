import mysql.connector as mc
con = mc.connect(host = 'localhost', user = 'root', password = 'avinashbvm', database = 'studb')
cur = con.cursor()
#database creation
import dbcreation
dbcreation.createdb()



print('|==================================================STUDENT MANAGEMENT SYSTEM==================================================|')
name = input('Enter Username')
pwd = input('Enter Password')
print()

#Authorisation
cur.execute(f"select * from users where user = '{name}' and password = '{pwd}'")
if cur.fetchone() is None:
    print('INVALID!')
else:
    import Main





# © PROJECT DONE BY AVINASH DONIPARTHI
