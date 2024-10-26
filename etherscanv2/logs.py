from etherscanv2 import EtherScanV2


class Logs(EtherScanV2):
    def getLogs(self, **params):
        return self.__connect_api("logs", "getLogs", params)
