from flask import Flask, redirect, request, url_for, render_template, make_response
import hashlib

app = Flask(__name__)
app.secret_key = 'super_secret_key'

users = {
    "alice": { "name" : "Alice", "pass": "alice123"},
    "dave": { "name" : "Dave", "pass": "dave123"},
    "eve": { "name" : "Eve", "pass": "eve123"}
}

def find_user(username, password):
    user = users.get(username)
    if user and user['pass'] == password:
        return user
    return None

def generate_login_cookie():
    return hashlib.sha256(app.secret_key.encode()).hexdigest()

@app.route('/')
def home():
    return render_template('users.html', users=users)

@app.route('/register', methods=['GET'])
def register_get():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register_post():
    username = request.form['username']
    password = request.form['password']
    if username in users:
        return "User already exists!"
    users[username] = {"name": username, "pass": password}
    return redirect(url_for('home'))

@app.route('/login', methods=['GET'])
def login_get():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']
    user = find_user(username, password)
    if user:
        resp = make_response(redirect(url_for('dashboard')))
        resp.set_cookie('logged_in', generate_login_cookie())
        return resp
    return "Invalid credentials!"

@app.route('/dashboard')
def dashboard():
    logged_in_cookie = request.cookies.get('logged_in')
    if logged_in_cookie == generate_login_cookie():
        return render_template('dashboard.html')
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True, port=3333)