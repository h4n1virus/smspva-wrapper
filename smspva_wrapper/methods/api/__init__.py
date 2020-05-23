from .balance_sim import BalanceSim
from .ban import Ban
from .denial import Denial
from .get_2fa import Get2FA
from .get_balance import GetBalance
from .get_clear_sms import GetClearSMS
from .get_count_new import GetCountNew
from .get_number import GetNumber
from .get_proverka import GetProverka
from .get_service_price import GetServicePrice
from .get_sms import GetSMS
from .get_userinfo import GetUserInfo
from .redirect import Redirect


class API(
    BalanceSim,
    Ban,
    Denial,
    Get2FA,
    GetBalance,
    GetClearSMS,
    GetCountNew,
    GetNumber,
    GetProverka,
    GetServicePrice,
    GetSMS,
    GetUserInfo,
    Redirect
):
    pass
