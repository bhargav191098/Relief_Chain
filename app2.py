from flask import Flask,request

from flask import jsonify
  
import MySQLdb
 
import gc

import json
   
app = Flask(__name__)
   
app.debug = True
   
# database connection method
 
def connection():
 
	conn = MySQLdb.connect(
	 
	host = "localhost",
	 
	user = "root",
	 
	passwd = "1234567890",
	 
	db = "users"
	 
	)
	 
 
 
	c = conn.cursor()
	 
	return c, conn
	   
c, con = connection()
@app.route("/")
 
def hello():
 
    return 'WUBBA LUBBA DUB DUB'

@app.route("/login",methods=['POST'])

def log():
	print(request.form['aadhar'])
	aa = request.form['aadhar']
	print(request.form['phone'])
	ph = request.form['phone']
	#return 'hello'+request.form['aadhar']
	query = 'select Phone from login where AadharID="'+aa+'"'
        c.execute(query)
	d = ""
	users = c.fetchall()
	
	for user in users:
		d = d+user[0]
	if d==ph: 
		return "1"
	else:
 		return "0"
   
 
@app.route("/get/")
 
def get_data():
   
	c.execute("SELECT * FROM login")
	 
	users = c.fetchall()
	 

	 
	 
	data = '{'
	 
	for user in users:
	
	 
		data = data + '"'+user[0]+'"' + ': ' +' "'+user[2]+'"' + ','
	 

	data = data+'"'+'12'+'"'+':'+'"'+'21'+'"'+'}'
	

	json_data = json.dumps(data)	
	 
	gc.collect()
	 

	 
	 
	return jsonify(json_data)

if __name__ == "__main__":
 
	app.run(host='0.0.0.0',port='3000',debug='True')
