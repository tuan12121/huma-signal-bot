import requests
from datetime import datetime

def get_recent_candles(symbol='HUMAUSDT', interval='1m', limit=20):
    url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        candles = []
        for entry in data:
            candles.append({
                'time': datetime.fromtimestamp(entry[0] / 1000).strftime('%Y-%m-%d %H:%M'),
                'open': float(entry[1]),
                'high': float(entry[2]),
                'low': float(entry[3]),
                'close': float(entry[4]),
                'volume': float(entry[5]),
            })
        return candles
    except Exception as e:
        print("Error fetching candles:", e)
        return []