import mysql.connector as mc
con = mc.connect(host = 'localhost', user = 'root', password = 'avinashbvm')
cur = con.cursor()
con.autocommit = True

def createdb():
    #Create Student Database if it doesnt already exist
    cur.execute("create database if not exists studb")


    #Use the database
    cur.execute("use studb")

    #Create users table for authentication process
    cur.execute("create table if not exists users(user varchar(10) primary key,password varchar(15))")

    #Create the main table for holding students' data
    cur.execute("create table if not exists students(stu_id int auto_increment primary key, first_name varchar(25), last_name varchar (25), class int,sec char(1),\
    stream varchar(10), father_name varchar(25), mother_name varchar(25),parents_phno varchar(10), DOJ date)")
    #Create Marks Table
    cur.execute("create table if not exists marks(stu_id int auto_increment primary key, WT_I float(20,1), MT_I float(20,1), Half_Yearly float(30,1),\
    WT_II float(20,1), MT_II float(20,1), Annual float(20,1))")



#Adding Users
def addUsers():
    user = input('Enter Username')
    password = input('Enter Password')
    cur.execute(f"insert into users values('{user}','{password}')")




# © PROJECT DONE BY AVINASH DONIPARTHI
