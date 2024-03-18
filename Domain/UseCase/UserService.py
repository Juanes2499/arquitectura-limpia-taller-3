from Domain.UseCase.Build import Build
from Domain.UseCase.UserRepository import UserRepository
from Domain.Entity.UserEntity  import UserEntity

class UserService: 
    def __init__(self):
        pass

    def get_user(self):
        builder = Build()
        service = builder.BuilRespotory()
        usersDomain = service.get_all_user()
        nameUser = {user.get_user() for user in usersDomain}
        return nameUser