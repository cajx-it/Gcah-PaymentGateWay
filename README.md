# 💳 GCash Payment Gateway Listener

> An Android APK (built with Flutter) that listens for incoming GCash payment notifications and instantly forwards the payment data to your server endpoint — giving you complete control over how payments are handled in your system.

![Flutter](https://img.shields.io/badge/Flutter-02569B?style=for-the-badge&logo=flutter&logoColor=white)
![GCash](https://img.shields.io/badge/GCash-0070BA?style=for-the-badge&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

---

## 🚀 What is this?

**GCash Payment Gateway Listener** is an Android app (APK) built with Flutter. Install it on any Android device, point it to your server, and it will listen for incoming GCash payments in real time. The moment a payment is received, the app captures the sender's details and forwards them straight to your backend — where you decide what happens next.

No complex API integrations. No approval process. Just install, configure, and go.

---

## ✨ Features

- 📱 **Android APK — no build required** — just download, install, and run
- 🔔 **Real-time payment listener** — captures GCash payment notifications the moment they arrive
- 📦 **Full payload forwarding** — sends transaction ID, amount, sender name, phone number, and timestamp to your server
- 🔧 **Server-agnostic** — works with any backend (PHP, Node.js, Python, Java, etc.)
- 🧩 **Developer-first design** — you decide what to do with the payment data on your end
- 📋 **Sample webhook included** — get started immediately with the provided Python server example

---

## 🏗️ How it works

```
Customer pays via GCash Cashier
            │
            ▼
 GCash sends payment notification
            │
            ▼
  Flutter Listener App receives it
            │
            ▼
  Full payment data forwarded to
      your server endpoint
            │
            ▼
  Your server does whatever it needs:
  ✅ Update order status
  ✅ Send confirmation email
  ✅ Trigger fulfillment
  ✅ Log to database
  ✅ Anything you want
```

---

## 📁 Project Structure

```
Gcah-PaymentGateWay/
├── App/                  # Pre-built Android APK — ready to install
└── Sample Webhook/       # Sample server-side webhook handler (Python)
```

---

## ⚙️ Getting Started

### Prerequisites

- An Android device or emulator
- A running backend server with a publicly accessible URL (or use [ngrok](https://ngrok.com) for local testing)
- A GCash account that will receive payments

### 1. Download and install the APK

Download the latest APK from the [`App/`](https://github.com/cajx-it/Gcah-PaymentGateWay/tree/main/App) folder in this repository.

> ⚠️ You may need to enable **"Install from unknown sources"** on your Android device:
> Settings → Security → Enable "Unknown sources" or "Install unknown apps"
> Then grant the Notification Access


Install the APK on your Android device by opening the downloaded file.

### 2. Configure your server endpoint

Once the app is installed, enter your server's webhook URL inside the app. This is the endpoint where all GCash payment notifications will be forwarded.

If you're testing locally, use ngrok to expose your local server:

```bash
ngrok http 5000
```

Then paste the generated `https://` URL into the app as your endpoint.

### 3. Set up the sample webhook server

Navigate to the `Sample Webhook` folder and run the provided Python server to see a working example of how to receive and handle payment data.

```bash
cd "Sample Webhook"
pip install flask
python webhook.py
```

### 4. Test it

Send a GCash payment to the registered account. Your server should immediately receive the payment notification with the sender's details.

---

## 💼 How this helps your business

### Accept GCash payments without a full merchant integration
Getting access to GCash's official partner API requires approval, NDA signing, and a lengthy onboarding process. This tool lets you start accepting and tracking GCash payments immediately while you work through that process — or as a permanent lightweight solution.

### Full visibility into every transaction
Because the complete payment payload is forwarded to your server, you have full access to every field GCash sends — transaction IDs, amounts, timestamps, merchant codes, QR data, and more. No data is hidden or abstracted away.

### Plug into any existing system
Whether you run a POS system, an e-commerce store, a school enrollment portal, or a custom business app — this listener plugs in as a sidecar. Your existing system just needs to expose an endpoint to receive the payment data.

### Automate your payment workflows
Once payment data hits your server, you can automate anything: send SMS/email confirmations, update inventory, mark orders as paid, generate receipts, push to accounting software, or trigger any downstream process your business needs.

### No vendor lock-in
Your business logic lives entirely on your server. If you ever switch payment providers, only the listener changes — your backend workflows stay intact.

---

## 📦 Payment Data You Receive

When a GCash payment is made, your server endpoint receives a JSON payload with the following fields:

| Field | Description |
|---|---|
| `id` | Unique transaction ID of the payment |
| `amount` | The payment amount sent by the customer |
| `senderName` | Full name of the GCash account that sent the payment |
| `phoneNumber` | GCash-registered phone number of the sender |
| `timestamp` | Date and time when the payment was made |

### Example — how your server sees it (Python)

```python
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json

    print("\n🔥 NEW WEBHOOK RECEIVED")
    print(f"ID:        {data.get('id')}")
    print(f"Amount:    {data.get('amount')}")
    print(f"Sender:    {data.get('senderName')}")
    print(f"Phone:     {data.get('phoneNumber')}")
    print(f"Timestamp: {data.get('timestamp')}")

    # Your business logic here
    return jsonify({"status": "received"}), 200
```

---

## 🔐 Security Notes

- Always **validate incoming webhook requests** on your server — check that the payload contains expected fields before processing.
- Use **HTTPS** for your server endpoint — never accept payment data over plain HTTP in production.
- **Never expose your webhook URL publicly** without some form of authentication token or secret to prevent spoofed requests.

---

## 🛠️ Use Case Examples

- **WiFi Hotspot Monetization** — charge customers via GCash before granting internet access
- **Small Business POS** — accept GCash payments at physical stores with automatic order confirmation
- **Online Stores** — integrate GCash as a payment option with real-time order fulfillment
- **School / Event Registration** — automate enrollment confirmation upon successful payment
- **Freelancer Invoicing** — get notified instantly when a client pays

---


## ⚠️ Disclaimer

This project is an independent developer tool and is **not officially affiliated with, endorsed by, or partnered with GCash or Mynt**. Use it responsibly and in compliance with GCash's terms of service and applicable laws.

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

<p align="center">Built with 💙 by <a href="https://github.com/cajx-it">cajx-it</a></p>
