import os
from flask import Flask, request, flash, jsonify
from flask_mysqldb import MySQL
from wtforms import Form, StringField, IntegerField, validators, DateTimeField
from datetime import datetime
# from flask_wtf.file import FileField, FileAllowed, FileRequired


app = Flask(__name__)
app.secret_key = 'many random bytes'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_CUSTOMER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'RMS'


class CustomerForm(Form):
    user_id = StringField('Name', [validators.InputRequired()])
    phone = StringField('Role', [validators.InputRequired()])
    address = StringField('address', [validators.InputRequired()])

mysql = MySQL(app)

@app.route('/add_customer', methods=['POST'])
def add_customer():
    form = CustomerForm(request.form)
    if form.validate():
        user_id = form.user_id.data
        phone = form.phone.data
        address = form.address.data
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO customer(user_id, phone, address) VALUES(%s, %s, %s)", (user_id, phone, address ))
        mysql.connection.commit()
        cur.close()
        response = {'code': '200', 'status': 'true', 'message': 'customer added successfully'}
        return jsonify(response)
    else:
        response = {'code': '400', 'status': 'false', 'message': 'Invalid input'}
        return jsonify(response)

    
@app.route('/customer/<int:customer_user_id>', methods=['GET'])
def get_customer(customer_user_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM customer WHERE user_id=%s", (customer_user_id,))
    customer = cur.fetchone()
    cur.close()
    if customer:
        response = {'code': '200', 'status': 'true', 'data': customer}
        return jsonify(response)
    else:
        response = {'code': '400', 'status': 'false', 'message': 'customer not found'}
        return jsonify(response)

@app.route('/customer', methods=['GET'])
def get_all_customers():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM customer")
    customers = cur.fetchall()
    cur.close()
    response = {'code': '200', 'status': 'true', 'data': customers}
    return jsonify(response)

@app.route('/del_customer/<int:user_id>', methods=['DELETE'])
def delete_customer(user_id):
    cur = mysql.connection.cursor()
    customer = cur.execute(f"DELETE FROM customer WHERE user_id={user_id}")
    mysql.connection.commit()
    cur.close()
    if customer > 0:
        final_response = {'code': '200', 'status': 'true', 'message': 'customer found', 'data': customer}
        return jsonify(final_response)
    else:
        final_response = {'code': '400', 'status': 'false', 'message': 'customer not found', 'data': customer}
        return jsonify(final_response)


@app.route('/upd_customer/<int:customer_user_id>', methods=['PUT'])
def update_customer(customer_user_id):
    form = CustomerForm(request.form)
    if form.validate():
        user_id = form.user_id.data
        phone = form.phone.data
        address = form.address.data
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM customer WHERE user_id=%s", (customer_user_id,))
        customer = cur.fetchone()
        if not customer:
            cur.close()
            final_response = {'code': '404', 'status': 'false', 'message': 'customer not found'}
            return jsonify(final_response)
        else:
            cur.execute("UPDATE c_customer SET name=%s, role=%s, updated_at=%s WHERE user_id=%s", (user_id, phone, address, customer_user_id))
            mysql.connection.commit()
            cur.close()
            response = {'code': '200', 'status': 'true', 'message': 'customer updated successfully'}
            return jsonify(response)
    else:
        final_response = {'code': '400', 'status': 'false', 'message': 'Invalid input'}
        return jsonify(final_response)


if __name__ == "__main__":
    app.run(debug=True)
