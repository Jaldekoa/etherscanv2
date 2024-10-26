from etherscanv2 import EtherScanV2


class Contracts(EtherScanV2):
    def getabi(self, **params):
        return self.__connect_api("contract", "getabi", params)

    def getsourcecode(self, **params):
        return self.__connect_api("contract", "getsourcecode", params)

    def getcontractcreation(self, **params):
        return self.__connect_api("contract", "getcontractcreation", params)

    def verifysourcecode(self, **params):
        return self.__connect_api("contract", "verifysourcecode", params)

    def checkverifystatus(self, **params):
        return self.__connect_api("contract", "checkverifystatus", params)

    def verifyproxycontract(self, **params):
        return self.__connect_api("contract", "verifyproxycontract", params)

    def checkproxyverification(self, **params):
        return self.__connect_api("contract", "checkproxyverification", params)
