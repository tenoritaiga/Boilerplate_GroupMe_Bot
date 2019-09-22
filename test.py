from flask import Flask

app = Flask(__name__)
test = 'foo'

@app.route('/', methods=['GET'])
def bar():
    global test
    print(test)
    test = 'baz'
    print(test)
    return 'ok'