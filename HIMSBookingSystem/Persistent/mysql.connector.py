import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost", user = "root", password = "Kebab4life1410#", database = "HIMS")

print(mydb)