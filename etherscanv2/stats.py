from etherscanv2 import __base_url, __connect_api
from urllib.parse import urlencode


def ethsupply(apikey: str, chainid: int):
    params, module, action = locals(), "stats", "ethsupply"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)

def ethsupply2(apikey: str, chainid: int):
    params, module, action = locals(), "stats", "ethsupply2"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)

def ethprice(apikey: str, chainid: int):
    params, module, action = locals(), "stats", "ethprice"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)

def chainsize(apikey: str, chainid: int, startdate: str, enddate: str, clienttype: str, syncmode: str, sort: str):
    params, module, action = locals(), "stats", "chainsize"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)

def nodecount(apikey: str, chainid: int):
    params, module, action = locals(), "stats", "nodecount"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)

def dailytxnfee(apikey: str, chainid: int):
    params, module, action = locals(), "stats", "dailytxnfee"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)

def dailynewaddress(apikey: str, chainid: int, startdate: str, enddate: str, sort: str):
    params, module, action = locals(), "stats", "dailynewaddress"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)

def dailynetutilization(apikey: str, chainid: int, startdate: str, enddate: str, sort: str):
    params, module, action = locals(), "stats", "dailynetutilization"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)

def dailyavghashrate(apikey: str, chainid: int, startdate: str, enddate: str, sort: str):
    params, module, action = locals(), "stats", "dailyavghashrate"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)

def dailytx(apikey: str, chainid: int, startdate: str, enddate: str, sort: str):
    params, module, action = locals(), "stats", "dailytx"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)

def dailyavgnetdifficulty(apikey: str, chainid: int, startdate: str, enddate: str, sort: str):
    params, module, action = locals(), "stats", "dailyavgnetdifficulty"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)

def ethdailymarketcap(apikey: str, chainid: int, startdate: str, enddate: str, sort: str):
    params, module, action = locals(), "stats", "ethdailymarketcap"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)

def ethdailymarketcap(apikey: str, chainid: int, startdate: str, enddate: str, sort: str):
    params, module, action = locals(), "stats", "ethdailymarketcap"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)

def ethdailyprice(apikey: str, chainid: int, startdate: str, enddate: str, sort: str):
    params, module, action = locals(), "stats", "ethdailyprice"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)
