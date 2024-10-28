class Contracts:

    def __init__(self, etherscan: 'EtherScanV2'):
        self.etherscan = etherscan

    def getabi(self, **params):
        return self.etherscan._EtherScanV2__connect_api("contract", "getabi", params)

    def getsourcecode(self, **params):
        return self.etherscan._EtherScanV2__connect_api("contract", "getsourcecode", params)

    def getcontractcreation(self, **params):
        return self.etherscan._EtherScanV2__connect_api("contract", "getcontractcreation", params)

    def verifysourcecode(self, **params):
        return self.etherscan._EtherScanV2__connect_api("contract", "verifysourcecode", params)

    def checkverifystatus(self, **params):
        return self.etherscan._EtherScanV2__connect_api("contract", "checkverifystatus", params)

    def verifyproxycontract(self, **params):
        # ⚠️ ONLY POST METHOD ⚠️
        return self.etherscan._EtherScanV2__connect_api("contract", "verifyproxycontract", params)

    def checkproxyverification(self, **params):
        return self.etherscan._EtherScanV2__connect_api("contract", "checkproxyverification", params)
