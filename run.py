from flask import Flask
print(__name__)
app = Flask(__name__)

# decorator
@app.route('/')
def hello_world():
    items = ["Apfel", "Birne", "Banana"]

    output = ""
    for item in items:
        output += "<h3>" + item + "</h3>"

    return output
#    return 'Hello, World!'

@app.route('/test')
def test():
    paragraph = "<p>Halloooo Welt</p>"
    return "Hello <strong>Test</strong>!" + paragraph

