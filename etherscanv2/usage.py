from etherscanv2 import EtherScanV2
import requests


class Usage(EtherScanV2):
    def getapilimit(self):
        return self.__connect_api("getapilimit", "getapilimit", params)

    def chainlist(self):
        return requests.get("https://api.etherscan.io/v2/chainlist").json()['result']
