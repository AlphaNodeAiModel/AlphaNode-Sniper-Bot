# telegram_alerts.py
import requests
from config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID

def send_signal(symbol, direction, price):
    msg = f"""
🚨 AlphaNode Signal 🚨
📡 Pair: ${symbol.replace('USDT', '')} / USDT
🟢 Direction: {direction}
⚙️ Leverage: ⚡ 10x
🔗 Margin: Cross
📌 Entry: ${price}

🎯 TP1 → +30%
🎯 TP2 → +50%
🎯 TP3 → +100%
🎯 TP4 → +150%

❌ SL → -15%
"""
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": TELEGRAM_CHAT_ID, "text": msg}
    requests.post(url, data=dat
