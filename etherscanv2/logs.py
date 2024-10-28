class Logs:

    def __init__(self, etherscan: 'EtherScanV2'):
        self.etherscan = etherscan

    def getLogs(self, **params):
        return self.etherscan._EtherScanV2__connect_api("logs", "getLogs", params)
