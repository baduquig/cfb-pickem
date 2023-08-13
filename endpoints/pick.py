from endpoints.db_config import DBConfig
import json

class Pick():
    def __init__(self):
        self.db_conn = DBConfig.db_connect()
    
    def submit_picks(self, picks):
        try:
            cursor = self.db_conn.cursor()

            for pick in picks:
                user_id = pick['userID']
                game_id = pick['gameID']
                selected_school = pick['selectedSchool']
                query_str = f'CALL CFB_SUBMIT_PICK(\'{user_id}\'. \'{game_id}\'. \'{selected_school}\');'
                cursor.execute(query_str)

            cursor.close()
            self.db_conn.close()

            response_data = {
                'message': 'Pick Submitted Successfully!',
                'data': {str(picks)}
            }
            response = json.dumps(response_data), 200
        except:
            response_data = {
                'message': 'Internal error occurred. New picks not updated...'
            }
            response = json.dumps(response_data), 500
        
        return response
