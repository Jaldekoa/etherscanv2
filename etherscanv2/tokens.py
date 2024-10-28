class Tokens:

    def __init__(self, etherscan):
        self.etherscan = etherscan

    def tokensupply(self, **params):
        return self.etherscan._EtherScanV2__connect_api("stats", "tokensupply", params)

    def tokenbalance(self, **params):
        return self.etherscan._EtherScanV2__connect_api("account", "tokenbalance", params)

    def tokensupplyhistory(self, **params):
        return self.etherscan._EtherScanV2__connect_api("stats", "tokensupplyhistory", params)

    def tokenbalancehistory(self, **params):
        return self.etherscan._EtherScanV2__connect_api("account", "tokenbalancehistory", params)

    def tokenholderlist(self, **params):
        return self.etherscan._EtherScanV2__connect_api("token", "tokenholderlist", params)

    def tokeninfo(self, **params):
        return self.etherscan._EtherScanV2__connect_api("token", "tokeninfo", params)

    def addresstokenbalance(self, **params):
        return self.etherscan._EtherScanV2__connect_api("account", "addresstokenbalance", params)

    def addresstokennftbalance(self, **params):
        return self.etherscan._EtherScanV2__connect_api("account", "addresstokennftbalance", params)

    def addresstokennftinventory(self, **params):
        return self.etherscan._EtherScanV2__connect_api("account", "addresstokennftinventory", params)
