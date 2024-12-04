import mysql.connector
from mysql.connector import Error
def getConn():
	try:
		conn = mysql.connector.connect (host='192.168.100.117',port=3306,user='user',password='password',database='schoolDB')
		curs = conn.cursor()
		return conn
	except Error as e:
		print(e) 
def getData(sql):
    try:
        conn = getConn()
        curs = conn.cursor()
        curs.execute(sql)
        ans = curs.fetchall()
        return ans
    except Error as e:
        print(e)
def showMenu():
    print("\n--- Menu List ---")
    print("1. Enter SQL Query ")
    print("2. Show Databases")
    print("3. Show Tables")
    print("4. Exit")
try:
    while True:
        showMenu()
        userInput = input("Enter the Option 1 or 2 : \n")
        if userInput == "1":
            while True:
                sql_query = input("Enter MySQL Query or press Ctrl+C to exit: >  ")
                ans = getData(sql_query)
                for data in ans:
                    print(data)
        elif userInput == "2":
            ans = getData("show databases;")
            for data in ans:
                print(data[0])
        elif userInput == "3":
            ans = getData("show tables;")
            for data in ans:
                print(data[0])
        elif userInput == "4":
            print("Exit the script!!!")
            break
except ValueError as e:
    print(e) 