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

#execute sql query with many values
mycursor.executemany(sql, val)


#commit transactions
mydb.commit()



print(mycursor.rowcount, " rows was inserted.") 

#access token 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