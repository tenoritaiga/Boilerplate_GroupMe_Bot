from flask import Flask, session

app = Flask(__name__)
session['test'] = 'abcde'

@app.route('/',methods=['GET'])
def foo():
    print(session['test'])
    session['test'] = 'vwxyz'
    session.modified = True
    return 'done'

foo()