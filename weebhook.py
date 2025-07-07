# This Python script receives TradingView alerts via webhook
# and places orders via Binance API (can be adapted to Zerodha)

from flask import Flask, request, jsonify
from binance.client import Client
from binance.enums import *
import json

app = Flask(__name__)

# === Binance API Setup ===
API_KEY = 'your_api_key'
API_SECRET = 'your_api_secret'
client = Client(API_KEY, API_SECRET)

# === Configuration ===
symbol = "BTCUSDT"
quantity = 0.001  # adjust per your balance

# === Flask Webhook Receiver ===
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json

    print("Received alert:", data)

    if data['action'] == 'buy':
        order = client.order_market_buy(symbol=symbol, quantity=quantity)
        print("Buy order placed.", order)
        return jsonify({"status": "buy order sent"})

    elif data['action'] == 'sell':
        order = client.order_market_sell(symbol=symbol, quantity=quantity)
        print("Sell order placed.", order)
        return jsonify({"status": "sell order sent"})

    return jsonify({"status": "unknown action"})
-------------------------------------------------------------------------------
# === Run the server ===
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

// Load higher timeframe trend (e.g., 1H on 15min chart)
emaHTF = request.security(syminfo.tickerid, "60", ta.ema(close, 50))
trendConfirm = close > emaHTF  // Use only if price is above HTF trend

// Add this to your buySignal condition:
buySignal := buySignal and trendConfirm
---------------------------------------------------------------------------------
reversalBuy = ta.crossover(close, lowerBB) and rsi < 40
reversalSell = ta.crossunder(close, upperBB) and rsi > 60

if reversalBuy
    strategy.entry("Reversal Buy", strategy.long)
    strategy.exit("TP/SL Reversal", from_entry="Reversal Buy", profit=takeProfitPerc * 0.01, loss=stopLossPerc * 0.01)

if reversalSell
    strategy.entry("Reversal Sell", strategy.short)
    strategy.exit("TP/SL Reversal", from_entry="Reversal Sell", profit=takeProfitPerc * 0.01, loss=stopLossPerc * 0.01)

alertcondition(reversalBuy, title="Reversal Buy Alert", message="Reversal Buy Triggered!")
alertcondition(reversalSell, title="Reversal Sell Alert", message="Reversal Sell Triggered!")
