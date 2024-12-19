class TradeManager:
    def __init__(self, exchange_rates: dict[str, dict[str, int]], main_herd: dict[str, int]):
        self.exchange_rates = exchange_rates
        self.main_herd = main_herd