from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "API działa!"})

# Funkcja pomocnicza, która zamienia na float lub zwraca 0.0
def safe_float(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return 0.0

@app.route('/api/v1.0/predict', methods=['GET'])
def predict():
    try:
        # Pobranie parametrów i obsługa braku lub pustych wartości
        num1 = safe_float(request.args.get("num1"))
        num2 = safe_float(request.args.get("num2"))

        prediction = 1 if (num1 + num2) > 5.8 else 0

        return jsonify({
            "prediction": prediction,
            "features": {
                "num1": num1,
                "num2": num2
            }
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")