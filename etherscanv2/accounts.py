from urllib.parse import urlencode
import requests

__base_url = "https://api.etherscan.io/v2/api"


def __connect_api(url: str):
    return requests.get(url).json()['result']


def balance(apikey: str, chainid: int, address: str, tag: str):
    params, module, action = locals(), "account", "balance"
    url = f"{__base_url}?apikey={apikey}&chainid={chainid}&module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)


def balancemulti(apikey: str, chainid: int, address: str, tag: str):
    params, module, action = locals(), "account", "balancemulti"
    url = f"{__base_url}?apikey={apikey}&chainid={chainid}&module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)


def txlist(apikey: str, chainid: int, address: str, startblock: int, endblock: int, page: int, offset: int, sort: str):
    params, module, action = locals(), "account", "txlist"
    url = f"{__base_url}?apikey={apikey}&chainid={chainid}&module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)


def txlistinternal_address(apikey: str, chainid: int, address: str, startblock: int, endblock: int, page: int, offset: int, sort: str):
    params, module, action = locals(), "account", "txlistinternal"
    url = f"{__base_url}?apikey={apikey}&chainid={chainid}&module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)


def txlistinternal_hash(apikey: str, chainid: int, txhash: str):
    params, module, action = locals(), "account", "txlistinternal"
    url = f"{__base_url}?apikey={apikey}&chainid={chainid}&module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)


def txlistinternal_block(apikey: str, chainid: int, startblock: int, endblock: int, page: int, offset: int, sort: str):
    params, module, action = locals(), "account", "txlistinternal"
    url = f"{__base_url}?apikey={apikey}&chainid={chainid}&module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)


def tokentx(apikey: str, chainid: int, address: str, contractaddress: str, page: int, offset: int, startblock: int, endblock: int, sort: str):
    params, module, action = locals(), "account", "tokentx"
    url = f"{__base_url}?apikey={apikey}&chainid={chainid}&module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)


def tokennfttx(apikey: str, chainid: int, address: str, contractaddress: str, page: int, offset: int, startblock: int, endblock: int, sort: str):
    params, module, action = locals(), "account", "tokennfttx"
    url = f"{__base_url}?apikey={apikey}&chainid={chainid}&module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)


def token1155tx(apikey: str, chainid: int, address: str, contractaddress: str, page: int, offset: int, startblock: int, endblock: int, sort: str):
    params, module, action = locals(), "account", "token1155tx"
    url = f"{__base_url}?apikey={apikey}&chainid={chainid}&module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)


def getminedblocks(apikey: str, chainid: int, address: str, blocktype: str, page: int, offset: int):
    params, module, action = locals(), "account", "getminedblocks"
    url = f"{__base_url}?apikey={apikey}&chainid={chainid}&module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)


def txsbeaconwithdrawal(apikey: str, chainid: int, address: str, contractaddress: str, page: int, offset: int, startblock: int, endblock: int, sort: str):
    params, module, action = locals(), "account", "txsBeaconWithdrawal"
    url = f"{__base_url}?apikey={apikey}&chainid={chainid}&module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)


def balancehistory(apikey: str, chainid: int, address: str, blockno: int):
    params, module, action = locals(), "account", "balancehistory"
    url = f"{__base_url}?apikey={apikey}&chainid={chainid}&module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)
