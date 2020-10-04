from flask import Flask, render_template, request
print(__name__)
app = Flask(__name__)

class Item():
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount


# decorator
@app.route('/')
def hello_world():

    items = [
        {"name": "Apfel", "amount": 5},
        {"name": "Computer", "amount": 1},
        {"name": "Birne", "amount": 4}
    ]

    # Berechnungen - idealerweise nicht im template
    for item in items:
        item["amount"] = item["amount"] * 2

    person = ("Max", "Mustermann")

    return render_template("start.html", person=person, items=items)

@app.route('/test')
def test():
    name = request.args.get("name")
    age2 = request.args.get("age")
    return render_template("test.html", name=name, age=age2)

@app.route('/currency')
def calculate():
    d = [
        {"euro": "1€", "result": "1.56"},
        {"euro": "10€", "result": "19.56"},
        {"euro": "100€", "result": "195.58"},
        {"euro": "1000€", "result": "1955.83"}
    ]
    val = request.args.get("value")
    print(val)
    if val != None:
        val = float(val.replace(",", "."))
        result = val * 1.95583
        result = round(result, 2)
        print(result)
    else:
        result = None
        val = None
        print("Bitte einen gültigen Wert eingeben!")

    return render_template("currency.html", value=val, result=result, d=d)
