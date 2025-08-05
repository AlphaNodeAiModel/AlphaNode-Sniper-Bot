# strategies.py
def apply_strategies(candle_data):
    # Example strategy (you can expand)
    if candle_data["rsi"] < 30 and candle_data["ema_15"] > candle_data["price"]:
        return "LONG"
    elif candle_data["rsi"] > 70 and candle_data["ema_15"] < candle_data["price"]:
        return "SHORT"
    return None
