from .raw_balance_sim import RawBalanceSim
from .raw_ban import RawBan
from .raw_denial import RawDenial
from .raw_get_2fa import RawGet2FA
from .raw_get_balance import RawGetBalance
from .raw_get_clearsms import RawGetClearSMS
from .raw_get_count_new import RawGetCountNew
from .raw_get_number import RawGetNumber
from .raw_get_proverka import RawGetProverka
from .raw_get_service_price import RawGetServicePrice
from .raw_get_sms import RawGetSMS
from .raw_get_userinfo import RawGetUserinfo
from .raw_redirect import RawRedirect


class RAWAPI(
    RawBalanceSim,
    RawBan,
    RawDenial,
    RawGet2FA,
    RawGetBalance,
    RawGetClearSMS,
    RawGetCountNew,
    RawGetNumber,
    RawGetProverka,
    RawGetServicePrice,
    RawGetSMS,
    RawGetUserinfo,
    RawRedirect
):
    pass
