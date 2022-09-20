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


#addition SQL query
sql = "INSERT INTO `students` (name, email, address) VALUES (%s, %s, %s)"

#students data
val = [
  ('Ahmed', 'ahmed@uofk.edu', 'Sudan/Khartoum'),
  ('Ali', 'ali@uofk.edu', 'Sudan/Khartoum'),
  ('Khalid', 'khalid@uofk.edu', 'Sudan/Khartoum'),
  ('Fillan', 'fillan@uofk.edu', 'Sudan/Khartoum'),
  ('Illan', 'illan@uofk.edu', 'Sudan/Khartoum')
]

