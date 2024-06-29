from flask import Flask, jsonify, request
import db as z

app = Flask(__name__)

@app.route('/get-user')
def cfb_get_user():
    username = request.args.get('username')
    pw = request.args.get('pw')
    user_id = z.get_user(username, pw)

    response = jsonify({"userid": user_id})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/create-user')
def cfb_create_user():
    username = request.args.get('username')
    pw = request.args.get('pw')
    status = z.create_user(username, pw)

    response = jsonify({"status": status})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/submit-pick')
def cfb_submit_pick():
    user_id = request.args.get('userid')
    game_id = request.args.get('pw')
    selected_team = request.args.get('selected')
    status = z.submit_pick(user_id, game_id, selected_team)

    response = jsonify({"status": status})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    app.run(debug=True)