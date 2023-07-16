Instead of ABC, the TrandingEngine is now a protocal class

A usual function is define outside the class hierarchy which in turn takes the Protocol as the argument


### Concerns
Aren't the objects of `EthereumTradingBot` and `BitcoinTradingBot` containing too much info for the `trade()` method?