from flask import Flask,jsonify
import sqlite3

app=Flask(__name__)




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


if __name__=="__main__":
    app.run(debug=True)