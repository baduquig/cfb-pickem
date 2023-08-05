from endpoints.db_config import DBConfig
import json

class User():
    def __init__(self):
        self.db_conn = DBConfig.db_connect()
    
    def create_new_user(self, username, pw):
        try:
            print('Here 1')
            cursor = self.db_conn.cursor()
            print('Here 2')
            cursor.execute('CALL CREATE_NEW_USER(\'' + username + '\', \'' + pw + '\');')
            print('Here 3')
            # cursor.commit()
            print('Here 4')
            cursor.execute('SELECT MAX(USER_ID) FROM CFB_USERS;')
            print('Here 5')
            user_id = cursor.fetchall()[0][0]
            print('Here 6')
            cursor.close()
            print('Here 7')
            self.db_conn.close()
            print('Here 8')

            response_data = {
                'message': 'New User Created Successfully!',
                'data': {'userID': user_id, 'userName': username}
            }
            print('Here 9')
            response = json.dumps(response_data), 201
        except:
            response_data = {
                'message': 'Internal error occurred. New user not created...'
            }
            response = json.dumps(response_data), 500
        
        return response