import array
from ast import Constant
from os import name
from flask import Flask,request,jsonify
from flask_cors import CORS, cross_origin
import mysql.connector as con
from numpy import char

# render_template,

mydb= con.connect(host="localhost",user="root",password="mom@dad",database="khush")
cur=mydb.cursor()


app=Flask(__name__) #obj declare
CORS(app, support_credentials=True) #cros and origin

@app.route('/')
def hello():
    return "welcome to page"
@app.route('/select_frist')
def select():
    cur.execute("SELECT * FROM online")
    data = cur.fetchall()  # Fetch all rows from the result set

    # Convert the fetched data into a list of dictionaries
    result = []
    for row in data:
        # Assuming the first column is 'id' and the second column is 'name'
        result.append({"id": row[0], "name": row[1]})  # Adjust column indexes accordingly

    return jsonify({"data": result})

   
    
@app.route('/insert-data', methods=['POST']) #make api is getdata change in insert update,payment etc;
def json_example():
    request_data = request.get_json() 
    bname=request_data['namek']
    bsurname=request_data['surnamek']
    cur.execute("INSERT INTO online (num,na) VALUES (%s, %s)", (bname, bsurname))

    mydb.commit() 
    data={
      "status":"success run"  #print into network
    }


    return jsonify(data) #lib used to convert obj to string

app.run(debug=True)
