Due to duck typing the`trade()` isnt really aware of `EthereumTradingBot` and `BitcoinTradingBot` 

Therefore it is possible to segregate different ideas lumped together in the `TradingEngine`

Protocol segregation provides an alternative to mixins as it doesnt have the baggage of the latter
