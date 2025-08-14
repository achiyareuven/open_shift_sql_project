import mysql.connector

class Dal:
    def __init__(self,
                 host="mysql-service",
                 user="appduser",
                 password="appdpass",
                 database="sampledb",
                 port=3306):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.conn = None

    def connect(self):
        try:
            self.conn =mysql.connector.connect(
                host=self.host,
                user = self.user,
                password=self.password,
                database = self.database,
                port = self.port
            )
        except mysql.connector.Error as err:
            print("error connection ")
            raise

    def close(self):
        if self.conn and self.conn.is_connected():
            self.conn.close()

    def execute_query(self,query:str,parms = None):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(query, parms or ())
        return cursor.fetchall()



