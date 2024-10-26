from etherscanv2 import __base_url, __connect_api
from urllib.parse import urlencode


def getcontractcreation(apikey: str, chainid: int, contractaddresses: str):
    params, module, action = locals(), "contract", "getcontractcreation"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)


def verifysourcecode(apikey: str, chainid: int, codeformat: str, sourcecode: str, constructorarguments: str, contractaddress: str, contractname:str, compilerversion: str):
    params, module, action = locals(), "contract", "verifysourcecode"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)


def checkverifystatus(apikey: str, chainid: int, guid: str):
    params, module, action = locals(), "contract", "verifysourcecode"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)


def verifyproxycontract(apikey: str, chainid: int, address: str, expectedimplementation: str = None):
    params, module, action = locals(), "contract", "verifyproxycontract"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)
    pass

def checkproxyverification(apikey: str, chainid: int, guid: str):
    params, module, action = locals(), "contract", "checkproxyverification"
    url = f"{__base_url}?module={module}&action={action}&{urlencode(params)}"
    return __connect_api(url)
