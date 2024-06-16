import mysql.connector
from config import db_config

def instantiate_connection():
    """Function to instantiate connection to MySQL `PICKEM_GB` database
       Accepts: n/a
       Returns: `conn`: MySQLConnection Object"""
    config = db_config
    conn = mysql.connector.connect(**config)
    return conn

def get_user(cursor: object, username: str, pw: str):
    """Function to retreive the User ID for the given login attempt
       Accepts: `cursor`: MySQL Database Connection Cursor, `username`: String, `pw`: String
       Returns: `user_id`: Number"""
    exec_proc_str = f"EXEC CFB_GET_USER @USERNAME_INPUT '{username}', @PW_INPUT '{pw}';"
    cursor.execute(exec_proc_str)
    record = cursor.fetchone()
    cursor.close()

    user_id = record[0]
    if (all(record[0]) or record[0] != ''):
        user_id = 0
    return user_id

def create_user(cursor: object, username: str, pw: str):
    """Function to create picks and user record for new user
       Accepts: `cursor`: MySQL Database Connection Cursor, `username`: String, `pw`: String
       Returns: n/a"""
    exec_proc_str = f"EXEC CFB_CREATE_USER @USERNAME_INPUT '{username}', @PW '{pw}';"
    cursor.execute(exec_proc_str)
    cursor.close()

def submit_pick(cursor: object, user_id: int, game_id: int, selected_team: str):
    """Function to submit/update pick for a given user and game
       Accepts: `cursor`: MySQL Database Connection Cursor, `user_id`: Number, `game_id`: Number, `selected_team`: String
       Returns: n/a"""
    exec_proc_str = f"EXEC CFB_SUBMIT_PICK @USR '{user_id}', @GM '{game_id}', @SELECTED_TEAM '{selected_team}';"
    cursor.execute(exec_proc_str)
    cursor.close()