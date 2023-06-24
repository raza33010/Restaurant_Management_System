import os
from flask import Flask, request, flash, jsonify
from flask_mysqldb import MySQL
from wtforms import Form, StringField, IntegerField, validators, DateTimeField
from datetime import datetime
# from flask_wtf.file import FileField, FileAllowed, FileRequired


app = Flask(__name__)
app.secret_key = 'many random bytes'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_EMPLOYEE'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'RMS'


class EmployeeForm(Form):
    user_id = IntegerField('user_id', [validators.InputRequired()])
    category = StringField('category', [validators.InputRequired()])
    salary = IntegerField('salary', [validators.InputRequired()])
    created_at = DateTimeField('Created At', default=datetime.utcnow)
    updated_at = DateTimeField('Updated At', default=datetime.utcnow)
    
mysql = MySQL(app)

@app.route('/add_employee', methods=['POST'])
def add_employee():
    form = EmployeeForm(request.form)
    if form.validate():
        user_id = form.user_id.data
        category = form.category.data
        salary = form.salary.data
        created_at = form.created_at.data
        updated_at = form.updated_at.data
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO employee(user_id, category, salary, created_at, updated_at) VALUES(%s, %s, %s, %s, %s)", (user_id, category, salary, created_at, updated_at))
        mysql.connection.commit()
        cur.close()
        response = {'code': '200', 'status': 'true', 'message': 'employee added successfully'}
        return jsonify(response)
    else:
        response = {'code': '400', 'status': 'false', 'message': 'Invalid input'}
        return jsonify(response)

    
@app.route('/employee/<int:employee_user_id>', methods=['GET'])
def get_employee(employee_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM employee WHERE user_id=%s", (employee_id,))
    employee = cur.fetchone()
    cur.close()
    if employee:
        response = {'code': '200', 'status': 'true', 'data': employee}
        return jsonify(response)
    else:
        response = {'code': '400', 'status': 'false', 'message': 'employee not found'}
        return jsonify(response)

@app.route('/employee', methods=['GET'])
def get_all_employees():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM employee")
    employees = cur.fetchall()
    cur.close()
    response = {'code': '200', 'status': 'true', 'data': employees}
    return jsonify(response)

@app.route('/del_employee/<int:user_id>', methods=['DELETE'])
def delete_employee(user_id):
    cur = mysql.connection.cursor()
    employee = cur.execute(f"DELETE FROM employee WHERE user_id={user_id}")
    mysql.connection.commit()
    cur.close()
    if employee > 0:
        final_response = {'code': '200', 'status': 'true', 'message': 'employee found', 'data': employee}
        return jsonify(final_response)
    else:
        final_response = {'code': '400', 'status': 'false', 'message': 'employee not found', 'data': employee}
        return jsonify(final_response)


@app.route('/upd_employee/<int:employee_user_id>', methods=['PUT'])
def update_employee(employee_id):
    form = EmployeeForm(request.form)
    if form.validate():
        user_id = form.user_id.data
        category = form.category.data
        salary = form.salary.data
        updated_at = form.updated_at.data
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM employee WHERE user_id=%s", (employee_id,))
        employee = cur.fetchone()
        if not employee:
            cur.close()
            final_response = {'code': '404', 'status': 'false', 'message': 'employee not found'}
            return jsonify(final_response)
        else:
            cur.execute("UPDATE c_employee SET name=%s, role=%s, updated_at=%s, updated_at=%s WHERE user_id=%s", (user_id, category, salary, updated_at, employee_id))
            mysql.connection.commit()
            cur.close()
            response = {'code': '200', 'status': 'true', 'message': 'employee updated successfully'}
            return jsonify(response)
    else:
        final_response = {'code': '400', 'status': 'false', 'message': 'Invalid input'}
        return jsonify(final_response)


if __name__ == "__main__":
    app.run(debug=True)
