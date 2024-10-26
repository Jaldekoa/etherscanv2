from etherscanv2 import __base_url, __connect_api
from urllib.parse import urlencode


def getlogs_address(apikey: str, chainid: int, address: str, fromblock: int, toblock: int, page: int, offset: int):
    params, module, action = locals(), "logs", "getLogs"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)

def getlogs_topics(apikey: str, chainid: int, fromblock: int, toblock: int, topic: str, topicoperator: str, page: int, offset: int):
    params, module, action = locals(), "logs", "getLogs"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)


def getlogs_address_topics(apikey: str, chainid: int, fromblock: int, toblock: int, address: str,  topic: str, topicoperator: str, page: int, offset: int):
    params, module, action = locals(), "logs", "getLogs"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)
