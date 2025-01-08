from flask import Flask, jsonify
from data_fetcher import fetch_crypto_data
from data_analyzer import analyze_data
from flask_cors import CORS


app = Flask(__name__)

CORS(app)

@app.route('/api/crypto-data', methods=['GET'])
def fetch_data():
    result_list = fetch_crypto_data()
    data = result_list[0]
    data_timeStamp = result_list[1]

    if data.empty:
        return jsonify({"error": "Failed to fetch data"}), 500

    return jsonify({"data": data.to_dict(orient='records')
    ,"timestamp":data_timeStamp})

@app.route('/api/crypto-analysis', methods=['GET'])
def analyze():
    result_list = fetch_crypto_data()

    data = result_list[0]
    data_timeStamp = result_list[1]

    if data.empty:
        return jsonify({"error": "Failed to fetch data"}), 500
    analysis = analyze_data(data)

    return jsonify({"data": analysis
    ,"timestamp":data_timeStamp})

if __name__ == '__main__':
    app.run(debug=True)