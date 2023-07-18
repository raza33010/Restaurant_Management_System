import os
from flask import Flask, request, flash, jsonify, render_template, redirect
from flask_mysqldb import MySQL
from wtforms import Form, StringField, IntegerField, validators, DateTimeField, FloatField, DateField
from datetime import datetime , date 
# from flask_wtf.file import FileField, FileAllowed, FileRequired


app = Flask(__name__)
app.secret_key = 'many random bytes'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'RMS'

mysql = MySQL(app)
# login apis
@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    if email == 'useradmin@gmail.com' and password == '1234':
        # Login successful
        return redirect('/dashboard')
    else:
        # Login failed
        return redirect('/')

@app.route('/dashboard')
def dashboard():
    # Render the dashboard page after successful login
    return render_template('dashboard.html')

# menuu apis

class MenuForm(Form):
    item_name = StringField('item_name', [validators.InputRequired()])
    price = FloatField('price', [validators.InputRequired()])
    description = StringField('description', [validators.InputRequired()])
    created_at = DateTimeField('Created At', default=datetime.utcnow)
    updated_at = DateTimeField('Updated At', default=datetime.utcnow)


@app.route('/add_menu', methods=['POST'])
def add_menu():
    form = MenuForm(request.form)
    if form.validate():
        item_name = form.item_name.data
        price = form.price.data
        description = form.description.data
        created_at = form.created_at.data
        updated_at = form.updated_at.data
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO menu(item_name, price, description, created_at, updated_at) VALUES(%s, %s, %s, %s, %s)", (item_name, price, description, created_at, updated_at))
        mysql.connection.commit()
        cur.close()
        return redirect('/dashboard')
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
    response = { "data" : menus }
    return jsonify(response)
    # return render_template('dashboard.html', menu = menus)



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
        updated_at = form.updated_at.data
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM menu WHERE id=%s", (menu_id,))
        menu = cur.fetchone()
        if not menu:
            cur.close()
            final_response = {'code': '404', 'status': 'false', 'message': 'menu not found'}
            return jsonify(final_response)
        else:
            cur.execute("UPDATE menu SET item_name=%s, price=%s, description=%s, updated_at=%s WHERE id=%s", (item_name, price, description, updated_at, menu_id))
            mysql.connection.commit()
            cur.close()
            response = {'code': '200', 'status': 'true', 'message': 'menu updated successfully'}
            return jsonify(response)
    else:
        final_response = {'code': '400', 'status': 'false', 'message': 'Invalid input'}
        return jsonify(final_response)


# User APIS

class UserForm(Form):
    name = StringField('Name', [validators.InputRequired()])
    role = StringField('Role', [validators.InputRequired()])
    created_at = DateTimeField('Created At', default=datetime.utcnow)
    updated_at = DateTimeField('Updated At', default=datetime.utcnow)
    
@app.route('/add_user', methods=['POST'])
def add_user():
    form = UserForm(request.form)
    if form.validate():
        name = form.name.data
        role = form.role.data
        created_at = form.created_at.data
        updated_at = form.updated_at.data
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO user(name, role, created_at, updated_at) VALUES(%s, %s, %s, %s)", (name, role, created_at, updated_at))
        mysql.connection.commit()
        cur.close()
        return redirect('/dashboard')
    else:
        response = {'code': '400', 'status': 'false', 'message': 'Invalid input'}
        return jsonify(response)

    
@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM user WHERE id=%s", (user_id,))
    user = cur.fetchone()
    cur.close()
    if user:
        response = {'code': '200', 'status': 'true', 'data': user}
        return jsonify(response)
    else:
        response = {'code': '400', 'status': 'false', 'message': 'user not found'}
        return jsonify(response)

@app.route('/user', methods=['GET'])
def get_all_users():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM user")
    users = cur.fetchall()
    cur.close()
    response = {'code': '200', 'status': 'true', 'data': users}
    return jsonify(response)

@app.route('/del_user/<int:id>', methods=['DELETE'])
def delete_user(id):
    cur = mysql.connection.cursor()
    user = cur.execute(f"DELETE FROM user WHERE id={id}")
    mysql.connection.commit()
    cur.close()
    if user > 0:
        final_response = {'code': '200', 'status': 'true', 'message': 'user found', 'data': user}
        return jsonify(final_response)
    else:
        final_response = {'code': '400', 'status': 'false', 'message': 'user not found', 'data': user}
        return jsonify(final_response)


@app.route('/upd_user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    form = UserForm(request.form)
    if form.validate():
        name = form.name.data
        role = form.role.data
        updated_at = form.updated_at.data
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM user WHERE id=%s", (user_id,))
        user = cur.fetchone()
        if not user:
            cur.close()
            final_response = {'code': '404', 'status': 'false', 'message': 'user not found'}
            return jsonify(final_response)
        else:
            cur.execute("UPDATE user SET name=%s, role=%s, updated_at=%s WHERE id=%s", (name, role, updated_at, user_id))
            mysql.connection.commit()
            cur.close()
            response = {'code': '200', 'status': 'true', 'message': 'user updated successfully'}
            return jsonify(response)
    else:
        final_response = {'code': '400', 'status': 'false', 'message': 'Invalid input'}
        return jsonify(final_response)

# Customer Apis
class CustomerForm(Form):
    user_id = IntegerField('Name', [validators.InputRequired()])
    phone = IntegerField('Role', [validators.InputRequired()])
    address = StringField('address', [validators.InputRequired()])
    created_at = DateTimeField('Created At', default=datetime.utcnow)
    updated_at = DateTimeField('Updated At', default=datetime.utcnow)
    
@app.route('/add_customer', methods=['POST'])
def add_customer():
    form = CustomerForm(request.form)
    if form.validate():
        user_id = form.user_id.data
        phone = form.phone.data
        address = form.address.data
        created_at = form.created_at.data
        updated_at = form.updated_at.data
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO customer(user_id, phone, address, created_at, updated_at) VALUES(%s, %s, %s, %s, %s)", (user_id, phone, address, created_at, updated_at))
        mysql.connection.commit()
        cur.close()
        return redirect('/dashboard')
    else:
        response = {'code': '400', 'status': 'false', 'message': 'Invalid input'}
        return jsonify(response)

    
@app.route('/customer/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM customer WHERE id=%s", (customer_id,))
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

@app.route('/del_customer/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    cur = mysql.connection.cursor()
    customer = cur.execute(f"DELETE FROM customer WHERE id={customer_id}")
    mysql.connection.commit()
    cur.close()
    if customer > 0:
        final_response = {'code': '200', 'status': 'true', 'message': 'customer found', 'data': customer}
        return jsonify(final_response)
    else:
        final_response = {'code': '400', 'status': 'false', 'message': 'customer not found', 'data': customer}
        return jsonify(final_response)


@app.route('/upd_customer/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    form = CustomerForm(request.form)
    if form.validate():
        user_id = form.user_id.data
        phone = form.phone.data
        address = form.address.data
        updated_at = form.updated_at.data
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM customer WHERE   id=%s", (customer_id,))
        customer = cur.fetchone()
        if not customer:
            cur.close()
            final_response = {'code': '404', 'status': 'false', 'message': 'customer not found'}
            return jsonify(final_response)
        else:
            cur.execute("UPDATE customer SET  user_id=%s, phone=%s, address=%s, updated_at=%s WHERE id=%s", (user_id, phone, address, updated_at, customer_id))
            mysql.connection.commit()
            cur.close()
            response = {'code': '200', 'status': 'true', 'message': 'customer updated successfully'}
            return jsonify(response)
    else:
        final_response = {'code': '400', 'status': 'false', 'message': 'Invalid input'}
        return jsonify(final_response)

# Employee APis

class EmployeeForm(Form):
    user_id = IntegerField('user_id', [validators.InputRequired()])
    category = StringField('category', [validators.InputRequired()])
    salary = IntegerField('salary', [validators.InputRequired()])
    created_at = DateTimeField('Created At', default=datetime.utcnow)
    updated_at = DateTimeField('Updated At', default=datetime.utcnow)

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
        return redirect('/dashboard')
    else:
        response = {'code': '400', 'status': 'false', 'message': 'Invalid input'}
        return jsonify(response)

    
@app.route('/employee/<int:employee_id>', methods=['GET'])
def get_employee(employee_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM employee WHERE id=%s", (employee_id,))
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

@app.route('/del_employee/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    cur = mysql.connection.cursor()
    employee = cur.execute(f"DELETE FROM employee WHERE id={employee_id}")
    mysql.connection.commit()
    cur.close()
    if employee > 0:
        final_response = {'code': '200', 'status': 'true', 'message': 'employee found', 'data': employee}
        return jsonify(final_response)
    else:
        final_response = {'code': '400', 'status': 'false', 'message': 'employee not found', 'data': employee}
        return jsonify(final_response)


@app.route('/upd_employee/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    form = EmployeeForm(request.form)
    if form.validate():
        user_id = form.user_id.data
        category = form.category.data
        salary = form.salary.data
        updated_at = form.updated_at.data
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM employee WHERE id=%s", (employee_id,))
        employee = cur.fetchone()
        if not employee:
            cur.close()
            final_response = {'code': '404', 'status': 'false', 'message': 'employee not found'}
            return jsonify(final_response)
        else:
            cur.execute("UPDATE employee SET user_id=%s, category=%s, salary=%s, updated_at=%s WHERE id=%s", (user_id, category, salary, updated_at, employee_id))
            mysql.connection.commit()
            cur.close()
            response = {'code': '200', 'status': 'true', 'message': 'employee updated successfully'}
            return jsonify(response)
    else:
        final_response = {'code': '400', 'status': 'false', 'message': 'Invalid input'}
        return jsonify(final_response)

# Bill Apis

class BillForm(Form):
    order_id = IntegerField('order_id', [validators.InputRequired()])
    total_amount = IntegerField('total_amount', [validators.InputRequired()])
    payment_status = StringField('payment_status', [validators.InputRequired()])
    created_at = DateTimeField('Created At', default=datetime.utcnow)
    updated_at = DateTimeField('Updated At', default=datetime.utcnow)

@app.route('/add_bill', methods=['POST'])
def add_bill():
    form = BillForm(request.form)
    if form.validate():
        order_id = form.order_id.data
        total_amount = form.total_amount.data
        payment_status = form.payment_status.data
        created_at = form.created_at.data
        updated_at = form.updated_at.data
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO bill(order_id, total_amount, payment_status, created_at, updated_at) VALUES(%s, %s, %s, %s, %s)", (order_id, total_amount, payment_status, created_at, updated_at))
        mysql.connection.commit()
        cur.close()
        return redirect('/dashboard')
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
        updated_at = form.updated_at.data
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM bill WHERE id=%s", (bill_id,))
        bill = cur.fetchone()
        if not bill:
            cur.close()
            final_response = {'code': '404', 'status': 'false', 'message': 'bill not found'}
            return jsonify(final_response)
        else:
            cur.execute("UPDATE bill SET order_id=%s, total_amount=%s, payment_status=%s, updated_at=%s WHERE id=%s", (order_id, total_amount, payment_status, updated_at,bill_id))
            mysql.connection.commit()
            cur.close()
            response = {'code': '200', 'status': 'true', 'message': 'bill updated successfully'}
            return jsonify(response)
    else:
        final_response = {'code': '400', 'status': 'false', 'message': 'Invalid input'}
        return jsonify(final_response)

# Order Apis

class OrderForm(Form):
    emp_id = IntegerField('emp_id', [validators.InputRequired()])
    cust_id = IntegerField('cust_id', [validators.InputRequired()])
    order_date = DateField('order_date', [validators.InputRequired()])
    order_item = StringField('order_item', [validators.InputRequired()])
    quantity = IntegerField('quantity', [validators.InputRequired()])
    price = FloatField('price', [validators.InputRequired()])
    description = StringField('description', [validators.InputRequired()])
    order_status = StringField('status', [validators.InputRequired()])
    created_at = DateTimeField('Created At', default=datetime.utcnow)
    updated_at = DateTimeField('Updated At', default=datetime.utcnow)


@app.route('/add_order', methods=['POST'])
def add_order():
    form = OrderForm(request.form)
    if form.validate():
        emp_id = form.emp_id.data
        cust_id = form.cust_id.data
        order_date = form.order_date.data
        order_item = form.order_item.data
        quantity = form.quantity.data
        price = form.price.data
        description = form.description.data
        order_status = form.order_status.data
        created_at = form.created_at.data
        updated_at = form.updated_at.data
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO orders(emp_id, cust_id, order_date, order_item, quantity, price ,description, order_status, created_at, updated_at) VALUES(%s, %s, %s,  %s,  %s,  %s,  %s,  %s, %s,  %s)",
                     (emp_id, cust_id, order_date, order_item, quantity, price, description, order_status, created_at, updated_at))
        mysql.connection.commit()
        cur.close()
        return redirect('/dashboard')
    else:
        response = {'code': '400', 'status': 'false', 'message': 'Invalid input'}
        return jsonify(response)

    
@app.route('/order/<int:order_id>', methods=['GET'])
def get_order(order_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM orders WHERE id=%s", (order_id,))
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
    cur.execute("SELECT * FROM orders")
    orders = cur.fetchall()
    cur.close()
    response = {'code': '200', 'status': 'true', 'data': orders}
    return jsonify(response)

@app.route('/del_order/<int:id>', methods=['DELETE'])
def delete_order(id):
    cur = mysql.connection.cursor()
    order = cur.execute(f"DELETE FROM orders WHERE id={id}")
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
        emp_id = form.emp_id.data
        cust_id = form.cust_id.data
        order_date = form.order_date.data
        order_item = form.order_item.data
        quantity = form.quantity.data
        price = form.price.data
        description = form.description.data
        order_status = form.order_status.data
        updated_at = form.updated_at.data

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM orders WHERE id=%s", (order_id,))
        order = cur.fetchone()
        if not order:
            cur.close()
            final_response = {'code': '404', 'status': 'false', 'message': 'order not found'}
            return jsonify(final_response)
        else:
            cur.execute("UPDATE orders SET emp_id=%s, cust_id=%s, order_date=%s, order_item=%s, quantity=%s, price=%s, description=%s, order_status=%s, updated_at=%s WHERE id=%s", 
                        (emp_id, cust_id, order_date, order_item, quantity, price, description, order_status, updated_at, order_id))
            mysql.connection.commit()
            cur.close()
            response = {'code': '200', 'status': 'true', 'message': 'order updated successfully'}
            return jsonify(response)
    else:
        final_response = {'code': '400', 'status': 'false', 'message': 'Invalid input'}
        return jsonify(final_response)

# Stock Apis

class StockForm(Form):
    menu_item = StringField('menu_item', [validators.InputRequired()])
    quantity = IntegerField('quantity', [validators.InputRequired()])
    created_at = DateTimeField('Created At', default=datetime.utcnow)
    updated_at = DateTimeField('Updated At', default=datetime.utcnow)

@app.route('/add_stock', methods=['POST'])
def add_stock():
    form = StockForm(request.form)
    if form.validate():
        menu_item = form.menu_item.data
        quantity = form.quantity.data
        created_at = form.created_at.data
        updated_at = form.updated_at.data
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO stock(menu_item, quantity, created_at, updated_at) VALUES(%s, %s, %s, %s)", (menu_item, quantity, created_at, updated_at))
        mysql.connection.commit()
        cur.close()
        return redirect('/dashboard')
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
        updated_at = form.updated_at.data
        
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM stock WHERE id=%s", (stock_id,))
        stock = cur.fetchone()
        if not stock:
            cur.close()
            final_response = {'code': '404', 'status': 'false', 'message': 'stock not found'}
            return jsonify(final_response)
        else:
            cur.execute("UPDATE stock SET menu_item=%s, quantity=%s, updated_at=%s WHERE id=%s", (menu_item, quantity, updated_at, stock_id))
            mysql.connection.commit()
            cur.close()
            response = {'code': '200', 'status': 'true', 'message': 'stock updated successfully'}
            return jsonify(response)
    else:
        final_response = {'code': '400', 'status': 'false', 'message': 'Invalid input'}
        return jsonify(final_response)



if __name__ == "__main__":
    app.run(debug=True)
