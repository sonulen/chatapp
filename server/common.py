
class User:
    def __init__(self, nickname: str = None, auth: bool = False):
        self.__nickname = nickname
        self.__auth = auth

    @property
    def nickname(self) -> str:
        return self.__nickname

    @nickname.setter
    def nickname(self, nickname) -> None:
        if not nickname:
            return
        
        self.__nickname = nickname

    @property
    def auth(self) -> bool:
        return self.__auth

    @auth.setter
    def auth(self, status: bool) -> None:
        self.__auth = status

    
class Message:
    def __init__(self, nickname: str, msg: str):
        self.__nickname = nickname
        self.__msg = msg

    @property
    def content(self) -> str:
        return f"{self.__nickname}: {self.__msg}"
