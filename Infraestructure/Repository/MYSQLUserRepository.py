from Infraestructure.Repository.Conexion import Conexion
from Infraestructure.Repository.DTOUser import DTOUser
from Domain.UseCase.UserRepository import UserRepository
from Infraestructure.Repository.MapperUser import MapperUser

class MYSQLUserRepository(UserRepository): 
    def __init__(self):
        self.conexion = Conexion()
    
    def get_all_user(self):
        database = self.conexion.get_Conexion()
        cursorSelect = database.cursor()
        cursorSelect.execute("SELECT * FROM Persona")
        users = {DTOUser(persona[0],persona[1],persona[2]) for persona in cursorSelect }
        cursorSelect.close()
        mapper = MapperUser(users)
        return mapper.mapperUser()