from etherscanv2 import __base_url, __connect_api
from urllib.parse import urlencode


def eth_blockNumber(apikey: str, chainid: int):
    params, module, action = locals(), "proxy", "eth_blockNumber"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)


def eth_getBlockByNumber(apikey: str, chainid: int, tag: str, boolean: str):
    params, module, action = locals(), "proxy", "eth_getBlockByNumber"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)


def eth_getUncleByBlockNumberAndIndex(apikey: str, chainid: int, tag: str, index: str):
    params, module, action = locals(), "proxy", "eth_getUncleByBlockNumberAndIndex"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)


def eth_getBlockTransactionCountByNumber(apikey: str, chainid: int, tag: str):
    params, module, action = locals(), "proxy", "eth_getBlockTransactionCountByNumber"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)


def eth_getTransactionByHash(apikey: str, chainid: int, txhash: str):
    params, module, action = locals(), "proxy", "eth_getTransactionByHash"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)


def eth_getTransactionByBlockNumberAndIndex(apikey: str, chainid: int, tag: str, index: str):
    params, module, action = locals(), "proxy", "eth_getTransactionByBlockNumberAndIndex"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)


def eth_getTransactionCount(apikey: str, chainid: int, address: str, tag: str):
    params, module, action = locals(), "proxy", "eth_getTransactionCount"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)


def eth_sendRawTransaction(apikey: str, chainid: int, address: str, hex: str):
    params, module, action = locals(), "proxy", "eth_sendRawTransaction"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)


def eth_getTransactionReceipt(apikey: str, chainid: int, address: str, txhash: str):
    params, module, action = locals(), "proxy", "eth_getTransactionReceipt"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)


def eth_call(apikey: str, chainid: int, address: str, to: str, data: str, tag: str):
    params, module, action = locals(), "proxy", "eth_call"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)


def eth_getCode(apikey: str, chainid: int, address: str, tag: str):
    params, module, action = locals(), "proxy", "eth_getCode"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)


def eth_getStorageAt(apikey: str, chainid: int, address: str, position: str, tag: str):
    params, module, action = locals(), "proxy", "eth_getStorageAt"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)


def eth_gasPrice(apikey: str, chainid: int):
    params, module, action = locals(), "proxy", "eth_gasPrice"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)


def eth_estimateGas(apikey: str, chainid: int, data: str, to: str, value: str, gas: str, gasprice: str):
    params, module, action = locals(), "proxy", "eth_estimateGas"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)
