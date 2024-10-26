from etherscanv2 import EtherScanV2


class ChainSpecific(EtherScanV2):
    def txnbridge(self, **params):
        return self.__connect_api("account", "txnbridge", params)
