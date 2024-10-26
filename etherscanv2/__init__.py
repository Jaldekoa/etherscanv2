import requests

__base_url: str = "https://api.etherscan.io/v2/api"


def __connect_api(url: str):
    return requests.get(url).json()['result']


SUPPORTED_CHAINS: dict[str, int] = {
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
