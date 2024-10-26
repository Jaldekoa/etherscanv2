from etherscanv2 import __base_url, __connect_api
from urllib.parse import urlencode


def getstatus(apikey: str, chainid: int, txhash: str):
    params, module, action = locals(), "transaction", "getstatus"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)


def gettxreceiptstatus(apikey: str, chainid: int, txhash: str):
    params, module, action = locals(), "transaction", "gettxreceiptstatus"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)
