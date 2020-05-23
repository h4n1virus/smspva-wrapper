import logging
import requests
from smspva_wrapper.errors import Errors
from smspva_wrapper.ext import Base

log = logging.getLogger(__name__)


class Caller(Base):
    def call(self, query: str) -> dict:
        """Low level function for calling API

        Args:
            query (str): query

        Returns:
            json_dict (dict):
                containing dictionary of parsed JSON response from API

        Raises:
            InvalidAPIKeyError
            InsufficientFundsError
            TooShortIntervalError
            RepeatRequestLaterError
            RequestSyntaxError
            APIGeneralError
            NetworkingError
            UnknownAPIError
        """

        r = requests.get(f"{self.api_base}&{query}")
        log.debug(r.status_code, r.content)

        if r.status_code == 200:
            try:
                json_dict: dict = r.json()
                return json_dict
            except ValueError:
                err = r.content.decode()
                if 'API KEY не получен!' == err:
                    raise Errors.InvalidAPIKeyError(err)
                elif 'API KEY не найден!' == err:
                    raise Errors.InvalidAPIKeyError(err)
                elif 'API KEY not received!' == err:
                    raise Errors.InvalidAPIKeyError(err)
                elif 'Недостаточно средств!' == err:
                    raise Errors.InsufficientFundsError(err)
                elif 'Превышено количество попыток!' == err:
                    raise Errors.TooShortIntervalError(err)
                elif 'Произошла неизвестная ошибка.' == err:
                    raise Errors.RepeatRequestLaterError(err)
                elif 'Неверный запрос.' == err:
                    raise Errors.RequestSyntaxError(err)
                elif 'Произошла внутренняя ошибка сервера.' == err:
                    raise Errors.RepeatRequestLaterError(err)
                else:
                    raise Errors.UnknownAPIError(err)
        else:
            raise Errors.NetworkingError("status code: ", r.status_code)
