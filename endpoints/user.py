from db_config import DBConfig
import json
import mysql.connector

class User():
    def __init__(self):
        self.db_config = DBConfig.db_config