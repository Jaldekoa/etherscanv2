from etherscanv2 import __base_url, __connect_api
from urllib.parse import urlencode


def tokensupply(apikey: str, chainid: int, contractaddress: str):
    params, module, action = locals(), "stats", "tokensupply"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)


def tokenbalance(apikey: str, chainid: int, contractaddress: str, address: str):
    params, module, action = locals(), "account", "tokenbalance"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)


def tokensupplyhistory(apikey: str, chainid: int, contractaddress: str, blockno: int):
    params, module, action = locals(), "stats", "tokensupplyhistory"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)


def tokenbalancehistory(apikey: str, chainid: int, contractaddress: str, blockno: int):
    params, module, action = locals(), "account", "tokensupplyhistory"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)


def tokenholderlist(apikey: str, chainid: int, contractaddress: str, page: int, offset: int):
    params, module, action = locals(), "token", "tokenholderlist"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)


def tokeninfo(apikey: str, chainid: int, contractaddress: str):
    params, module, action = locals(), "token", "tokeninfo"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)


def addresstokenbalance(apikey: str, chainid: int, address: str, page: int, offset: int):
    params, module, action = locals(), "account", "addresstokenbalance"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)


def addresstokennftbalance(apikey: str, chainid: int, address: str, page: int, offset: int):
    params, module, action = locals(), "account", "addresstokennftbalance"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)


def addresstokennftinventory(apikey: str, chainid: int, contractaddress: str, page: int, offset: int):
    params, module, action = locals(), "account", "addresstokennftinventory"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)
