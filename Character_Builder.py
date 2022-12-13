# pip install pymysql
import pymysql #helps connect to mysql
import pandas as pd # https://stackoverflow.com/questions/46777397/how-can-i-see-the-output-in-python-as-like-sql-table-format
import Character_Builder
import itertools

def printTable(tableNum):
        sql = "SELECT *" #the start of the sql query - for the print table function we always need slect all
        collumnNames = ['id','name','hp','wp','ad','ap']
        if(tableNum == 0):
            sql = sql + " FROM `character` " # adds to our query
            crsr.execute(sql) #executes the sql query
            for row in crsr: #loops through each row that was gathered to print neatly into terminal
                toPrint = ""
                for item in row:
                    toPrint += str(item) + " "
                print(toPrint)
                
        elif(tableNum == 1):
            sql = sql + " from class " # adds to our query
            res = crsr.execute(sql) #executes the sql query
            print(*collumnNames)
            for row in crsr: #loops through each row that was gathered to print neatly into terminal
                toPrint = ""
                for item in row:
                    toPrint += str(item) + " "
                print(toPrint)
        elif(tableNum == 2):  
            sql = sql + " from item "
            res = crsr.execute(sql)
            print(*collumnNames + "capacity")
            for row in crsr: #loops through each row that was gathered to print neatly into terminal
                toPrint = ""
                for item in row:
                    toPrint += str(item) + " "
                print(toPrint)
        elif(tableNum == 3):
            sql = sql + " from headwear "
            res = crsr.execute(sql)
            print(*collumnNames)
            for row in crsr: #loops through each row that was gathered to print neatly into terminal
                toPrint = ""
                for item in row:
                    toPrint += str(item) + " "
                print(toPrint)
        elif(tableNum == 4):
            sql = sql + " from top "
            res = crsr.execute(sql)
            print(*collumnNames)
            for row in crsr: #loops through each row that was gathered to print neatly into terminal
                toPrint = ""
                for item in row:
                    toPrint += str(item) + " "
                print(toPrint)
        elif(tableNum == 5):
            sql = sql + " from bottom "
            crsr.execute(sql)
            print(*collumnNames)
            for row in crsr: #loops through each row that was gathered to print neatly into terminal
                toPrint = ""
                for item in row:
                    toPrint += str(item) + " "
                print(toPrint)
            else: print("invalid entree into printTable()")

def updateRTs(tableNum, id, AP, AD, WP, HP, Wcap):
    sql = "SELECT *"
    if(tableNum == 1):
        sql = sql + "FROM class "
        sql = sql + "WHERE id = "+ str(id)
        crsr = db.cursor()
        crsr.execute(sql)
        print('got here, 73')
        crsrList = crsr.fetchall()
        print(crsrList)
        print(crsrList[0][5])
        print('got here, 75')

        #updates tallies
        # AP += int(crsrList[0][5]) #row5
        # AD += int(crsrList[0][4]) #row4
        # HP += int(crsrList[0][2]) #row2
        # Wcap += int(crsrList[0][3]) #row3        
    elif(tableNum == 2):
        print('')
    elif(tableNum == 3):
        print('')
    elif(tableNum == 4):
        print('')
    elif(tableNum == 5):
        print('')
    else:
        print("invalid tableNum in updateRTs()")

def view_or_change(tableNum):
    printTable(tableNum)
    print("Would you like to change anything here? (y/n): ")
    valid = False
    while (valid == False):
        useri = input()
        if (useri != 'y' or useri !='n'):
            print("Invalid Input. Use 'y' or 'n': ")
        else: valid = True
        
if __name__ == "__main__":
    
    conn_str = (r'DRIVER={MySQL ODBC 8.0 ANSI Driver};Server=localhost;Database=character_builder;UID=root;PWD=Ariunsuld12!') #connects to data base
    db = pymysql.connect(host='localhost', user='root', password='Ariunsuld12!', database='character_builder')
    crsr = db.cursor()

    print("Welcome to Character Builder! ")
    print("Type the name of your character and press enter: ")
    User_Character_Name = input()
   
    # sql = "where id = useri"
    # print("You chose" + str(sql))

    #Remember to cite source
    
    #running total variables, all integers that simply are place holders for final stats
    rtAP = 0 #running total for ability power
    rtAD = 0 #attack damage
    rtWP = 0 #weight points
    rtHP = 0 #Health points
    rtWCap = 0  #Weight capacity
    
    #update loop section
    counter = 1 
    while(counter < 2):
        printTable(counter)
        print("Type the number of your choice and press enter: ")
        useri = input()
        updateRTs(counter, useri, rtAP, rtAD, rtWP, rtHP, rtWCap) #runs a function that is yet to be written
        counter += 1
    #end loop

    #test block
    print(rtAP," ",rtAD)
    #printTable(2) #prints tables 1,2,3,4,5,5

    
    # suto code! Have user choose a name for their character (at some pont doesnt have to be the start)
    #            Present user with each table one at a time
    #            At any point, the user can request to print something, or a variety of things to keep up with what they've done
    #            Have a way for the user to select the tuple they want to add to their character
    #            Once selected we will keep a running tally of their characters stats, so we have to update these after each user selection
    #              - the loop essentially: prints the next table -> takes user input -> updates our running counters
    #            Once gone through every table print and insert their character into our character table
    #            Ask user if they want to change/add anything
