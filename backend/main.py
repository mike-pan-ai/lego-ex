from flask import Flask, jsonify
import requests

app = Flask(__name__)


@app.route("/api/price/<set_id>")
def get_price(set_id):
    # Example using a placeholder LEGO API (replace with real API later)
    response = requests.get(f"https://api.bricklink.com/api/store/v1/items/{set_id}")

    # TODO: Replace with real API and add your key
    data = {"set_id": set_id, "price": None, "status": "placeholder"}

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
