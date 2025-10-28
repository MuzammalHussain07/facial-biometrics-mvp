from flask import Flask

app = Flask(__name__)

@app.route("/verify", methods=["POST"])
def verify():
    return {"result": "Demo verification success"}

@app.route("/health")
def health():
    return {"status": "OK", "service": "Local Agent"}

if __name__ == "__main__":
    app.run(port=5000)
