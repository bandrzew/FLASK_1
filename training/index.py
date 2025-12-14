from flask import Flask, render_template

app = Flask(__name__)

def get_pages():
    return {
        "page1": "page1.html",
        "page2": "page2.html",
        "page3": "page3.html"
    }

@app.route('/')
def index():
    items = ["Item 1", "Item 2", "Item 3"]
    return render_template(get_pages()["page1"], items=items)

@app.route('/page2')
def page2():
    items = ["Item A", "Item B", "Item C"]
    return render_template(get_pages()["page2"], items=items)

@app.route('/page3')
def page3():
    items = ["Apple", "Banana", "Cherry"]
    return render_template(get_pages()["page3"], items=items)

if __name__ == '__main__':
    app.run(debug=True)