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
    exec_select_str = f"SELECT USER_ID FROM USERS WHERE USERNAME = '{username}' AND PW = '{pw}';"
    try:
        logfile = open('./error.log', 'a')
        conn = instantiate_connection()
        cursor = conn.cursor()
        cursor.execute(exec_select_str)
        record = cursor.fetchone()
        user_id = record[0]

        logfile.write(f'{user_id}')
        if (user_id is None or user_id == ''):
            user_id = 0
    except Exception as e:
        user_id = 0
        logfile.write(f'Error occurred getting user:\n{e}\n\n\n')
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
        logfile = open('./error.log', 'a')
        logfile.write(f'Error occurred creating user:\n{e}\n\n\n')
        logfile.close()
    return status

def get_all_picks():
    """Function to retrieve all picks
       Accepts: n/a
       Returns: n/a"""
    exec_select_str = 'SELECT * FROM CFB_GET_ALL_DATA_VW;'
    try:
        conn = instantiate_connection()
        cursor = conn.cursor()
        cursor.execute(exec_select_str)
        data = cursor.fetchall()
        formatted_response = [{
                            'userID': record[0],
                            'username': record[1],
                            'gameID': record[2],
                            'teamPicked': record[3],
                            'awayTeam': record[4],
                            'awayTeamName': record[5],
                            'awayTeamMascot': record[6],
                            'awayLogoURL': record[7],
                            'awayConference': record[8],
                            'awayConferenceWins': record[9],
                            'awayConferenceLosses': record[10],
                            'awayConferenceTies': record[11],
                            'awayOverallWins': record[12],
                            'awayOverallLosses': record[13],
                            'awayOverallTies': record[14],
                            'homeTeam': record[15],
                            'homeTeamName': record[16],
                            'homeTeamMascot': record[17],
                            'homeLogoURL': record[18],
                            'homeConference': record[19],
                            'homeConferenceWins': record[20],
                            'homeConferenceLosses': record[21],
                            'homeConferenceTies': record[22],
                            'homeOverallWins': record[23],
                            'homeOverallLosses': record[24],
                            'homeOverallTies': record[25],
                            'stadium': record[26],
                            'stadiumCapacity': record[27],
                            'city': record[28],
                            'state': record[29],
                            'tvCoverage': record[30],
                            'bettingLine': record[31],
                            'bettingLineOverUnder': record[32],
                            'attendance': record[33],
                            'awayWinPercentage': record[34],
                            'homeWinPercentage': record[35],
                            'awayQuarter1': record[36],
                            'awayQuarter2': record[37],
                            'awayQuarter3': record[38],
                            'awayQuarter4': record[39],
                            'awayOvertime': record[40],
                            'awayTotal': record[41],
                            'homeQuarter1': record[42],
                            'homeQuarter2': record[43],
                            'homeQuarter3': record[44],
                            'homeQuarter4': record[45],
                            'homeOvertime': record[46],
                            'homeTotal': record[47],
                            'gameTime': record[48],
                            'gameDate': record[49],
                            'gameMonth': record[50],
                            'gameDay': record[51],
                            'gameYear': record[52]
                           } for record in data]
    except Exception as e:
        formatted_response = [{'status': 400}]
        logfile = open('./error.log', 'a')
        logfile.write(f'Error retrieving all picks:\n{e}\n\n\n')
        logfile.close()
    return formatted_response

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
        logfile = open('./error.log', 'a')
        logfile.write(f'Error occurred submitting pick:\n{e}\n\n\n')
        logfile.close()
    return status