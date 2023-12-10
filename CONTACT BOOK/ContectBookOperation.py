import oracledb
def addinformation():
    while(True):
        try:
            con=oracledb.connect("system/tiger@localhost/ORCL")
            cur=con.cursor()
            print("---------------------------------------------")
            cno=int(input("Enter contact phone number:"))
            cname=input("Enter contact name:")
            cemail=input("Enter contact email:")
            cadr=input("Enter contact address:")
            print("------------------------------------------------")
            cur.execute("insert into contactbook values(%d,'%s','%s','%s')" %(cno,cname,cemail,cadr))
            con.commit()
            if(cur.rowcount>0):
                print("contact record added successfully")
            else:
                print("contact record does not exist")
            ch=input("Do you want to add another record(yes/no):")
            if(ch.lower()=="no"):
                break
            print("-------------------------------------------------------")
        except oracledb.DatabaseError as db:
            print("problem in database",db)
        except ValueError:
            print(" Dont enter alnum,str and special symbols")
#main program


def viewcontactlist():
    try:
        con=oracledb.connect("system/tiger@localhost/ORCL")
        cur=con.cursor()
        cur.execute("select * from contactbook")
        print("------------------------------------------")
        recs=cur.fetchall()
        for rec in recs:
            for val in rec:
                print("{}".format(val),end=" ")
            print()
        print("---------------------------------------------")
    except oracledb.DatabaseError as db:
        print("problem in database",db)
    except ValueError:
        print("dont enter alnum,strs and special symbols")
#main program


def searchcontact():
    try:
        con=oracledb.connect("system/tiger@localhost/ORCL")
        cur=con.cursor()
        cur.execute("select * from contactbook")
        print("-------------------------------------------")
        recs=cur.fetchmany(3)
        for res in recs:
            for val in res:
                print("{}".format(val),end=" ")
            print()
        print("----------------------------------------------")
    except oracledb.DatabaseError as db:
        print("problem in database",db)
    except ValueError:
        print("dont enter alnum str and special symbols")
#main program



def updatecontact():
    while(True):
      try:
          con=oracledb.connect("system/tiger@localhost/ORCL")
          cur=con.cursor()
          print("--------------------------------------------")
          cno=int(input("Enter contact phone number to update:"))
          cname=input("Enter contact name to update other deatils:")
          cemail=input("Enter contact email address to update:")
          cadr=input("Enter contact address to update:")
          cur.execute("update contactbook set cno=%d,cemail='%s',cadr='%s' where cname='%s' "%(cno,cemail,cadr,cname))
          con.commit()
          if(cur.rowcount>0):
              print("Contact record update successfully")
          else:
              print("Contact record does not exist")
          ch=input("Do you want to update another record(yes/no):")
          if(ch.lower()=="no"):
              break
          print("------------------------------------------------")
      except oracledb.DatabaseError as db:
          print("problem in database",db)
      except ValueError:
          print("dont enter alnum,str and special symbols")
#main program



def Deletecontact():
    while(True):
        try:
           con=oracledb.connect("system/tiger@localhost/ORCL")
           cur=con.cursor()
           print("------------------------------------------")
           cname=input("Enter contact name:")
           cur.execute("delete from contactBook where cname='%s'"%cname)
           con.commit()
           if(cur.rowcount>0):
               print("contactBook record deleted")
           else:
               print("contactBook record does not exist")
           ch=input("Do you want to delete another record(yes/no):")
           if(ch.lower()=="no"):
               break
           print("-----------------------------------------------")
        except oracledb.DatabaseError as db:
            print("problem in database",db)
        except ValueError:
            print("dont enter alnum,strs and symbols")
#main program




