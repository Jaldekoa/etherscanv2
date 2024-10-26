from etherscanv2 import __base_url, __connect_api
from urllib.parse import urlencode


def getapilimit(apikey: str, chainid: int):
    params, module, action = locals(), "getapilimit", "getapilimit"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)

def chainlist():
    return __connect_api("https://api.etherscan.io/v2/chainlist")
