from flask import Flask

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
	 
	passwd = "",
	 
	db = "users"
	 
	)
	 
 
 
	c = conn.cursor()
	 
	return c, conn
	   
c, con = connection()
@app.route("/")
 
def hello():
 
    return 'WUBBA LUBBA DUB DUB'
   
 
@app.route("/get/")
 
def get_data():
   
	c.execute("SELECT * FROM login")
	 
	users = c.fetchall()
	 

	 
	 
	data = '{'
	 
	for user in users:
	
	 
		data = data + '"'+user[0]+'"' + ': ' +' "'+user[2]+'"' + ','
	 

	data = data+'"'+'12'+'"'+':'+'"'+'21'+'"'+'}'
	

		
	 
	gc.collect()
	 

	 
	 
	return jsonify(data)

if __name__ == "__main__":
 
	app.run(host='0.0.0.0',debug='True')
