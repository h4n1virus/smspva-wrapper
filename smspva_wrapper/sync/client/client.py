from typing import Union

from smspva_wrapper.types import Services, Countries
from smspva_wrapper.errors import Errors


class Client:
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
        backend: str = 'simsms'
    ):
        self.api_key = api_key
        self.backend = self._get_backend(backend)



    @property
    def me(self) -> Containers.UserInfo:
        return self.get_userinfo()

    @property
    def balance(self) -> float:
        return float(self.me.balance)

    @property
    def karma(self) -> float:
        return float(self.me.karma)

    def get_balance(self) -> Containers.Balance:
        return Containers.Balance(
            Methods.get_balance(
                api_base=self.api_base
            )
        )

    def get_userinfo(self) -> Containers.UserInfo:
        return Containers.UserInfo(
            Methods.get_userinfo(
                api_base=self.api_base
            )
        )

    def get_count_new(self, service: Union[Services, str], country: Union[Countries, str]) -> Containers.CountNew:
        return Containers.CountNew(
            Methods.get_count_new(
                api_base=self.api_base,
                service=str(service),
                country=str(country)
            )
        )

    def get_service_price(self, service: Union[Services, str], country: Union[Countries, str]) -> Containers.ServicePrice:
        return Containers.ServicePrice(
            Methods.get_service_price(
                api_base=self.api_base,
                service=str(service),
                country=str(country)
            )
        )

    def get_number(self, service: Union[Services, str], country: Union[Countries, str]) -> Containers.Number:
        return Containers.Number(
            Methods.get_number(
                api_base=self.api_base,
                service=str(service),
                country=str(country)
            )
        )

    def ban(self, service: Union[Services, str], _id: str) -> Containers.Ban:
        return Containers.Ban(
            Methods.ban(
                api_base=self.api_base,
                service=str(service),
                _id=_id
            )
        )

    def get_sms(self, service: Union[Services, str], country: Union[Countries, str], _id: str) -> Containers.SMS:
        return Containers.SMS(
            Methods.get_sms(
                api_base=self.api_base,
                service=str(service),
                country=str(country),
                _id=_id
            )
        )

    def denial(self, service: Union[Services, str], country: Union[Countries, str], _id: str) -> Containers.Denial:
        return Containers.Denial(
            Methods.denial(
                api_base=self.api_base,
                service=str(service),
                country=str(country),
                _id=_id
            )
        )

    def get_proveka(self, service: Union[Services, str], number: str) -> Containers.Proverka:
        return Containers.Proverka(
            Methods.get_proverka(
                api_base=self.api_base,
                service=str(service),
                number=number
            )
        )

    def balance_sim(self, service: Union[Services, str], _id: str) -> Containers.BalanceSIM:
        return Containers.BalanceSIM(
            Methods.balance_sim(
                api_base=self.api_base,
                service=str(service),
                _id=_id
            )
        )

    def redirect(self, service: Union[Services, str], number_redirect: str, _id: str) -> Containers.Redirect:
        return Containers.Redirect(
            Methods.redirect(
                api_base=self.api_base,
                service=str(service),
                _id=_id,
                number_redirect=number_redirect
            )
        )

    def get_2fa(self, secret: str) -> Containers.TwoFA:
        return Containers.TwoFA(
            Methods.get_2fa(
                api_base=self.api_base,
                secret=str(secret)
            )
        )

    def get_clearsms(self, service: Union[Services, str], _id: str) -> Containers.ClearSMS:
        return Containers.ClearSMS(
            Methods.get_clearsms(
                api_base=self.api_base,
                service=str(service),
                _id=_id
            )
        )
