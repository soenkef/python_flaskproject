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
    #items = [
    #    Item("Apfel", 5),
    #    Item("Computer", 1),
    #    Item("Birne", 4)
    #]
    items = [
        {"name": "Apfel", "amount": 5},
        {"name": "Computer", "amount": 1},
        {"name": "Birne", "amount": 4}
    ]#

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


