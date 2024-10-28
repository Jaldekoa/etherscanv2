from etherscanv2 import EtherScanV2
from dotenv import load_dotenv
import pytest
import os


def test_balance():
    load_dotenv()
    eth = EtherScanV2(apikey=os.getenv("ETHERSCAN_API_KEY"), chainid=1)
    result = eth.Account.balance(address="0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae")
    assert isinstance(result, str)
