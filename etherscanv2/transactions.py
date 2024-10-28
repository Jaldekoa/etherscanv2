class Transactions:

    def __init__(self, etherscan):
        self.etherscan = etherscan

    def getstatus(self, **params):
        return self.etherscan._EtherScanV2__connect_api("transaction", "getstatus", params)

    def gettxreceiptstatus(self, **params):
        return self.etherscan._EtherScanV2__connect_api("transaction", "gettxreceiptstatus", params)

    def gettxreceiptstatus(self, **params):
        return self.etherscan._EtherScanV2__connect_api("transaction", "gettxreceiptstatus", params)
