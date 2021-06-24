#!/usr/bin/env python

import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

key = ""
secret = ""

spot_client = Client(key, secret)
logging.info(
    spot_client.managed_sub_account_withdraw(
        fromEmail="alice@test.com", asset="USDT", amount=0.01
    )
)