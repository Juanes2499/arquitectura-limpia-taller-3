import abc

class UserRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_all_user(self): 
        pass