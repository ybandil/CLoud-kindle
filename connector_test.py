from io import BytesIO
from wsgiref.util import FileWrapper

import mysql.connector
from flask import Flask, jsonify, render_template, send_file, request

# Create the connection object
myconn = mysql.connector.connect(host="kindletestdata.czend6kabecw.ap-south-1.rds.amazonaws.com", user="admin",
                                 passwd="Yashcse1", database="Kindlebookdata")

# printing the connection object
print(myconn)

# creating the cursor object
cur = myconn.cursor()

# sql = "insert into book_data(book_id,book_name,book_pdf) values (%s, %s, %s)"
#
# with open("customer.pdf", 'rb') as file:
#     binaryData = file.read()
#
# empPicture = binaryData
# # Convert data into tuple format
# insert_blob_tuple = (3, "short_stories", empPicture)
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

sql_fetch_blob_query = """SELECT book_name from book_data"""
cur.execute(sql_fetch_blob_query)
record = cur.fetchall()
print(len(record))
name1 = []
for row in record:
    name1.append(row[0])
    # print("Name = ", row[1])
    # book_data = row[2]
    # book_n = row[1]
    # print("Storing employee image and bio-data on disk \n")
    # print(row[1])

print(name1)
app = Flask(__name__)


@app.route('/')
@app.route('/hello')
def hello():
    return render_template("indexing.html", book_name=name1)


@app.route('/book', methods=['POST'])
def book():
    print("ram")
    select = request.form.get("test")
    print(select)

    # print("Storing employee image and bio-data on disk \n"
    return render_template("indexing2.html", filename=select)


@app.route('/image_route/<filename>')
def image_route(filename):
    myconn._open_connection()
    cur1 = myconn.cursor()
    sql_fetch_blob_quer = """SELECT book_pdf from book_data where book_name = %s"""
    cur1.execute(sql_fetch_blob_quer, (filename,))
    recor = cur1.fetchall()
    for ro in recor:
        boo_data = ro[0]
    bytes_io = BytesIO(boo_data)
    print("----------------------------")
    return send_file(bytes_io, download_name=filename + ".pdf", mimetype="application/pdf")


myconn.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
    # app.run(debug=True)
