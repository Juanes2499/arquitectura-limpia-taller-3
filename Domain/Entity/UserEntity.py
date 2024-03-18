class UserEntity: 
    def __init__(self,identificacion,nombre,apellido):
        self.identificacion = identificacion
        self.nombre = nombre
        self.apellido = apellido
    
    def get_user(self):
        return f"Identificacion: {self.identificacion} Nombre: {self.nombre} Apellido: {self.apellido}"