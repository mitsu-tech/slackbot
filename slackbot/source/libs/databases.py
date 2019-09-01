import os
from os.path import join, dirname
from dotenv import load_dotenv
import slackbot_settings
import MySQLdb


class Database:
    def __init__(self):
        self.connection = MySQLdb.connect(
            host = slackbot_settings.DB_HOST,
            user = str(slackbot_settings.DB_USER).lstrip("('").rstrip(",)'"),
            passwd = str(slackbot_settings.DB_PASSWD).lstrip("('").rstrip(",)'"),
            db = slackbot_settings.DB
            )
        self.cursor = self.connection.cursor()

    def get(self, object, message):
        self.cursor.execute("show " + object + ";")
        rows = self.cursor.fetchall()
        for i in rows:
            message.send(str(i).lstrip("('").rstrip("',)"))
        self.close()

    def create(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS person(
        id INT(11) AUTO_INCREMENT NOT NULL,
        name VARCHAR(30) NOT NULL,
        age INT(3) NOT NULL,
        PRIMARY KEY (id));"""
        )
        self.close()

    def delete(self):
        self.cursor.execute("""DROP TABLE person""")
        self.close()

    def close(self):
        self.connection.commit()
        self.connection.close()