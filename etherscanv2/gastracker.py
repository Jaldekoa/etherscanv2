from etherscanv2 import __base_url, __connect_api
from urllib.parse import urlencode


def gasestimate(apikey: str, chainid: int, gasprice: int):
    params, module, action = locals(), "gastracker", "gasestimate"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)


def gasoracle(apikey: str, chainid: int):
    params, module, action = locals(), "gastracker", "gasoracle"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)


def gasoracle(apikey: str, chainid: int, startdate: str, enddate: str, sort: str):
    params, module, action = locals(), "stats", "dailyavggaslimit"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)


def dailygasused(apikey: str, chainid: int, startdate: str, enddate: str, sort: str):
    params, module, action = locals(), "stats", "dailygasused"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)


def dailyavggasprice(apikey: str, chainid: int, startdate: str, enddate: str, sort: str):
    params, module, action = locals(), "stats", "dailyavggasprice"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)
