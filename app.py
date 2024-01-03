from flask import Flask,jsonify,request
import sqlite3
from flask_httpauth import HTTPBasicAuth

app=Flask(__name__)
auth=HTTPBasicAuth()

users={"rashmi":"123456789"}

@auth.verify_password
def verify_password(username,password):
    if username in users and users[username]==password:
        return username


# Create a route to get all the data from the database
@app.route('/emp_data',methods=['GET'])
def get_data():
    try:
        conn=sqlite3.connect("employee.db")
        cur=conn.cursor()
        cur.execute("SELECT * FROM Employees")
        data=cur.fetchall()
        return jsonify(data)
    finally:
        cur.close()

#Create a route to get data based on a specific ID
@app.route('/emp_data/<int:id>',methods=['GET'])
def get_data_by_id(id):
    try:
        conn=sqlite3.connect("employee.db")
        cur=conn.cursor()
        cur.execute(f'SELECT * FROM Employees WHERE ID={id}')
        data=cur.fetchall()
        return jsonify(data)
    finally:
        cur.close()

#Create a route to add data to the database
@app.route('/add_emp_data',methods=['POST'])
@auth.login_required
def add_emp():
    try:
        conn=sqlite3.connect("employee.db")
       
        request_data=request.get_json()
       
        
        with sqlite3.connect("employee.db") as con:  
            cur=conn.cursor() 
            cur.execute("insert into Employees(name,age,email,address,contact) values (?,?,?,?,?)",
                        (request_data["name"],request_data["age"],request_data["email"],request_data["address"],request_data["contact"]))
            conn.commit()
        return {"message": "New employee added"}, 201
    except KeyError:
        conn.rollback
        msg="We can not add employee"
    finally:
        conn.close()



#Create a route to update data in the database
@app.route('/update_emp/<int:id>',methods=['PUT'])
def update_emp(id):
    try:
        conn=sqlite3.connect("employee.db")
        cur=conn.cursor()
        request_data=request.get_json()
        email=request_data["email"]
        cur.execute(f'UPDATE Employees SET email={email} where id={id}')
        conn.commit()
        return{"message":"Data updated successfully"}
    finally:
        conn.close()
        

#Create a route to delete data from the database
@app.route('/delete_emp/<int:id>',methods=['DELETE'])
def delete_emp(id):
    try:
        conn=sqlite3.connect("employee.db")
        cur=conn.cursor()
        cur.execute(f'DELETE FROM Employees where id={id}')
        conn.commit()
        return{"message":"Employee deleted successfully"}
    finally:
        conn.close()


if __name__=="__main__":
    app.run(debug=True)