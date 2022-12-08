# For take profit, create a limit order with same size, opposite side and 'reduceOnly':true parameter.
def setTp(exchange, symbol: str, side: str, size: int, tp: float):
    params = dict(reduceOnly=True)
    side = 'sell' if side=='buy' else 'buy'
    try:
        res = exchange.createOrder(symbol, 'limit', side, size, price=tp, params=params)
        return res
    except Exception as e:
        print(e)


