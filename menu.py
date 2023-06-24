import os
from flask import Flask, request, flash, jsonify
from flask_mysqldb import MySQL
from wtforms import Form, StringField, IntegerField, validators, DateTimeField
from datetime import datetime , date 
# from flask_wtf.file import FileField, FileAllowed, FileRequired


app = Flask(__name__)
app.secret_key = 'many random bytes'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_MENU'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'RMS'


class MenuForm(Form):
    item_name = StringField('item_name', [validators.InputRequired()])
    price = StringField('price', [validators.InputRequired()])
    description = StringField('description', [validators.InputRequired()])
mysql = MySQL(app)

@app.route('/add_menu', methods=['POST'])
def add_menu():
    form = MenuForm(request.form)
    if form.validate():
        item_name = form.item_name.data
        price = form.price.data
        description = form.payment_status.data
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO menu(item_name, price, description) VALUES(%s, %s, %s)", (item_name, price, description))
        mysql.connection.commit()
        cur.close()
        response = {'code': '200', 'status': 'true', 'message': 'menu added successfully'}
        return jsonify(response)
    else:
        response = {'code': '400', 'status': 'false', 'message': 'Invalid input'}
        return jsonify(response)

    
@app.route('/menu/<int:menu_id>', methods=['GET'])
def get_menu(menu_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM menu WHERE id=%s", (menu_id,))
    menu = cur.fetchone()
    cur.close()
    if menu:
        response = {'code': '200', 'status': 'true', 'data': menu}
        return jsonify(response)
    else:
        response = {'code': '400', 'status': 'false', 'message': 'menu not found'}
        return jsonify(response)

@app.route('/menu', methods=['GET'])
def get_all_menus():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM menu")
    menus = cur.fetchall()
    cur.close()
    response = {'code': '200', 'status': 'true', 'data': menus}
    return jsonify(response)

@app.route('/del_menu/<int:id>', methods=['DELETE'])
def delete_menu(id):
    cur = mysql.connection.cursor()
    menu = cur.execute(f"DELETE FROM menu WHERE id={id}")
    mysql.connection.commit()
    cur.close()
    if menu > 0:
        final_response = {'code': '200', 'status': 'true', 'message': 'menu found', 'data': menu}
        return jsonify(final_response)
    else:
        final_response = {'code': '400', 'status': 'false', 'message': 'menu not found', 'data': menu}
        return jsonify(final_response)


@app.route('/upd_menu/<int:menu_id>', methods=['PUT'])
def update_menu(menu_id):
    form = MenuForm(request.form)
    if form.validate():
        item_name = form.item_name.data
        price = form.price.data
        description = form.description.data
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM menu WHERE id=%s", (menu_id,))
        menu = cur.fetchone()
        if not menu:
            cur.close()
            final_response = {'code': '404', 'status': 'false', 'message': 'menu not found'}
            return jsonify(final_response)
        else:
            cur.execute("UPDATE c_menu SET item_name=%s, price=%s, description=%s WHERE id=%s", (item_name, price, description, menu_id))
            mysql.connection.commit()
            cur.close()
            response = {'code': '200', 'status': 'true', 'message': 'menu updated successfully'}
            return jsonify(response)
    else:
        final_response = {'code': '400', 'status': 'false', 'message': 'Invalid input'}
        return jsonify(final_response)


if __name__ == "__main__":
    app.run(debug=True)
