class ChainSpecific:

    def __init__(self, etherscan):
        self.etherscan = etherscan

    def txnbridge(self, **params):
        return self.etherscan._EtherScanV2__connect_api("account", "txnbridge", params)
