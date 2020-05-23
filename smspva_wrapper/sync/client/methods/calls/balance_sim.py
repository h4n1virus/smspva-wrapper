from ..raw_api import RawBalanceSim
from smspva_wrapper.types.containers import BalanceSIMContainer


class BalanceSim:
    def balance_sim(self):
        r = RawBalanceSim.raw_balance_sim(
            api_base=None
        )