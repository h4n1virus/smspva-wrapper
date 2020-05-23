from ..ext import Base
from ..ext.containers import UserInfoContainer
from ..methods import API


class Client(API, Base):
    """High level wrapper for making requests to SMSPVA API

    Parameters:
        api_key (str):
            The *APIKEY* of your SMSPVA/SIMSMS account as str: E.g: "DSWAFvdedrE4"
        backend (str):
            Backend to be used: SMSPVA or SIMSMS
    """

    def __init__(
        self,
        api_key: str,
        backend: str = 'simsms',
    ):
        Base.__init__(self, api_key=api_key, backend=backend)
        self._name = self.me.name

    @property
    def me(self) -> UserInfoContainer:
        return self.get_userinfo()

    @property
    def balance(self) -> float:
        return float(self.me.balance)

    @property
    def karma(self) -> float:
        return float(self.me.karma)

    @property
    def name(self) -> str:
        return self._name
