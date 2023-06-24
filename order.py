import os
from flask import Flask, request, flash, jsonify
from flask_mysqldb import MySQL
from wtforms import Form, StringField, IntegerField, validators, DateTimeField
from datetime import datetime , date 
# from flask_wtf.file import FileField, FileAllowed, FileRequired


app = Flask(__name__)
app.secret_key = 'many random bytes'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_ORDER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'RMS'


class OrderForm(Form):
    employee_id = StringField('employee_id', [validators.InputRequired()])
    cust_id = StringField('cust_id', [validators.InputRequired()])
    order_date = StringField('order_date', default=date.utcnow)
    order_item = StringField('order_item', [validators.InputRequired()])
    quantity = StringField('quantity', [validators.InputRequired()])
    price = StringField('price', [validators.InputRequired()])
    description = StringField('description', [validators.InputRequired()])
    order_status = StringField('status', [validators.InputRequired()])
   

mysql = MySQL(app)

@app.route('/add_order', methods=['POST'])
def add_order():
    form = OrderForm(request.form)
    if form.validate():
        employee_id = form.employee_id.data
        cust_id = form.cust_id.data
        order_date = form.order_date.data
        order_item = form.order_item.data
        quantity = form.quantity.data
        price = form.price.data
        description = form.description.data
        order_status = form.order_status.data
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO order(employee_id, cust_id, order_date, order_item, quantity, price ,description, order_status) VALUES(%s, %s, %s,  %s,  %s,  %s,  %s,  %s)",
                     (employee_id, cust_id, order_date, order_item, quantity, price, description, order_status))
        mysql.connection.commit()
        cur.close()
        response = {'code': '200', 'status': 'true', 'message': 'order added successfully'}
        return jsonify(response)
    else:
        response = {'code': '400', 'status': 'false', 'message': 'Invalid input'}
        return jsonify(response)

    
@app.route('/order/<int:order_id>', methods=['GET'])
def get_order(order_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM order WHERE id=%s", (order_id,))
    order = cur.fetchone()
    cur.close()
    if order:
        response = {'code': '200', 'status': 'true', 'data': order}
        return jsonify(response)
    else:
        response = {'code': '400', 'status': 'false', 'message': 'order not found'}
        return jsonify(response)

@app.route('/order', methods=['GET'])
def get_all_orders():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM order")
    orders = cur.fetchall()
    cur.close()
    response = {'code': '200', 'status': 'true', 'data': orders}
    return jsonify(response)

@app.route('/del_order/<int:id>', methods=['DELETE'])
def delete_order(id):
    cur = mysql.connection.cursor()
    order = cur.execute(f"DELETE FROM order WHERE id={id}")
    mysql.connection.commit()
    cur.close()
    if order > 0:
        final_response = {'code': '200', 'status': 'true', 'message': 'order found', 'data': order}
        return jsonify(final_response)
    else:
        final_response = {'code': '400', 'status': 'false', 'message': 'order not found', 'data': order}
        return jsonify(final_response)


@app.route('/upd_order/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    form = OrderForm(request.form)
    if form.validate():
        employee_id = form.employee_id.data
        cust_id = form.cust_id.data
        order_date = form.order_date.data
        order_item = form.order_item.data
        quantity = form.quantity.data
        price = form.price.data
        description = form.description.data
        order_status = form.order_status.data


        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM order WHERE id=%s", (order_id,))
        order = cur.fetchone()
        if not order:
            cur.close()
            final_response = {'code': '404', 'status': 'false', 'message': 'order not found'}
            return jsonify(final_response)
        else:
            cur.execute("UPDATE c_order SET employee_id=%s, cust_id=%s, order_date=%s, order_item=%s, quantity=%s, price=%s, description=%s, order_status=%s,  WHERE id=%s", 
                        (employee_id, cust_id, order_date, order_item, quantity, price, description, order_status))
            mysql.connection.commit()
            cur.close()
            response = {'code': '200', 'status': 'true', 'message': 'order updated successfully'}
            return jsonify(response)
    else:
        final_response = {'code': '400', 'status': 'false', 'message': 'Invalid input'}
        return jsonify(final_response)


if __name__ == "__main__":
    app.run(debug=True)
