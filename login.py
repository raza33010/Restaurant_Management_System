from flask import Flask, request, jsonify, render_template, redirect

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)