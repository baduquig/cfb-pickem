from flask import Flask, jsonify, request
import db as z

app = Flask(__name__)

cursor = z.instantiate_connection()

@app.route('/get-user')
def cfb_get_user():
    username = request.args.get('username')
    pw = request.args.get('pw')
    user_id = z.get_user(cursor, username, pw)
    response = jsonify({"userid": user_id})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/create-user')
def cfb_create_user():
    username = request.args.get('username')
    pw = request.args.get('pw')
    z.create_user(cursor, username, pw)

@app.route('/submit-pick')
def cfb_submit_pick():
    user_id = request.args.get('userid')
    game_id = request.args.get('pw')
    selected_team = request.args.get('selected')
    z.submit_pick(cursor, user_id, game_id, selected_team)