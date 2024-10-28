class Stats:

    def __init__(self, etherscan: 'EtherScanV2'):
        self.etherscan = etherscan

    def ethsupply(self, **params):
        return self.etherscan._EtherScanV2__connect_api("stats", "ethsupply", params)

    def ethsupply2(self, **params):
        return self.etherscan._EtherScanV2__connect_api("stats", "ethsupply2", params)

    def ethprice(self, **params):
        return self.etherscan._EtherScanV2__connect_api("stats", "ethprice", params)

    def chainsize(self, **params):
        return self.etherscan._EtherScanV2__connect_api("stats", "chainsize", params)

    def nodecount(self, **params):
        return self.etherscan._EtherScanV2__connect_api("stats", "nodecount", params)

    def dailytxnfee(self, **params):
        return self.etherscan._EtherScanV2__connect_api("stats", "dailytxnfee", params)

    def dailynewaddress(self, **params):
        return self.etherscan._EtherScanV2__connect_api("stats", "dailynewaddress", params)

    def dailynetutilization(self, **params):
        return self.etherscan._EtherScanV2__connect_api("stats", "dailynetutilization", params)

    def dailyavghashrate(self, **params):
        return self.etherscan._EtherScanV2__connect_api("stats", "dailyavghashrate", params)

    def dailytx(self, **params):
        return self.etherscan._EtherScanV2__connect_api("stats", "dailytx", params)

    def dailyavgnetdifficulty(self, **params):
        return self.etherscan._EtherScanV2__connect_api("stats", "dailyavgnetdifficulty", params)

    def ethdailymarketcap(self, **params):
        return self.etherscan._EtherScanV2__connect_api("stats", "ethdailymarketcap", params)

    def ethdailyprice(self, **params):
        return self.etherscan._EtherScanV2__connect_api("stats", "ethdailyprice", params)
