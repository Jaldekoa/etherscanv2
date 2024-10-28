import requests

class Usage:

    def __init__(self, etherscan):
        self.etherscan = etherscan

    def getapilimit(self, **params):
        return self.etherscan._EtherScanV2__connect_api("getapilimit", "getapilimit", params)

    def chainlist(self):
        return requests.get("https://api.etherscan.io/v2/chainlist").json()['result']
