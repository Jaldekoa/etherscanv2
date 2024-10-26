from etherscanv2 import EtherScanV2


class Transactions(EtherScanV2):
    def getstatus(self, **params):
        return self.__connect_api("transaction", "getstatus", params)

    def gettxreceiptstatus(self, **params):
        return self.__connect_api("transaction", "gettxreceiptstatus", params)

    def gettxreceiptstatus(self, **params):
        return self.__connect_api("transaction", "gettxreceiptstatus", params)
