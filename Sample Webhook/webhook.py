from flask import Flask, request, jsonify

app = Flask(__name__)

# optional auth token (match your Flutter authToken)
AUTH_TOKEN = "1"

@app.route("/webhook", methods=["POST"])
def webhook():
    # ─────────────────────────────
    # AUTH CHECK
    # ─────────────────────────────
    auth_header = request.headers.get("Authorization", "")

    if AUTH_TOKEN:
        if auth_header != f"Bearer {AUTH_TOKEN}":
            return jsonify({"error": "Unauthorized"}), 401

    # ─────────────────────────────
    # JSON BODY
    # ─────────────────────────────
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    # ─────────────────────────────
    # YOUR TRANSACTION DATA
    # ─────────────────────────────
    print("\n🔥 NEW WEBHOOK RECEIVED")
    print(f"ID: {data.get('id')}")
    print(f"Amount: {data.get('amount')}")
    print(f"Sender: {data.get('senderName')}")
    print(f"Phone: {data.get('phoneNumber')}")
    print(f"Timestamp: {data.get('timestamp')}")

    # ─────────────────────────────
    # SUCCESS RESPONSE
    # ─────────────────────────────
    return jsonify({
        "status": "ok",
        "message": "Transaction received"
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)