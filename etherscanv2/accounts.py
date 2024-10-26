from etherscanv2 import EtherScanV2


class Accounts(EtherScanV2):
    def balance(self, **params):
        return self.__connect_api("account", "balance", params)

    def balancemulti(self, **params):
        return self.__connect_api("account", "balancemulti", params)

    def txlist(self, **params):
        return self.__connect_api("account", "txlist", params)

    def txlistinternal(self, **params):
        return self.__connect_api("account", "txlistinternal", params)

    def tokentx(self, **params):
        return self.__connect_api("account", "tokentx", params)

    def tokennfttx(self, **params):
        return self.__connect_api("account", "tokennfttx", params)

    def token1155tx(self, **params):
        return self.__connect_api("account", "token1155tx", params)

    def getminedblocks(self, **params):
        return self.__connect_api("account", "getminedblocks", params)

    def txsbeaconwithdrawal(self, **params):
        return self.__connect_api("account", "txsBeaconWithdrawal", params)

    def balancehistory(self, **params):
        return self.__connect_api("account", "balancehistory", params)
