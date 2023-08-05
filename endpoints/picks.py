from db_config import DBConfig
import json
import mysql.connector

class Picks():
    def __init__(self):
        self.db_config = DBConfig.db_config

    def db_connect(self, config):
        conn = mysql.connector.connect(**config)
        return conn

    def create_select_statement(self, user_id, game_id):
        db_name = self.db_config["database"]

        if user_id is None and game_id is None:
            select_stmt = f'SELECT * FROM {db_name}.CFB_ALL_DATA_VW;'
        elif user_id is None and game_id is not None:
            select_stmt = f'SELECT * FROM {db_name}.CFB_ALL_DATA_VW WHERE GAME_ID = {game_id}'
        elif user_id is not None and game_id is None:
            select_stmt = f'SELECT * FROM {db_name}.CFB_ALL_DATA_VW WHERE USER_ID = {user_id};'
        else:
            select_stmt = f'SELECT * FROM {db_name}.CFB_ALL_DATA_VW WHERE GAME_ID = {game_id} AND USER_ID = {user_id};'
        return select_stmt

    def create_result_string(self, results_tuples):
        results_dicts = []
        for record in results_tuples:
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

    def get_all_data(self, game_id, user_id):
        #user_id = request.args.get('userID')
        #game_id = request.args.get('gameID')

        conn = self.db_connect(self.db_config)
        cursor = conn.cursor()
        select_stmt = self.create_select_statement(game_id, user_id)
        cursor.execute(select_stmt)
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        
        response = self.create_result_string(results)
        #response.headers.add('Access-Control-Allow-Origin', '*')
        return response