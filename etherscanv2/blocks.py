from etherscanv2 import EtherScanV2


class Blocks(EtherScanV2):
    def getblockreward(self, **params):
        return self.__connect_api("block", "getblockreward", params)

    def getblockcountdown(self, **params):
        return self.__connect_api("block", "getblockcountdown", params)

    def getblocknobytime(self, **params):
        return self.__connect_api("block", "getblocknobytime", params)

    def dailyavgblocksize(self, **params):
        return self.__connect_api("stats", "dailyavgblocksize", params)

    def dailyblkcount(self, **params):
        return self.__connect_api("stats", "dailyblkcount", params)

    def dailyblockrewards(self, **params):
        return self.__connect_api("stats", "dailyblockrewards", params)

    def dailyavgblocktime(self, **params):
        return self.__connect_api("stats", "dailyavgblocktime", params)

    def dailyuncleblkcount(self, **params):
        return self.__connect_api("stats", "dailyuncleblkcount", params)
