import csv
import MySQLdb

mydb = MySQLdb.connect(host="127.0.0.1", user="root", password="", database="student_db")

with open('Machine_readable_file.csv') as csv_file:
    csvfile = csv.reader(csv_file, delimiter=",")
    all_value = []
    for row in csvfile:
        value = (row[0], row[1], row[2])
        all_value.append(value)


# Create the INSERT INTO sql query
query = "insert into `info` (`name`,`company`,`contactno`) VALUES (%s, %s, %s)"


# Get the cursor, which is used to traverse the database, line by line
mycursor = mydb.cursor()

mycursor.executemany(query, all_value)

# Commit the transaction
mydb.commit()
