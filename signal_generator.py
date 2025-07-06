def is_bullish_engulfing(candles):
    if len(candles) < 2:
        return False
    prev = candles[-2]
    curr = candles[-1]
    return prev['close'] < prev['open'] and curr['close'] > curr['open'] and curr['close'] > prev['open'] and curr['open'] < prev['close']

def signal_generator(candles):
    if is_bullish_engulfing(candles):
        return "BUY"
    if candles[-1]['close'] < candles[-2]['close']:
        return "SELL"
    return "NONE"