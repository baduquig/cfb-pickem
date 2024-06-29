import mysql.connector
from config import db_config

def instantiate_connection():
    """Function to instantiate connection to MySQL `PICKEM_GB` database
       Accepts: n/a
       Returns: `conn`: MySQLConnection Object"""
    config = db_config
    conn = mysql.connector.connect(**config)
    return conn

def get_user(username: str, pw: str):
    """Function to retreive the User ID for the given login attempt
       Accepts: `username`: String, `pw`: String
       Returns: `user_id`: Number"""
    exec_proc_str = f"CALL CFB_GET_USER('{username}', '{pw}');"
    try:
        conn = instantiate_connection
        cursor = conn.cursor()
        cursor.execute(exec_proc_str)
        record = cursor.fetchone()
        cursor.close()
        conn.close()

        user_id = record[0]
        if (user_id is None or record[0] == ''):
            user_id = 0
    except Exception as e:
        user_id = 0
        logfile = open('./error.log', 'w')
        logfile.write(f'Error occurred getting user:\n{e}')
        logfile.close()
    return user_id

def create_user(username: str, pw: str):
    """Function to create picks and user record for new user
       Accepts: `username`: String, `pw`: String
       Returns: n/a"""
    exec_proc_str = f"CALL CFB_CREATE_USER('{username}', '{pw}');"
    try:
        conn = instantiate_connection()
        cursor = conn.cursor()
        cursor.execute(exec_proc_str)
        conn.commit()
        cursor.close()
        conn.close()
        status = 200
    except Exception as e:
        status = 400
        logfile = open('./error.log', 'w')
        logfile.write(f'Error occurred creating user:\n{e}')
        logfile.close()
    return status

def submit_pick(user_id: int, game_id: int, selected_team: str):
    """Function to submit/update pick for a given user and game
       Accepts: `user_id`: Number, `game_id`: Number, `selected_team`: String
       Returns: n/a"""
    exec_proc_str = f"CALL CFB_SUBMIT_PICK('{user_id}', '{game_id}', '{selected_team}');"
    try:
        conn = instantiate_connection()
        cursor = conn.cursor()
        cursor.execute(exec_proc_str)
        conn.commit()
        cursor.close()
        conn.close()
        status = 200
    except Exception as e:
        status = 400
        logfile = open('./error.log', 'w')
        logfile.write(f'Error occurred submitting pick:\n{e}')
        logfile.close()
    return status