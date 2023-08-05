from endpoints.db_config import DBConfig
import json

class User():
    def __init__(self):
        self.db_conn = DBConfig.db_connect()
    
    def create_new_user(self, username, pw):
        try:
            cursor = self.db_conn.cursor()
            cursor.execute('CALL CREATE_NEW_USER(\'' + username + '\', \'' + pw + '\');')
            
            cursor.execute('SELECT MAX(USER_ID) FROM CFB_USERS;')
            user_id = cursor.fetchall()[0][0]
            
            cursor.close()
            self.db_conn.close()
            
            response_data = {
                'message': 'New User Created Successfully!',
                'data': {'userID': user_id, 'userName': username}
            }
            response = json.dumps(response_data), 201
        except:
            response_data = {
                'message': 'Internal error occurred. New user not created...'
            }
            response = json.dumps(response_data), 500
        
        return response