from endpoints.db_config import DBConfig
import json

class Validate():
    def __init__(self):
        self.db_conn = DBConfig.db_connect()
    
    def get_user(self, userid, pw):
        cursor = self.db_conn.cursor()
        cursor.execute('CALL CFB_GET_USER(\'' + userid + '\', \'' + pw + '\');')
        user_record = cursor.fetchone()
        return user_record

    def validate(self, userid, pw):
        if (userid is None or pw is None):
            if userid is None:
                response_data = {
                    'message': 'User ID credential not provided.'
                }
            if pw is None:
                response_data = {
                    'message': 'Password credential not provided.'
                }
            response = json.dumps(response_data), 400
            return response
        
        user_record = self.get_user(userid, pw)
        
        if len(user_record) > 0:
            response_data = {
                'message': 'User login credentials validated.',
                'data': {'userID': user_record[0]}
            }
            response = json.dumps(response_data), 200
        else:
            response_data = {
                'message': 'Verify credentials.'
            }
            response = json.dumps(response_data), 401
        return response
        