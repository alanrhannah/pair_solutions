def get_max_profit(stock_prices_yesterday):
    if len(stock_prices_yesterday) < 2:
        raise IndexError('Getting a profit requires at least 2 prices')

    min_price = stock_prices_yesterday[0]
    max_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]

    for current_price in stock_prices_yesterday[1:]:
        # current price - the lowest price so far
        potential_profit = current_price - min_price
        # highest
        max_profit = max(max_profit, potential_profit)
        # lowest
        min_price  = min(min_price, current_price)

    return max_profit

if __name__ == '__main__':
    stocks = [10, 20, 40, 10, 60, 100, 5, 50, 20]
    print get_max_profit(stocks)
    stocks = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
    print get_max_profit(stocks)
