from etherscanv2 import EtherScanV2


class GasTracker(EtherScanV2):
    def gasestimate(self, **params):
        return self.__connect_api("gastracker", "gasestimate", params)

    def gasoracle(self, **params):
        return self.__connect_api("gastracker", "gasoracle", params)

    def dailyavggaslimit(self, **params):
        return self.__connect_api("stats", "dailyavggaslimit", params)

    def dailygasused(self, **params):
        return self.__connect_api("stats", "dailygasused", params)

    def dailyavggasprice(self, **params):
        return self.__connect_api("stats", "dailyavggasprice", params)
