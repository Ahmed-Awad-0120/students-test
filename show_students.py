import mysql.connector

#database connection instance

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Aiman@012",
  database="students_test"
)


#connection cursor for transactions
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM `students`")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)