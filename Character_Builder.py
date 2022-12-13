# pip install pymysql
import pymysql #helps connect to
import pyodbc
import Character_Builder
def printTable(tableNum):
        conn_str = (
            r'DRIVER={MySQL ODBC 8.0 ANSI Driver};Server=localhost;Database=character_builder;UID=root;PWD=Ariunsuld12!'
            )
        cnxn = pyodbc.connect(conn_str)
#        for item in _list:
        if(tableNum == 0):
                db = pymysql.connect(host='localhost', user='root', password='Ariunsuld12!', database='character_builder')
                crsr = db.cursor()
                sql = "select *"
                sql = sql + " from Character "

                res = crsr.execute(sql)
                for row in crsr:
                    print(str(row[0]) + ": " + str(row[1]))
        else:
                if(tableNum == 1):
                    db = pymysql.connect(host='localhost', user='root', password='Ariunsuld12!', database='character_builder')
                    crsr = db.cursor()
                    sql = "select *"
                    sql = sql + " from Class "

                    res = crsr.execute(sql)
                    for row in crsr:
                        print(row[0] + ": " + row[1])
                    else:
                        if(tableNum == 2):
                            db = pymysql.connect(host='localhost', user='root', password='Ariunsuld12!', database='character_builder')
                            crsr = db.cursor()
                            sql = "select *"
                            sql = sql + " from Item "

                            res = crsr.execute(sql)
                            for row in crsr:
                                print(row[0] + ": " + row[1])
                            else:
                                if(tableNum == 3):
                                    db = pymysql.connect(host='localhost', user='root', password='Ariunsuld12!', database='character_builder')
                                    crsr = db.cursor()
                                    sql = "select *"
                                    sql = sql + " from Head "

                                    res = crsr.execute(sql)
                                    for row in crsr:
                                        print(row[0] + ": " + row[1])
                                    else:
                                        if(tableNum == 4):
                                            db = pymysql.connect(host='localhost', user='root', password='Ariunsuld12!', database='character_builder')
                                            crsr = db.cursor()
                                            sql = "select *"
                                            sql = sql + " from Top "

                                            res = crsr.execute(sql)
                                            for row in crsr:
                                                print(row[0] + ": " + row[1])
                                            else:
                                                if(tableNum == 5):
                                                    db = pymysql.connect(host='localhost', user='root', password='Ariunsuld12!', database='character_builder')
                                                    crsr = db.cursor()
                                                    sql = "select *"
                                                    sql = sql + " from Bottom "

                                                    res = crsr.execute(sql)
                                                    for row in crsr:
                                                        print("id   name     hp  wp  ad  ap")
                                                        print(str(row[0]) + ": " + str(row[1]) + " " + str(row[2]) + " " + str(row[3]) + " " + str(row[4]) + " " + str(row[5]))
                                                    else: print("invalid entree into printTable()")


if __name__ == "__main__":

    print("Welcome to Character Builder!\nType the number of your choices and press enter.")
    #printTable(5)
#attempt2 from slides - (how it works in print table function)
    conn_str = (
        r"DRIVER={MySQL ODBC 8.0 ANSI Driver};Server=localhost;Database=character_builder;UID=root;PWD=Ariunsuld12!"
        )

    db = pymysql.connect(host='localhost', user='root', password='Ariunsuld12!', database='character_builder')
    crsr = db.cursor()
    sql = "SELECT * "
    sql = sql + " FROM Class "

    res = crsr.execute(sql)
    print("id  name  hp  wp  ad  ap")
    for row in crsr:
       #print(str(row[0]) + ": " + str(row[1]))
        print(str(row[0]) + ": " + str(row[1]) + " " + str(row[2]) + " " + str(row[3]) + " " + str(row[4]) + " " + str(row[5]))