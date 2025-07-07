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

