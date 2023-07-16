from bitcoin import BitcoinTradingBot
from ethereum import EthereumTradingBot
from simple_strategy import SimpleStrategy
from trading_bot import trade


def main():
    bitcoin_trader = BitcoinTradingBot()
    # trade(bitcoin_trader, bitcoin_trader) # note that the arguments can be the same object as all required methods in the same object
    trade(bitcoin_trader, SimpleStrategy()) # note that the arguments can be the same object as all required methods in the same object

    ethereum_trader = EthereumTradingBot()
    trade(ethereum_trader, SimpleStrategy())


if __name__ == "__main__":
    main()
