import mysql.connector
from flask import Flask , jsonify

# Create the connection object
myconn = mysql.connector.connect(host="kindletestdata.czend6kabecw.ap-south-1.rds.amazonaws.com", user="admin", passwd="Yashcse1", database="Kindlebookdata")

# printing the connection object
print(myconn)

# creating the cursor object
cur = myconn.cursor()

# sql = "insert into new_table(id,name,book) values (%s, %s, %s)"
# with open("CGAS_ASS1.pdf", 'rb') as file:
# binaryData = file.read()

# empPicture = binaryData

# Convert data into tuple format
# insert_blob_tuple = (6, "tets_book", empPicture)

# try:
# inserting the values into the table
# result = cur.execute(sql, insert_blob_tuple)
# print("Image and file inserted successfully as a BLOB into python_employee table", result)

# commit the transaction
# myconn.commit()

# except:
# myconn.rollback()


sql_fetch_blob_query = """SELECT * from user_data where user_id = %s"""
cur.execute(sql_fetch_blob_query, (1,))
record = cur.fetchall()
for row in record:
    print("Id = ", row[0], )
    print("Name = ", row[1])
    password = row[1]
    print("Storing employee image and bio-data on disk \n")
    print(password)
    # with open("tetsing.pdf", 'wb') as file:
    # file.write(file1)




myconn.close()


app = Flask(__name__)
@app.route('/')
def hello():
    return password

if __name__ =="__main__":
   app.run(host = '0.0.0.0',port=8080)