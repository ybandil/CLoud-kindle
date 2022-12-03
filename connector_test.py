import mysql.connector
from flask import Flask, jsonify, render_template

# Create the connection object
myconn = mysql.connector.connect(host="kindletestdata.czend6kabecw.ap-south-1.rds.amazonaws.com", user="admin",
                                 passwd="Yashcse1", database="Kindlebookdata")

# printing the connection object
print(myconn)

# creating the cursor object
cur = myconn.cursor()

# sql = "insert into book_data(book_id,book_name,book_pdf) values (%s, %s, %s)"
# with open("CGAS_ASS1.pdf", 'rb') as file:
#     binaryData = file.read()
#
# empPicture = binaryData
#
# # Convert data into tuple format
# insert_blob_tuple = (1, "tets_book", empPicture)
#
# try:
#     # inserting the values into the table
#     result = cur.execute(sql, insert_blob_tuple)
#     # print("Image and file inserted successfully as a BLOB into python_employee table", result)
#
#     # commit the transaction
#     myconn.commit()
#
# except:
#     myconn.rollback()

sql_fetch_blob_query = """SELECT * from book_data where book_id = %s"""
cur.execute(sql_fetch_blob_query, (1,))
record = cur.fetchall()
for row in record:
    print("Id = ", row[0], )
    print("Name = ", row[1])
    book_data = row[2]
    book_n = row[1]
    # print("Storing employee image and bio-data on disk \n")
    print(row[1])

app = Flask(__name__)


@app.route('/')
@app.route('/hello')
def hello():
    return render_template("indexing.html", book_name=book_n)


@app.route("/book",methods = ['POST'])
def book():
    with open("testing2.pdf", 'wb') as file:
        file.write(book_data)
    return "hello"


myconn.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
    #app.run(debug=True)
