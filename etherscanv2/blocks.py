class Blocks:

    def __init__(self, etherscan: 'EtherScanV2'):
        self.etherscan = etherscan

    def getblockreward(self, **params):
        return self.etherscan._EtherScanV2__connect_api("block", "getblockreward", params)

    def getblockcountdown(self, **params):
        return self.etherscan._EtherScanV2__connect_api("block", "getblockcountdown", params)

    def getblocknobytime(self, **params):
        return self.etherscan._EtherScanV2__connect_api("block", "getblocknobytime", params)

    def dailyavgblocksize(self, **params):
        return self.etherscan._EtherScanV2__connect_api("stats", "dailyavgblocksize", params)

    def dailyblkcount(self, **params):
        return self.etherscan._EtherScanV2__connect_api("stats", "dailyblkcount", params)

    def dailyblockrewards(self, **params):
        return self.etherscan._EtherScanV2__connect_api("stats", "dailyblockrewards", params)

    def dailyavgblocktime(self, **params):
        return self.etherscan._EtherScanV2__connect_api("stats", "dailyavgblocktime", params)

    def dailyuncleblkcount(self, **params):
        return self.etherscan._EtherScanV2__connect_api("stats", "dailyuncleblkcount", params)
