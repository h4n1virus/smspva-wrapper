import logging
import requests
from smspva_wrapper.errors import Errors
from smspva_wrapper.sync.ext import Base

log = logging.getLogger(__name__)


class Caller(Base):
    def __init__(self):
        super().__init__()

    def call(self, query: str) -> dict:
        """Low-level function for calling API

        Args:
            query (str): API link to request

        Returns:
            json_dict (dict): containing dictionary of parsed json from API

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
        r = requests.get(query)
        log.debug(r.status_code, r.content)

        if r.status_code == 200:
            try:
                json_dict: dict = r.json()
                return json_dict
            except ValueError:
                error = r.content.decode()
                if 'API KEY не получен!' == error:
                    raise Errors.InvalidAPIKeyError(error)
                elif 'API KEY не найден!' == error:
                    raise Errors.InvalidAPIKeyError(error)
                elif 'API KEY not received!' == error:
                    raise Errors.InvalidAPIKeyError(error)
                elif 'Недостаточно средств!' == error:
                    raise Errors.InsufficientFundsError(error)
                elif 'Превышено количество попыток!' == error:
                    raise Errors.TooShortIntervalError(error)
                elif 'Произошла неизвестная ошибка.' == error:
                    raise Errors.RepeatRequestLaterError(error)
                elif 'Неверный запрос.' == error:
                    raise Errors.RequestSyntaxError(error)
                elif 'Произошла внутренняя ошибка сервера.' == error:
                    raise Errors.RepeatRequestLaterError(error)
                else:
                    raise Errors.UnknownAPIError(error)
        else:
            raise Errors.NetworkingError("status code: ", r.status_code)
