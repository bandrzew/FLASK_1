from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about-me')
def about_me():
    return render_template('about_me.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/submit-contact', methods=['POST'])
def submit_contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    print(f"{name}\n{email}\n{message}")
    return f"Thank you, {name}! We've received your message."

if __name__ == '__main__':
    app.run(debug=True)
