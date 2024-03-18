from  Domain.Entity.UserEntity import UserEntity
from Infraestructure.Repository.DTOUser import DTOUser
class MapperUser:
    def __init__(self,users):
        self.users = users
       
    def mapperUser(self):
        usersDomain = {UserEntity(user.identificacion,user.nombre,user.apellido) for user in self.users}
        return usersDomain
        
           
