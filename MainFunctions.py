import mysql.connector as mc
import tabulate as tab
con = mc.connect(host = 'localhost', user = 'root', password = 'avinashbvm', database = 'studb')
cur = con.cursor()
con.autocommit = True


#==========================================================================================================================================

def printAll():
    global con
    global cur
    try:
        cur.execute("select * from students")
        header = ['STUDENT ID','FIRST NAME','LAST NAME','CLASS','SEC','STREAM','FATHER NAME','MOTHER NAME', 'PARENTS PHONE NUMBER', 'DATE OF JOIN']
        data = cur.fetchall()
        print (tab.tabulate(data,header,tablefmt = 'grid'))
    except:
        print('ERROR HAS OCCURED!! PLEASE TRY AGAIN!!')
#==========================================================================================================================================
        
def addStudent():
    global con
    global cur
    print('|================================================ADD NEW STUDENT================================================|')
    while True:
        try:
            firstname = input('Enter Students First Name :')
            if firstname.isalpha():
                break
            else:
                print('INVALID')
        except:
            print('INVALID')
    while True:
        try:
            lastname = input('Enter Students Last Name :')
            if lastname.isalpha():
                break
            else:
                print('INVALID')
        except:
            print('INVALID')
#Class
    while True:
        try:
            stuclass = int(input('Enter Student Class :'))
            if stuclass not in [1,2,3,4,5,6,7,8,9,10,11,12]:
                print ('INVALID')
            else:
                break
        except:
            print('INVALID!')
    while True:
        try:
            sec = input('Enter Section :')
            if sec.isalpha() and len(sec) == 1:
               break
            else:
                print('INVALID')
        except:
            print('INVALID!')
    while True:
        try:
            stream = input('Enter Stream (CsMath,BioMath,BioPsych,Commerce,Humanities) :')
            if stream in ['CsMath', 'BioMath', 'BioPsych', 'Commerce', 'Humanities']:
               break
            else:
                print('INVALID')
        except:
            print('INVALID!')
    while True:
        try:
            fathername = input('Enter Father Name :')
            if fathername.isdigit():
                print('INVALID')
            else:
                break        
        except:
            print('INVALID!')
    while True:
        try:
            mothername = input('Enter Mother Name :')
            if mothername.isdigit():
                print('INVALID')
            else:
                break 
        except:
            print('INVALID!')
    while True:
        try:
            phno = input('Enter Parents Phone Number:')
            if phno.isdigit() and len(phno) == 10:
               break
            else:
                print('INVALID')
        except:
            print('INVALID!')
    while True:
        try:
            year = input('Enter Year (YYYY) :')
            if len(year) !=4:
                 print('INVALID')
            else:
                break
        except:
            print('INVALID!')
    while True:
        try:             
            month = input('Enter Month (MM) :')
            if len(month) != 2 or int(month) > 12:
                print('INVALID')
            else:
                break
        except:
            print('INVALID!')
    while True:
        try:
            day = input('Enter Day (DD) :')
            if len(day) !=2 or int(day)  > 31:
                print('INVALID')
            else:
                break
        except:
            print('INVALID!')

    date = year+'-'+month+'-'+day
    cur.execute(f"insert into students(first_name,last_name,class,sec,stream,father_name,mother_name,parents_phno,DOJ)\
                values('{firstname}','{lastname}',{stuclass},'{sec}','{stream}','{fathername}','{mothername}',{phno},'{date}')")

    cur.execute(f"insert into marks(WT_I,MT_I,Half_Yearly,WT_II,MT_II,Annual)\
                 values (Null,Null,Null,Null,Null,Null)")



    print('''STUDENT HAS BEEN ADDED!!
WELCOME TO XXXXXX''')
#==========================================================================================================================================

def delStudent():
    global con
    global cur
    print('|================================================DELETE STUDENT================================================|')
    try:
        stuid = int(input('Enter ID of Student to be Removed :'))
        cur.execute(f"select * from students where stu_id = {stuid}")
        data = cur.fetchall()
        if len(data) == 0:
            print('Student Not Found !')
        else:
            header = ['STUDENT ID','FIRST NAME','LAST NAME','CLASS','SEC','STREAM','FATHER NAME','MOTHER NAME', 'PARENTS PHONE NUMBER','JOINING DATE']
            print(tab.tabulate(data,header,tablefmt = 'grid'))
            ch = input('Is this the student to be removed?(y/n) :')
            if ch in ('y','Y'):
                cur.execute(f"delete from students where stu_id = {stuid}")
                print('Record has been removed succesfully')
                cur.execute(f"delete from marks where stu_id = {stuid}")
    except:
        print('INVALID')
#==========================================================================================================================================

def editDetails():
    global con
    global cur
    print('|================================================EDIT STUDENT DETAILS================================================|')
    stuid = int(input('Enter ID of Student whose details are to be edited :'))
    cur.execute(f"select * from students where stu_id = {stuid}")
    if len(cur.fetchall()) == 0:
        print('Student not found ')
    else:
        ch = int(input('''
1 --> First Name
2 --> Last Name
3 --> Class
4 --> Sec
5 --> Stream
6 --> Father Name
7 --> Mother Name
8 --> Parents Phone Number
9 --> Date Of Join
10 --> Average Marks Of Student:
11 --> Exit
'''))
        if ch == 11:
            while True:
                break
        elif ch == 1:
            while True:
                try:
                    firstname = input('Enter students updated First Name :')
                    if firstname.isalpha():
                        cur.execute(f"update students set first_name = '{firstname}' where stu_id = {stuid}")
                        print('Edited Succesfully')    
                        break
                    else:
                        print('INVALID')
                except:
                    print('INVALID!')
        elif ch == 2:
            while True:
                try:
                    lastname = input('Enter students updated Last Name :')
                    if lastname.isalpha():
                        cur.execute(f"update students set last_name = '{lastname}' where stu_id = {stuid}")
                        print('Edited Succesfully')
                        break
                    else:
                        print('INVALID')
                except:
                    print('INVALID!')
        elif ch == 3:
            while True:
                try:
                    stuclass = int(input('Enter students updated Class:'))
                    if stuclass in [1,2,3,4,5.6,7,8,9,10,11,12]:
                        cur.execute(f"update students set class = {stuclass} where stu_id = {stuid}")
                        print('Edited Succesfully')
                        break
                    else:
                        print('INVALID')
                except:
                    print('INVALID!')
        elif ch == 4:
            while True:
                try:
                    sec = input('Enter students updated Section:')
                    if sec.isalpha() and len(sec) == 1:
                        cur.execute(f"update students set sec = '{sec}' where stu_id = {stuid}")
                        print('Edited Succesfully')
                        break
                    else:
                        print('INVALID')
                except:
                    print('INVALID!')
        elif ch == 5:
            while True:
                try:
                    stream = input('Enter updated Stream (CsMath,BioMath,BioPsych,Commerce,Humanities) :')
                    if stream in ['CsMath', 'BioMath', 'BioPsych', 'Commerce', 'Humanities']:
                        cur.execute(f"update students set stream = '{stream}' where stu_id = {stuid}")
                        print('Edited Succesfully')
                        break
                    else:
                        print('INVALID')
                except:
                    print('INVALID!')
        elif ch == 6:
            while True:
                try:
                    fathername = input('Enter updated Father\'s name :')
                    if fathername.isdigit():
                        print('INVALID')
                    else:
                        cur.execute(f"update students set father_name = '{fathername}' where stu_id = {stuid}")
                        print('Edited Succesfully')    
                        break
                except:
                    print('INVALID!')
        elif ch == 7:
            while True:
                try:
                    mothername = input('Enter updated Mother\'s name :')
                    if mothername.isalpha():
                        cur.execute(f"update students set mother_name = '{mothername}' where stu_id = {stuid}")
                        print('Edited Succesfully')    
                        break
                    else:
                        print('INVALID')
                except:
                    print('INVALID!')
        elif ch == 8:
            while True:
                try:
                    phno = int(input('Enter updated Phone Number :'))
                    if len(str(phno)) == 10:
                         cur.execute(f"update students set parents_phno = {phno} where stu_id = {stuid}")
                         print('Edited Succesfully')
                         break
                    else:
                        print('INVALID')
                except:
                    print('INVALID!')
        elif ch == 9:
            try:
                while True:
                        year = input('Enter Updated Year (YYYY) :')
                        if len(str(year)) == 4:
                             break
                        else:
                            print('INVALID')
                while True:
                        month = input('Enter Updated Month (MM) :')
                        if len(month) == 2 or int(month) < 12: 
                            break
                        else:
                            print('INVALID')
                while True:
                        day = input('Enter Updated Day (DD) :')
                        if len(day) == 2 or int(day)  < 31:
                            break
                        else:
                            print('INVALID')
                date = year + '-' + month + '-' + day
                cur.execute(f"update students set DOJ = '{date}' where stu_id = {stuid}")
            except:
                print('INVALID!')
        elif ch == 10:
            try:
                while True:
                    wt1 = float(input('Enter Average % in WEEKLY TEST-I :'))
                    if wt1 < 0 or wt1 > 100:
                        print('INVALID')
                    else:
                        break
                while True:
                    mt1 = float(input('Enter Average % in MID TERM EXAM-I :'))
                    if mt1 < 0 or mt1 > 100:
                        print('INVALID')
                    else:
                        break
                while True:
                    hy = float(input('Enter Average % in HALF YEARLY EXAM :'))
                    if hy < 0 or hy > 100:
                        print('INVALID')
                    else:
                        break
                while True:
                    wt2 = float(input('Enter Average % in WEEKLY TEST-II :'))
                    if wt2 < 0 or wt2 > 100:
                        print('INVALID')
                    else:
                        break
                while True:
                    mt2 = float(input('Enter Average % in MID TERM EXAM-II :'))
                    if mt2 < 0 or mt2 > 100:
                        print('INVALID')
                    else:
                        break
                while True:
                    an = float(input('Enter Average % in ANNUAL EXAM :'))
                    if an < 0 or an > 100:
                        print('INVALID')
                    else:
                        break

                cur.execute(f"update marks set WT_I = {wt1}, MT_I = {mt1}, Half_Yearly = {hy}, WT_II = {wt2}, MT_II = {mt2}, Annual = {an}\
                            where stu_id = {stuid}")
            except:
                print('INVALID !')

#==========================================================================================================================================

def search():
    ch = int(input(''' Search By
1 --> Student ID
2 --> Student First Name
3 --> Student Last Name
4 --> Class
5 --> Section
6 --> Stream
7 --> Father Name
8 --> Mother Name
9 --> Parents Phone Number
10 --> Exit
'''))

    if ch == 1:
        stuid = int(input('Enter Student ID :'))
        cur.execute (f'Select * from students where stu_id = {stuid}')
        data = cur.fetchall()
        if len(data) == 0:
            print('Student with ID ',stuid,'does not exist')
        else:
            header = ['STUDENT ID','FIRST NAME','LAST NAME','CLASS','SEC','STREAM','FATHER NAME','MOTHER NAME', 'PARENTS PHONE NUMBER','JOINING DATE']
            print(tab.tabulate(data,header,tablefmt = 'grid'))
    elif ch == 2:
        firstname = input('Enter first name :')
        cur.execute (f"select * from students where first_name = '{firstname}'")
        data = cur.fetchall()
        if len(data) == 0:
            print('Student with First Name ',firstname,'does not exist')
        else:
            header = ['STUDENT ID','FIRST NAME','LAST NAME','CLASS','SEC','STREAM','FATHER NAME','MOTHER NAME', 'PARENTS PHONE NUMBER','JOINING DATE']
            print(tab.tabulate(data,header,tablefmt = 'grid'))
    elif ch == 3:
        lastname = input('Enter last name :')
        cur.execute (f"select * from students where last_name = '{lastname}'")
        data = cur.fetchall()
        if len(data) == 0:
            print('Student with Lasr Name ',lastname,'does not exist')
        else:
            header = ['STUDENT ID','FIRST NAME','LAST NAME','CLASS','SEC','STREAM','FATHER NAME','MOTHER NAME', 'PARENTS PHONE NUMBER','JOINING DATE']
            print(tab.tabulate(data,header,tablefmt = 'grid'))
    elif ch == 4:
        stuclass = int(input('Enter Class :'))
        cur.execute (f"select * from students where class = {stuclass}")
        data = cur.fetchall()
        if len(data) == 0:
            print('Student with Class ',stuclass,'does not exist')
        else:
            header = ['STUDENT ID','FIRST NAME','LAST NAME','CLASS','SEC','STREAM','FATHER NAME','MOTHER NAME', 'PARENTS PHONE NUMBER','JOINING DATE']
            print(tab.tabulate(data,header,tablefmt = 'grid'))
    elif ch == 5:
        section = input('Enter section :')
        cur.execute (f"select * from students where sec = '{section}'")
        data = cur.fetchall()
        if len(data) == 0:
            print('Student with Section ',section,'does not exist')
        else:
            header = ['STUDENT ID','FIRST NAME','LAST NAME','CLASS','SEC','STREAM','FATHER NAME','MOTHER NAME', 'PARENTS PHONE NUMBER','JOINING DATE']
            print(tab.tabulate(data,header,tablefmt = 'grid'))
    elif ch == 6:
        stream = input('Enter stream :')
        cur.execute (f"select * from students where stream = '{stream}'")
        data = cur.fetchall()
        if len(data) == 0:
            print('Student with stream ',stream,'does not exist')
        else:
            header = ['STUDENT ID','FIRST NAME','LAST NAME','CLASS','SEC','STREAM','FATHER NAME','MOTHER NAME', 'PARENTS PHONE NUMBER','JOINING DATE']
            print(tab.tabulate(data,header,tablefmt = 'grid'))
    elif ch == 7:
        fathername = input('Enter Father Name :')
        cur.execute (f"select * from students where father_name = '{fathername}'")
        data = cur.fetchall()
        if len(data) == 0:
            print('Student with Father Name ',fathername,'does not exist')
        else:
            header = ['STUDENT ID','FIRST NAME','LAST NAME','CLASS','SEC','STREAM','FATHER NAME','MOTHER NAME', 'PARENTS PHONE NUMBER','JOINING DATE']
            print(tab.tabulate(data,header,tablefmt = 'grid'))
    elif ch == 8:
        mothername = input('Enter Mother Name :')
        cur.execute (f"select * from students where mother_name = '{mothername}'")
        data = cur.fetchall()
        if len(data) == 0:
            print('Student with Mother Name ',mothername,'does not exist')
        else:
            header = ['STUDENT ID','FIRST NAME','LAST NAME','CLASS','SEC','STREAM','FATHER NAME','MOTHER NAME', 'PARENTS PHONE NUMBER','JOINING DATE']
            print(tab.tabulate(data,header,tablefmt = 'grid'))
    elif ch == 9:
        phno = input('Enter Parents Phone Number')
        cur.execute (f"select * from students where parents_phno = '{phno}'")
        data = cur.fetchall()
        if len(data) == 0:
            print('Student with Phone Number ',phno,'does not exist')
        else:
            header = ['STUDENT ID','FIRST NAME','LAST NAME','CLASS','SEC','STREAM','FATHER NAME','MOTHER NAME', 'PARENTS PHONE NUMBER','JOINING DATE']
            print(tab.tabulate(data,header,tablefmt = 'grid'))
    elif ch == 10:
        while True:
            break
#==========================================================================================================================================
def showMarks():
    stuid = int(input('Enter ID of student whose mark is to printed :'))
    cur.execute(f"select * from marks where stu_id = {stuid}")
    data = cur.fetchall()
    if len(data) == 0:
        print(f'Student with ID {stuid} does not exist')
    else:
        print('**********************************************************AVERAGE MARKS(%)**********************************************************')
        header = ['STUDENT ID','WEEKLY TEST-I(%)','MID TERM EXAM-I(%)','HALF YEARLY EXAM(%)','WEEKLY TEST-II(%)'\
                  ,'MID TERM EXAM-II(%)','ANNUAL EXAM(%)']
        print(tab.tabulate(data,header,tablefmt = 'grid'))
#==========================================================================================================================================

while True:
    try:
        choice = int(input('''
1 --> Print Details Of All Students
2 --> Add New Students
3 --> Remove Students
4 --> Edit Student Details
5 --> Search Student Details
6 --> Show Student Marks(%)
7 --> Exit
'''))
        if choice == 1:
            printAll()
        elif choice == 2:
            addStudent()
        elif choice == 3:
            delStudent()
        elif choice == 4:
            editDetails()
        elif choice == 5:
            search()
        elif choice == 6:
            showMarks()
        elif choice == 7:
            break
        else:
            print('INVALID')
    except:
        print('INVALID!')
#==========================================================================================================================================



# © PROJECT DONE BY AVINASH DONIPARTHI


    
            


        
        
                            
                 
