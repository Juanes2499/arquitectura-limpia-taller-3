import mysql.connector

class Conexion:
    def __init__(self):
        self.host = "192.168.100.9"
        self.port = "3306"
        self.database = "Prueba"
        self.user = "root"
        self.password = "Qwer1234"
    
    def get_Conexion(self):
        conexion =  mysql.connector.connect(host=self.host,database=self.database,user=self.user,password=self.password)
        return conexion