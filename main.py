import json
import mysql.connector

config = {
    'user': 'sql9634488',
    'password': '2usSRQH2hu',
    'host': 'sql9.freemysqlhosting.net',
    'database': 'sql9634488',
    'raise_on_warnings': True
}

def db_connect():
    conn = mysql.connector.connect(**config)
    return conn

def create_select_statement(user_id, game_id):
    if user_id is None and game_id is None:
        select_stmt = f'SELECT * FROM {config["database"]}.CFB_ALL_DATA_VW;'
    elif user_id is None and game_id is not None:
        select_stmt = f'SELECT * FROM {config["database"]}.CFB_ALL_DATA_VW WHERE GAME_ID = {game_id}'
    elif user_id is not None and game_id is None:
        select_stmt = f'SELECT * FROM {config["database"]}.CFB_ALL_DATA_VW WHERE USER_ID = {user_id};'
    else:
        select_stmt = f'SELECT * FROM {config["database"]}.CFB_ALL_DATA_VW WHERE GAME_ID = {game_id} AND USER_ID = {user_id};'
    return select_stmt

def create_result_string(results_tuples):
    results_dicts = []
    for record in results_dicts:
        record_obj = {
            'userID': record[0],
            'userName': record[1],
            'gameID': record[2],
            'selectedSchool': record[3],
            'gameWeek': record[4],
            'gameDate': record[5],
            'gameTime': record[6],
            'score': record[7],
            'awaySchoolID': record[8],
            'awaySchoolName': record[9],
            'awaySchoolMascot': record[10],
            'awaySchoolWins': record[11],
            'awaySchoolLosses': record[12],
            'awaySchoolTies': record[13],
            'awaySchoolDivisionName': record[14],
            'awaySchoolConferenceName': record[15],            
            'homeSchoolID': record[16],
            'homeSchoolName': record[17],
            'homeSchoolMascot': record[18],
            'homeSchoolWins': record[19],
            'homeSchoolLosses': record[20],
            'homeSchoolTies': record[21],
            'homeSchoolDivisionName': record[22],
            'homeSchoolConferenceName': record[23],
            'locationName': record[24],
            'locationCity': record[25],
            'locationState': record[26]
        }
        results_dicts.append(record_obj)
    
    json_string = json.dumps(results_dicts)
    return json_string

def get_all_data(game_id, user_id):
    #user_id = request.args.get('userID')
    #game_id = request.args.get('gameID')

    conn = db_connect()
    cursor = conn.cursor()
    select_stmt = create_select_statement(game_id, user_id)
    cursor.execute(select_stmt)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    
    response = create_result_string(results)
    #response.headers.add('Access-Control-Allow-Origin', '*')
    return response

print(get_all_data(401520157, None))