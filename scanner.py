# scanner.py
from pybit.unified_trading import HTTP
from config import API_KEY, API_SECRET
from strategies import apply_strategies
import time

session = HTTP(api_key=API_KEY, api_secret=API_SECRET)

def scan_market():
    symbols = ["BTCUSDT", "ETHUSDT"]  # Add more pairs
    signals = []

    for symbol in symbols:
        try:
            data = session.get_kline(category="linear", symbol=symbol, interval="15", limit=50)
            candles = data["result"]["list"]
            latest_close = float(candles[-1][4])
            ema_15 = sum([float(c[4]) for c in candles[-15:]]) / 15
            rsi = 50  # Placeholder (insert actual RSI calc)

            decision = apply_strategies({
                "price": latest_close,
                "ema_15": ema_15,
                "rsi": rsi
            })

            if decision:
                signals.append((symbol, decision, latest_close))
        except Exception as e:
            print(f"Scan error for {symbol}: {e}")

    return signals
