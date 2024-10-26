from etherscanv2 import __base_url, __connect_api
from urllib.parse import urlencode


def getblockreward(apikey: str, chainid: int, blockno: int):
    params, module, action = locals(), "block", "getblockreward"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)


def getblockcountdown(apikey: str, chainid: int, blockno: int):
    params, module, action = locals(), "block", "getblockcountdown"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)


def getblocknobytime(apikey: str, chainid: int, timestamp: int, closest: str):
    params, module, action = locals(), "block", "getblocknobytime"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)


def dailyavgblocksize(apikey: str, chainid: int, startdate: str, enddate: str, sort: str):
    params, module, action = locals(), "block", "dailyavgblocksize"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)


def dailyblkcount(apikey: str, chainid: int, startdate: str, enddate: str, sort: str):
    params, module, action = locals(), "stats", "dailyblkcount"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)


def dailyblockrewards(apikey: str, chainid: int, startdate: str, enddate: str, sort: str):
    params, module, action = locals(), "stats", "dailyblockrewards"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)


def dailyavgblocktime(apikey: str, chainid: int, startdate: str, enddate: str, sort: str):
    params, module, action = locals(), "stats", "dailyavgblocktime"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)


def dailyuncleblkcount(apikey: str, chainid: int, startdate: str, enddate: str, sort: str):
    params, module, action = locals(), "stats", "dailyuncleblkcount"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)
