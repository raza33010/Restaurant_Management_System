import os
from flask import Flask, request, flash, jsonify
from flask_mysqldb import MySQL
from wtforms import Form, StringField, IntegerField, validators, DateTimeField
from datetime import datetime , date 
# from flask_wtf.file import FileField, FileAllowed, FileRequired


app = Flask(__name__)
app.secret_key = 'many random bytes'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_BILL'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'RMS'


class BillForm(Form):
    order_id = StringField('order_id', [validators.InputRequired()])
    total_amount = StringField('total_amount', [validators.InputRequired()])
    payment_status = StringField('payment_status', [validators.InputRequired()])
mysql = MySQL(app)

@app.route('/add_bill', methods=['POST'])
def add_bill():
    form = BillForm(request.form)
    if form.validate():
        order_id = form.order_id.data
        total_amount = form.total_amount.data
        payment_status = form.payment_status.data
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO bill(order_id, total_amount, payment_status) VALUES(%s, %s, %s)", (order_id, total_amount, payment_status))
        mysql.connection.commit()
        cur.close()
        response = {'code': '200', 'status': 'true', 'message': 'bill added successfully'}
        return jsonify(response)
    else:
        response = {'code': '400', 'status': 'false', 'message': 'Invalid input'}
        return jsonify(response)

    
@app.route('/bill/<int:bill_id>', methods=['GET'])
def get_bill(bill_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM bill WHERE id=%s", (bill_id,))
    bill = cur.fetchone()
    cur.close()
    if bill:
        response = {'code': '200', 'status': 'true', 'data': bill}
        return jsonify(response)
    else:
        response = {'code': '400', 'status': 'false', 'message': 'bill not found'}
        return jsonify(response)

@app.route('/bill', methods=['GET'])
def get_all_bills():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM bill")
    bills = cur.fetchall()
    cur.close()
    response = {'code': '200', 'status': 'true', 'data': bills}
    return jsonify(response)

@app.route('/del_bill/<int:id>', methods=['DELETE'])
def delete_bill(id):
    cur = mysql.connection.cursor()
    bill = cur.execute(f"DELETE FROM bill WHERE id={id}")
    mysql.connection.commit()
    cur.close()
    if bill > 0:
        final_response = {'code': '200', 'status': 'true', 'message': 'bill found', 'data': bill}
        return jsonify(final_response)
    else:
        final_response = {'code': '400', 'status': 'false', 'message': 'bill not found', 'data': bill}
        return jsonify(final_response)


@app.route('/upd_bill/<int:bill_id>', methods=['PUT'])
def update_bill(bill_id):
    form = BillForm(request.form)
    if form.validate():
        order_id = form.order_id.data
        total_amount = form.total_amount.data
        payment_status = form.payment_status.data
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM bill WHERE id=%s", (bill_id,))
        bill = cur.fetchone()
        if not bill:
            cur.close()
            final_response = {'code': '404', 'status': 'false', 'message': 'bill not found'}
            return jsonify(final_response)
        else:
            cur.execute("UPDATE c_bill SET order_id=%s, total_amount=%s, payment_system=%s WHERE id=%s", (order_id, total_amount, payment_status, bill_id))
            mysql.connection.commit()
            cur.close()
            response = {'code': '200', 'status': 'true', 'message': 'bill updated successfully'}
            return jsonify(response)
    else:
        final_response = {'code': '400', 'status': 'false', 'message': 'Invalid input'}
        return jsonify(final_response)


if __name__ == "__main__":
    app.run(debug=True)
