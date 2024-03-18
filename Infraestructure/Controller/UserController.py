from fastapi import FastAPI
from Domain.UseCase.UserService import UserService

aplicacion = FastAPI()

@aplicacion.get("/get-users")
def get_users():
    userService = UserService()
    return userService.get_user() 