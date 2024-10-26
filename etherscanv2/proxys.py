from etherscanv2 import EtherScanV2


class Proxy(EtherScanV2):
    def eth_blockNumber(self, **params):
        return self.__connect_api("proxy", "eth_blockNumber", params)

    def eth_getBlockByNumber(self, **params):
        return self.__connect_api("proxy", "eth_getBlockByNumber", params)

    def eth_getUncleByBlockNumberAndIndex(self, **params):
        return self.__connect_api("proxy", "eth_getUncleByBlockNumberAndIndex", params)

    def eth_getBlockTransactionCountByNumber(self, **params):
        return self.__connect_api("proxy", "eth_getBlockTransactionCountByNumber", params)

    def eth_getTransactionByHash(self, **params):
        return self.__connect_api("proxy", "eth_getTransactionByHash", params)

    def eth_getTransactionByBlockNumberAndIndex(self, **params):
        return self.__connect_api("proxy", "eth_getTransactionByBlockNumberAndIndex", params)

    def eth_getTransactionCount(self, **params):
        return self.__connect_api("proxy", "eth_getTransactionCount", params)

    def eth_sendRawTransaction(self, **params):
        return self.__connect_api("proxy", "eth_sendRawTransaction", params)

    def eth_getTransactionReceipt(self, **params):
        return self.__connect_api("proxy", "eth_getTransactionReceipt", params)

    def eth_call(self, **params):
        return self.__connect_api("proxy", "eth_call", params)

    def eth_getCode(self, **params):
        return self.__connect_api("proxy", "eth_getCode", params)

    def eth_getStorageAt(self, **params):
        return self.__connect_api("proxy", "eth_getStorageAt", params)

    def eth_gasPrice(self, **params):
        return self.__connect_api("proxy", "eth_gasPrice", params)

    def eth_estimateGas(self, **params):
        return self.__connect_api("proxy", "eth_estimateGas", params)
