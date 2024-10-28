from urllib.parse import urlencode
from .accounts import Accounts
from .contracts import Contracts
from .transactions import Transactions
from .blocks import Blocks
from .logs import Logs
from .proxys import Proxy
from .tokens import Tokens
from .gastracker import GasTracker
from .stats import Stats
from .chainspecific import ChainSpecific
from .usage import Usage
from .metadata import *
import requests

__all__ = ["EtherScanV2"]


class EtherScanV2:
    def __init__(self, apikey: str, chainid=supported_chains["Etherscan"]) -> None:
        self.__base_url: str = base_url
        self.api_key: str = apikey
        self.chain_id: str = chainid
        self.__valid_params = valid_params

        self.Account = Accounts(self)
        self.Contract = Contracts(self)
        self.Transaction = Transactions(self)
        self.Block = Blocks(self)
        self.Logs = Logs(self)
        self.Proxy = Proxy(self)
        self.Tokens = Tokens(self)
        self.GasTracker = GasTracker(self)
        self.Stats = Stats(self)
        self.ChainSpecific = ChainSpecific(self)
        self.Usage = Usage(self)

    def __connect_api(self, module: str, action: str, params: dict):
        api_params = {k: v for k, v in params.items() if k in self.__valid_params[action]}
        url = f"{self.__base_url}?apikey={self.api_key}&chainid={self.chain_id}&module={module}&action={action}&{urlencode(api_params)}"
        res = requests.get(url).json()
        if res['status'] == '0' or res['message'] == 'NOTOK':
            raise Exception(res['result'])
        return res['result']
