
from typing import Protocol


class TradingEngine(Protocol):
    def buy(self, amount: int) -> None:
        """Buy the asset"""
   
    def sell(self, amount: int) -> None:
        """Sell the asset"""
   
   
    def get_price_data(self) -> list[int]:
        """ Get the price data"""
   
    def get_amount(self) -> int:
        """Get the amount to trade"""


class TradingStrategy(Protocol):
    def should_buy(self, prices: list[int]) -> bool:
        """Whether to buy"""
   
    def should_sell(self, prices: list[int]) -> bool:
        """Whether to sell """
        


def trade(engine:TradingEngine, strategy :TradingStrategy) -> None:
    prices = engine.get_price_data()
    amount = engine.get_amount()

    if strategy.should_buy(prices):
        engine.buy(amount)
    if strategy.should_sell(prices):
        engine.sell(amount)