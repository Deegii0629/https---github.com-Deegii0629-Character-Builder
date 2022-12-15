import pymysql #helps connect to mysql
from tabulate import tabulate #https://stackoverflow.com/questions/9535954/printing-lists-as-tabular-data
import Character_Builder
import itertools

#Determines name of attribute for SQL queries
#Accepts int tableNum from 1 to 5
#Returns string corresponding name of attribute in Character_Builder SQL database
def setTable(tableNum):
    tableNum = int(tableNum)
    while(tableNum not in [0,1,2,3,4,5]):
        print("Invalid selection. Try again: ")
        tableNum = int(input())
    if(tableNum == 0):
        table = "character"
    elif(tableNum == 1):
        table = "class"
    elif(tableNum == 2):
        table = "item"
    elif(tableNum == 3):
        table = "headwear"
    elif(tableNum == 4):
        table = "top"
    elif(tableNum == 5):
        table = "bottom"
    return table

#Print out a table
#Accepts int, from 1 to 5
#Returns void
def printTable(tableNum):
    sql = "SELECT *" #the start of the sql query - for the print table function we always need slect all
    if(tableNum == 0):
        collumnNames = ['id','name','ap','ad','hp','wp','capacity','class_id','item_id','head_id','top_id','bottom_id']
    else:
        collumnNames = ['id','name','hp','wp','ad','ap']
        collumnNames1 = ['id','name','hp','capacity','ad','ap']
    table_ = setTable(tableNum)
    sql = sql + " FROM `" + setTable(tableNum) + "` " # adds to our query
    crsr.execute(sql) #executes the sql query
    toPrint = str(collumnNames)
    ##The below is the old method of printing (please leave it for reference and progress)
    # for row in crsr: #loops through each row that was gathered to print neatly into terminal
    #         toPrint = ""
    #         for item in row:
    #             toPrint += str(item) + " "
    #         print(toPrint)
    crsrData = crsr.fetchall()
    if(tableNum == 1):
        print(tabulate(crsrData,headers=collumnNames1,tablefmt='psql'))
    else:
        print(tabulate(crsrData,headers=collumnNames,tablefmt='psql'))
    return table_

#Update the running totals for user's created character
#Accepts int tableNum from 1 to 5; int id
#Returns NULL
def updateRTs(tableNum, statsArray):
    table = setTable(tableNum)
    sql = "SELECT* "
    sql = sql + "FROM " + str(table)
    crsr = db.cursor()
    crsr.execute(sql)
    crsrList = crsr.fetchall()
    #updates tallies
    statsArray[0] += int(crsrList[0][5]) #row5 AP
    statsArray[1] += int(crsrList[0][4]) #row4 AD
    statsArray[2] += int(crsrList[0][2]) #row2 HP
    if (tableNum == 1):
        statsArray[4] += int(crsrList[0][3]) #row3 WCap  
    elif(tableNum < 6 and tableNum > 1):
        statsArray[3] += int(crsrList[0][3]) #row3 WP

def insertAttribute(tableNum):
    printTable(tableNum)
    print("Type the number of your choice and press enter: ")
    useri = input()
    #updateRTs(counter, statsArray) #runs a function that is yet to be written
    print("") #spacing line

def createCharacter(character_name):
    sql = "INSERT INTO `character` (ID, Name)"
    sql = sql + "VALUES (" + str(getNewID()) + ", '" + character_name + "')"
    crsr.execute(sql)

def getTableSize(tableNum_):
    table_to_update = setTable(tableNum_)
    sql = "SELECT Count(ID) FROM `" + table_to_update + "`"
    crsr = db.cursor()
    crsr.execute(sql) #executing the sql
    return crsr.fetchall()[0][0]

def updateCharacterStats(statsArray_):
    characterStats = ["AP","AD","HP","WP","Capacity"]
    counter = 0
    for stat in characterStats:
        stat = str(stat)
        print(stat)
        statsArray_[counter] = str(statsArray_[counter])
        print(statsArray_[counter])
        sql = "UPDATE `" + "character" + "` SET " + stat + " = '" + str(statsArray[counter]) + "' WHERE ID = '" + str(getTableSize(0)) + "'"
        crsr.execute(sql)
        counter = counter + 1

#input is a list of strings of attributes of character and the number of the attribute to be changed
def updateAttributeFromCharacter(AttributeNum_, characterAttributes_):
    AttributeNum_ = int(AttributeNum_)
    table_to_update = setTable(0) #Determine Table FROM which to update
    printTable(AttributeNum_)
    print("Enter number of desired item: ")
    useri = input()
    while(int(useri) < 1 or int(useri) > getTableSize(AttributeNum_)):
        print("Invalid input. Try again: ")
        useri = input()
    item_to_update = characterAttributes_[AttributeNum_ + 7 - 1]
    sql = "UPDATE `" + table_to_update + "` SET `" + item_to_update + "` = " + useri + " WHERE ID = " + str(getTableSize(0))
    # sql = "FROM `" + table_to_update + "` "
    print(AttributeNum_)
    crsr.execute(sql)

#function to find a new valid id number for the character table
def getNewID():
    sql = "SELECT Count(ID) FROM `character`" 
    crsr = db.cursor()
    crsr.execute(sql) #executing the sql
    return crsr.fetchall()[0][0] + 1

#function used to insert a tuple into the character table
# def insertChar(User_Character_Name, statsArray):
#     sql = "INSERT INTO `character` (ID, Name, HP, WP, AD, AP, Capacity)"
#     sql = sql + "VALUES (" + str(getNewID()) + ", " + User_Character_Name + ", " #creates new tuple with values (ID NAME HP WP AD AP CAPACITY) being inserted all at once
#     sql = sql + str(statsArray[2]) + ", " + str(statsArray[3]) + ", " + str(statsArray[1]) + ", " + str(statsArray[0]) + ", " + str(statsArray[4]) + ")" 
#     crsr = db.cursor()
#     crsr.execute(sql) #executing the sql
    
#View a table, or make a change to an attribute of user's Character
#Accepts int tableNum from 1 to 5; int id
#Returns NULL
def view_and_change():
    done = False
    validInputs = ['n','N',1,2,3,4,5]
    tableOptions = ["Class","Item","Headwear","Top","Bottom"]
    #h = ['Number','Attribute']
    while(done == False):
        print("Currently, configuration is: \n")
        print("p.s. Stat attributes are hidden because the object of the game is to figure out what combos yield the best stats!")
        printTable(0)
        #print(tabulate(crsrData,headers=collumnNames,tablefmt='psql'))
        valid = False
        #useri = -1 #####    potentially delete this
        print("1: Class\n2: Item\n3: Headwear\n4: Top\n5: Bottom\n")
        while (valid == False):
            useri = input()
            if (useri not in validInputs == True and int(useri) not in validInputs):
                print("Invalid Input. Use 'n' , 'N' , or the number of the attribute to change: ")
            else: valid = True
        print("Would you like to change anything from these categories?: ")
        print("If so, choose it's number. Otherwise, press 'n' or 'N'")
        #crsrData = crsr.fetchall() tabulate(crsrData, headers= tableOptions, tablefmt='psql')
        if(useri not in ['n','N']):
            updateAttributeFromCharacter(useri , ["ID","Name","AP","AD","HP","WP","Capacity","Class_id","Item_id","Head_id","Top_id","Bottom_id"])
        else:
            done = True
        

#Main Function  
if __name__ == "__main__":
    
    #Connect to Database
    conn_str = (r'DRIVER={MySQL ODBC 8.0 ANSI Driver};Server=localhost;Database=character_builder;UID=root;PWD=Ariunsuld12!') #connects to data base
    db = pymysql.connect(host='localhost', user='root', password='Ariunsuld12!', database='character_builder')
    crsr = db.cursor()

    print(getTableSize(1))

    #Instruct User
    print("Welcome to Character Builder! ")
    print("Type the name of your character and press enter: ")
    User_Character_Name = input()
    createCharacter(User_Character_Name)
    print("")

    characterAttributes = ["ID","Name","AP","AD","HP","WP","Capacity","Class_id","Item_id","Head_id","Top_id","Bottom_id"]
    
    #array for running total variables, represent final stats
    statsArray = [0,0,0,0,0] #represents [AP, AD, HP, WP, WCap]

    #User initializes Character attributes
    counter = 1 
    while(counter < 6):
        updateAttributeFromCharacter(counter,characterAttributes)
        updateRTs(counter, statsArray)
        counter = counter + 1
    view_and_change()

    #calculates percent the character is optimal
    sumStats = statsArray[0] + statsArray[1] + statsArray[2]
    efficiencyPercent = (sumStats/420) * 100
    updateCharacterStats(statsArray)
    #prints finished character info to the screen prompts the option to save
    print("Final stats of ", User_Character_Name, " [AP, AD, HP, WP, WCap]:\n",statsArray)
    print("your character is ", efficiencyPercent, " percent optimal")
    printTable(0)
