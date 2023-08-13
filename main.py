from endpoints.validate import Validate
from endpoints.register import Register
from endpoints.all_data import AllData
from endpoints.pick import SubmitPicks
from flask import Flask, request #, jsonify

app = Flask(__name__)

@app.route('/validate')
def validate():
    username = request.args.get('username')
    pw = request.args.get('pw')

    response = Validate.validate(username, pw)
    return response

@app.route('/register')
def register():
    username = request.args.get('username')
    pw = request.args.get('pw')
    confirm_pw = request.args.get('confirm_pw')

    response = Register.register(username, pw, confirm_pw)
    return response

@app.route('/alldata')
def all_data():
    response = AllData.get_all_data()
    return response

@app.route('/submitpick')
def submit_pick():
    data = request.json
    response = SubmitPicks.submit_picks(data)
    return response
