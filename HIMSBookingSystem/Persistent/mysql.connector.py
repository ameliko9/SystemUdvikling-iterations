import mysql.connector

mydb = mysql.connector.connect(host = "localhost",
                               user = "root",
                               password = "Kebab4life1410#",
                               database = 'hims')

print(mydb)

# # get cursor object
# cursor = mydb.cursor()
#
# # execute your query
# cursor.execute("SELECT * FROM booking")
#
# # fetch all the matching rows
# result = cursor.fetchall()
#
# # loop through the rows
# for row in result:
#     print(row)
#     print("\n")