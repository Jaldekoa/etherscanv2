class GasTracker:

    def __init__(self, etherscan):
        self.etherscan = etherscan

    def gasestimate(self, **params):
        return self.etherscan._EtherScanV2__connect_api("gastracker", "gasestimate", params)

    def gasoracle(self, **params):
        return self.etherscan._EtherScanV2__connect_api("gastracker", "gasoracle", params)

    def dailyavggaslimit(self, **params):
        return self.etherscan._EtherScanV2__connect_api("stats", "dailyavggaslimit", params)

    def dailygasused(self, **params):
        return self.etherscan._EtherScanV2__connect_api("stats", "dailygasused", params)

    def dailyavggasprice(self, **params):
        return self.etherscan._EtherScanV2__connect_api("stats", "dailyavggasprice", params)
