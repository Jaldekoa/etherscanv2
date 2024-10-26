from etherscanv2 import __base_url, __connect_api
from urllib.parse import urlencode


def txnbridge(apikey: str, chainid: int, address: str, blocktype: str, page: int, offset: int):
    params, module, action = locals(), "account", "txnbridge"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)
