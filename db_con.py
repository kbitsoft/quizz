import mysql.connector

def con():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="digi_school"
    )
    return mydb

#from db_con import con
#mydb=con()
#cursor = mydb.cursor()