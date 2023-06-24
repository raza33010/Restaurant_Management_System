import os
from flask import Flask, request, flash, jsonify
from flask_mysqldb import MySQL
from wtforms import Form, StringField, IntegerField, validators, DateTimeField
from datetime import datetime , date 
# from flask_wtf.file import FileField, FileAllowed, FileRequired


app = Flask(__name__)
app.secret_key = 'many random bytes'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_STOCK'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'RMS'


class StockForm(Form):
    menu_item = StringField('menu_item', [validators.InputRequired()])
    quantity = StringField('quantity', [validators.InputRequired()])

mysql = MySQL(app)

@app.route('/add_stock', methods=['POST'])
def add_stock():
    form = StockForm(request.form)
    if form.validate():
        menu_item = form.menu_item.data
        quantity = form.quantity.data
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO stock(menu_item, quantity) VALUES(%s, %s, %s)", (menu_item, quantity))
        mysql.connection.commit()
        cur.close()
        response = {'code': '200', 'status': 'true', 'message': 'stock added successfully'}
        return jsonify(response)
    else:
        response = {'code': '400', 'status': 'false', 'message': 'Invalid input'}
        return jsonify(response)

    
@app.route('/stock/<int:stock_id>', methods=['GET'])
def get_stock(stock_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM stock WHERE id=%s", (stock_id,))
    stock = cur.fetchone()
    cur.close()
    if stock:
        response = {'code': '200', 'status': 'true', 'data': stock}
        return jsonify(response)
    else:
        response = {'code': '400', 'status': 'false', 'message': 'stock not found'}
        return jsonify(response)

@app.route('/stock', methods=['GET'])
def get_all_stocks():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM stock")
    stocks = cur.fetchall()
    cur.close()
    response = {'code': '200', 'status': 'true', 'data': stocks}
    return jsonify(response)

@app.route('/del_stock/<int:id>', methods=['DELETE'])
def delete_stock(id):
    cur = mysql.connection.cursor()
    stock = cur.execute(f"DELETE FROM stock WHERE id={id}")
    mysql.connection.commit()
    cur.close()
    if stock > 0:
        final_response = {'code': '200', 'status': 'true', 'message': 'stock found', 'data': stock}
        return jsonify(final_response)
    else:
        final_response = {'code': '400', 'status': 'false', 'message': 'stock not found', 'data': stock}
        return jsonify(final_response)


@app.route('/upd_stock/<int:stock_id>', methods=['PUT'])
def update_stock(stock_id):
    form = StockForm(request.form)
    if form.validate():
        menu_item = form.menu_item.data
        quantity = form.quantity.data
        
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM stock WHERE id=%s", (stock_id,))
        stock = cur.fetchone()
        if not stock:
            cur.close()
            final_response = {'code': '404', 'status': 'false', 'message': 'stock not found'}
            return jsonify(final_response)
        else:
            cur.execute("UPDATE c_stock SET menu_item=%s, quantity=%s WHERE id=%s", (item_name, menu_item, stock_id))
            mysql.connection.commit()
            cur.close()
            response = {'code': '200', 'status': 'true', 'message': 'stock updated successfully'}
            return jsonify(response)
    else:
        final_response = {'code': '400', 'status': 'false', 'message': 'Invalid input'}
        return jsonify(final_response)


if __name__ == "__main__":
    app.run(debug=True)
