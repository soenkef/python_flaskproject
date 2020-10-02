from flask import Flask, render_template
print(__name__)
app = Flask(__name__)

# decorator
@app.route('/')
def hello_world():
    items = ["Apfel", "Birne", "Banana"]

    return render_template("start.html", name="Max Mustermann", items=items)

@app.route('/test')
def test():
    return render_template("test.html", name="Max Mustermann")


