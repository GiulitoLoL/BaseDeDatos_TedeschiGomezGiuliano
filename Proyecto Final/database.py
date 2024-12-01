import mysql.connector

class Database:
    def __init__(self):
        
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Defere@45",
            database="Giuliano")
        self.cursor = self.conn.cursor(dictionary=True)
        
    def close(self):
        self.cursor.close()
        self.conn.close()