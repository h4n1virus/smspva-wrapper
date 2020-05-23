from .balance_object import BalanceContainer
from .balance_sim_object import BalanceSIMContainer
from .ban_object import BanContainer
from .denial_object import DenialContainer
from .count_new_object import CountNewContainer
from .number_object import NumberContainer
from .proverka_object import ProverkaContainer
from .redirect_object import RedirectContainer
from .service_price_object import ServicePriceContainer
from .sms_object import SMSContainer
from .two_fa_object import TwoFAContainer
from .userinfo_object import UserInfoContainer
from .clearsms_object import ClearSMSContainer


class Containers(
    BalanceContainer,
    BalanceSIMContainer,
    BanContainer,
    DenialContainer,
    CountNewContainer,
    NumberContainer,
    ProverkaContainer,
    RedirectContainer,
    ServicePriceContainer,
    SMSContainer,
    TwoFAContainer,
    UserInfoContainer,
    ClearSMSContainer
):
    pass
