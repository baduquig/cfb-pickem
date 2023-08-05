from endpoints.db_config import DBConfig
import json

class Pick():
    def __init__(self):
        self.db_conn = DBConfig.db_connect()

    def submit_pick(self, user_id, game_id, selected_school):
        try:
            cursor = self.db_conn.cursor()
            cursor.execute('CALL SUBMIT_PICK(\'' + user_id + '\', \'' + game_id + '\', \'' + selected_school + '\')')
            cursor.close()
            self.db_conn.close()

            response_data = {
                'message': 'Pick Submitted Successfully!',
                'data': {
                    'userID': user_id, 
                    'gameID': game_id, 
                    'selectedSchool': selected_school
                }
            }
        except:
            response_data = {
                'message': 'Internal error occurred. New picks not updated...'
            }
            response = json.dumps(response_data), 500
        
        return response