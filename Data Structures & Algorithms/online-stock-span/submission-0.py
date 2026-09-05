class StockSpanner:

    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int:
        self.prices.append(price)
        
        l = len(self.prices) - 1

        while price >= self.prices[l] and l >= 0:
            l -= 1

        return len(self.prices) - l - 1



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)