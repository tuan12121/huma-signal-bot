from flask import Flask, render_template, jsonify
import threading, time
from binance_api import get_recent_candles
from strategies import signal_generator

app = Flask(__name__)

bot_running = False
last_signal = "NONE"
last_candle_time = ""

def run_bot():
    global bot_running, last_signal, last_candle_time
    while bot_running:
        candles = get_recent_candles()
        if candles:
            signal = signal_generator(candles)
            last_signal = signal
            last_candle_time = candles[-1]['time']
        time.sleep(60)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start')
def start():
    global bot_running
    if not bot_running:
        bot_running = True
        threading.Thread(target=run_bot).start()
    return jsonify({'status': 'started'})

@app.route('/stop')
def stop():
    global bot_running
    bot_running = False
    return jsonify({'status': 'stopped'})

@app.route('/status')
def status():
    return jsonify({
        'running': bot_running,
        'last_signal': last_signal,
        'last_candle_time': last_candle_time
    })

if __name__ == '__main__':
    app.run(debug=True)