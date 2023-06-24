import os
from flask import Flask, request, flash, jsonify
from flask_mysqldb import MySQL
from wtforms import Form, StringField, IntegerField, validators, DateTimeField
from datetime import datetime , date 
# from flask_wtf.file import FileField, FileAllowed, FileRequired


app = Flask(__name__)
app.secret_key = 'many random bytes'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_ACCOUNT'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'RMS'


class AccountForm(Form):
    type = StringField('type', [validators.InputRequired()])
    total_amount = StringField('total_amount', [validators.InputRequired()])
    payment_method = StringField('payment_method', [validators.InputRequired()])
    date = StringField('date', default=date.utcnow)
mysql = MySQL(app)

@app.route('/add_account', methods=['POST'])
def add_account():
    form = AccountForm(request.form)
    if form.validate():
        type = form.type.data
        total_amount = form.total_amount.data
        payment_method = form.payment_method.data
        date = form.date.data
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO account(type, total_amount, payment_method, date) VALUES(%s, %s, %s,%s)", (type, total_amount, payment_method, date))
        mysql.connection.commit()
        cur.close()
        response = {'code': '200', 'status': 'true', 'message': 'account added successfully'}
        return jsonify(response)
    else:
        response = {'code': '400', 'status': 'false', 'message': 'Invalid input'}
        return jsonify(response)

    
@app.route('/account/<int:account_id>', methods=['GET'])
def get_account(account_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM account WHERE id=%s", (account_id,))
    account = cur.fetchone()
    cur.close()
    if account:
        response = {'code': '200', 'status': 'true', 'data': account}
        return jsonify(response)
    else:
        response = {'code': '400', 'status': 'false', 'message': 'account not found'}
        return jsonify(response)

@app.route('/account', methods=['GET'])
def get_all_accounts():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM account")
    accounts = cur.fetchall()
    cur.close()
    response = {'code': '200', 'status': 'true', 'data': accounts}
    return jsonify(response)

@app.route('/del_account/<int:id>', methods=['DELETE'])
def delete_account(id):
    cur = mysql.connection.cursor()
    account = cur.execute(f"DELETE FROM account WHERE id={id}")
    mysql.connection.commit()
    cur.close()
    if account > 0:
        final_response = {'code': '200', 'status': 'true', 'message': 'account found', 'data': account}
        return jsonify(final_response)
    else:
        final_response = {'code': '400', 'status': 'false', 'message': 'account not found', 'data': account}
        return jsonify(final_response)


@app.route('/upd_account/<int:account_id>', methods=['PUT'])
def update_account(account_id):
    form = AccountForm(request.form)
    if form.validate():
        type = form.type.data
        total_amount = form.total_amount.data
        payment_method = form.payment_method.data
        date = form.date.data
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM account WHERE id=%s", (account_id,))
        account = cur.fetchone()
        if not account:
            cur.close()
            final_response = {'code': '404', 'status': 'false', 'message': 'account not found'}
            return jsonify(final_response)
        else:
            cur.execute("UPDATE c_account SET type=%s, total_amount=%s, payment_method=%s, date=%s WHERE id=%s", (type, total_amount, payment_method, date, account_id))
            mysql.connection.commit()
            cur.close()
            response = {'code': '200', 'status': 'true', 'message': 'account updated successfully'}
            return jsonify(response)
    else:
        final_response = {'code': '400', 'status': 'false', 'message': 'Invalid input'}
        return jsonify(final_response)


if __name__ == "__main__":
    app.run(debug=True)
