from urllib.parse import urlencode
from accounts import Accounts
from contracts import Contracts
from transactions import Transactions
from blocks import Blocks
from logs import Logs
from proxys import Proxy
from tokens import Tokens
from gastracker import GasTracker
from stats import Stats
from chainspecific import ChainSpecific
from usage import Usage
import requests

__all__ = ["EtherScanV2", "Accounts", "Contracts", "Transactions", "Blocks", "Logs", "Proxy", "Tokens", "GasTracker", "Stats", "ChainSpecific", "Usage"]


class Metadata:
    base_url: str = "https://api.etherscan.io/v2/api"
    supported_chains: dict[str, int] = {
        "Etherscan": 1,
        "Sepolia Etherscan": 11155111,
        "Holesky Etherscan": 17000,
        "BscScan": 56,
        "Testnet BscScan": 97,
        "PolygonScan": 137,
        "Testnet PolygonScan": 80002,
        "zkEVM PolygonScan": 1101,
        "Testnet zkEVM PolygonScan": 2442,
        "BaseScan": 8453,
        "Testnet BaseScan": 84532,
        "Arbiscan": 42161,
        "Nova Arbiscan": 42170,
        "Sepolia Arbiscan": 421614,
        "LineaScan": 59144,
        "Testnet LineaScan": 59141,
        "FTMScan": 250,
        "Testnet FTMScan": 4002,
        "BlastScan": 81457,
        "Testnet BlastScan": 168587773,
        "Optimistic Etherscan": 10,
        "Sepolia Optimistic Etherscan": 11155420,
        "SnowScan": 43114,
        "Fuji SnowScan": 43113,
        "BTTCScan": 199,
        "Donau BTTCScan": 1028,
        "CeloScan": 42220,
        "Alfajores CeloScan": 44787,
        "Cronoscan": 25,
        "Fraxscan": 252,
        "Testnet Fraxscan": 2522,
        "GnosisScan": 100,
        "KromaScan": 255,
        "Testnet KromaScan": 2358,
        "Mantlescan": 5000,
        "Testnet Mantlescan": 5003,
        "Moonbeam Moonscan": 1284,
        "Moonriver Moonscan": 1285,
        "Moonbase Moonscan": 1287,
        "opBNB BscScan": 204,
        "Testnet opBNB BscScan": 5611,
        "ScrollScan": 534352,
        "Testnet ScrollScan": 534351,
        "Taikoscan": 167000,
        "Testnet Taikoscan": 167009,
        "WemixScan": 1111,
        "Testnet WemixScan": 1112,
        "zkSync Era": 324,
        "Testnet zkSync Era": 300,
        "Xaiscan": 660279,
        "Sepolia Xaiscan": 37714555429
    }

    valid_params = {
        # Accounts
        'balance': ['address', 'tag'],
        'balancemulti': ['address', 'tag'],
        'txlist': ['address', 'startblock', 'endblock', 'page', 'offset', 'sort'],
        'txlistinternal': ['address', 'txhash', 'startblock', 'endblock', 'page', 'offset', 'sort'],
        'tokentx': ['address', 'contractaddress', 'page', 'offset', 'startblock', 'endblock', 'sort'],
        'tokennfttx': ['address', 'contractaddress', 'page', 'offset', 'startblock', 'endblock', 'sort'],
        'token1155tx': ['address', 'contractaddress', 'page', 'offset', 'startblock', 'endblock', 'sort'],
        'getminedblocks': ['address', 'blocktype', 'page', 'offset'],
        'txsBeaconWithdrawal': ['address', 'contractaddress', 'page', 'offset', 'startblock', 'endblock', 'sort'],
        'balancehistory': ['address', 'blockno'],

        # Contracts
        'getabi': ['address'],
        'getsourcecode': ['address'],
        'getcontractcreation': ['contractaddress'],
        'verifysourcecode': ['codeformat', 'sourceCode', 'constructorArguements', 'contractaddress', 'contractname', 'compilerversion'],
        'checkverifystatus': ['guid'],
        'verifyproxycontract': ['address'],
        'checkproxyverification': ['guid'],

        # Transactions
        'getstatus': ['txhash'],
        'gettxreceiptstatus': ['txhash'],

        # Block
        'getblockreward': ['blockno'],
        'getblockcountdown': ['blockno'],
        'getblocknobytime': ['timestamp', 'closest'],
        'dailyavgblocksize': ['startdate', 'enddate', 'sort'],
        'dailyblkcount': ['startdate', 'enddate', 'sort'],
        'dailyblockrewards': ['startdate', 'enddate', 'sort'],
        'dailyavgblocktime': ['startdate', 'enddate', 'sort'],
        'dailyuncleblkcount': ['startdate', 'enddate', 'sort'],

        # Logs
        'getLogs': ['address', 'fromBlock', 'toBlock', 'topic', 'topicOperator', 'page', 'offset'],

        # Geth/Parity Proxy
        'eth_blockNumber': [],
        'eth_getBlockByNumber': ['tag', 'boolean'],
        'eth_getUncleByBlockNumberAndIndex': ['tag', 'index'],
        'eth_getBlockTransactionCountByNumber': ['tag'],
        'eth_getTransactionByHash': ['txhash'],
        'eth_getTransactionByBlockNumberAndIndex': ['tag', 'index'],
        'eth_getTransactionCount': ['address', 'tag'],
        'eth_sendRawTransaction': ['hex'],
        'eth_getTransactionReceipt': ['txhash'],
        'eth_call': ['to', 'data', 'tag'],
        'eth_getCode': ['address', 'tag'],
        'eth_getStorageAt': ['address', 'position'],
        'eth_gasPrice': [],
        'eth_estimateGas': ['data', 'to', 'value', 'gas', 'gasPrice'],

        # Token
        'tokensupply': ['contractaddress'],
        'tokenbalance': ['contractaddress', 'address'],
        'tokensupplyhistory': ['contractaddress', 'blockno'],
        'tokenbalancehistory': ['contractaddress', 'address', 'blockno'],
        'tokenholderlist': ['contractaddress', 'page', 'offset'],
        'tokeninfo': ['contractaddress'],
        'addresstokenbalance': ['address', 'page', 'offset'],
        'addresstokennftbalance': ['address', 'page', 'offset'],
        'addresstokennftinventory': ['address', 'contractaddress', 'page', 'offset'],

        # Gas Tracker
        'gasestimate': ['gasprice'],
        'gasoracle': [],
        'dailyavggaslimit': ['startdate', 'enddate', 'sort'],
        'dailygasused': ['startdate', 'enddate', 'sort'],
        'dailyavggasprice': ['startdate', 'enddate', 'sort'],

        # Stats
        'ethsupply': [],
        'ethsupply2': [],
        'ethprice': [],
        'chainsize': ['startdate', 'enddate', 'clienttype', 'syncmode', 'sort'],
        'nodecount': [],
        'dailytxnfee': ['startdate', 'enddate', 'sort'],
        'dailynewaddress': ['startdate', 'enddate', 'sort'],
        'dailynetutilization': ['startdate', 'enddate', 'sort'],
        'dailyavghashrate': ['startdate', 'enddate', 'sort'],
        'dailytx': ['startdate', 'enddate', 'sort'],
        'dailyavgnetdifficulty': ['startdate', 'enddate', 'sort'],
        'ethdailymarketcap': ['startdate', 'enddate', 'sort'],
        'ethdailyprice': ['startdate', 'enddate', 'sort'],

        # Chain Specific
        'txnbridge': ['address', 'blocktype', 'page', 'offset'],

        # Usage
        'getapilimit': [],
    }


class EtherScanV2:
    def __init__(self, apikey: str, chainid: str) -> None:
        self.__base_url: str = Metadata.base_url
        self.api_key: str = apikey
        self.chain_id: str = chainid
        self.__valid_params = Metadata.valid_params

    def __connect_api(self, module: str, action: str, params: dict):
        api_params = {k: v for k, v in params.items() if k in self.__valid_params[action]}
        url = f"{self.__base_url}?module={module}&action={action}&{urlencode(api_params)}"
        res = requests.get(url).json()
        if res['status'] == '0' or res['message'] == 'NOTOK':
            raise Exception(res['result'])
        return res['result']
