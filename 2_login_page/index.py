from flask import Flask, redirect, request, url_for, render_template

app = Flask(__name__)

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

@app.route('/')
def home():
    return render_template('users.html', users=users)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            return "User already exists!"
        users[username] = {"name": username, "pass": password}
        return redirect(url_for('home'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = find_user(username, password)
        if user:
            return redirect(url_for('dashboard'))
        return "Invalid credentials!"
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == "__main__":
    app.run(debug=True, port=3333)