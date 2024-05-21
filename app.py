import requests
from flask import Flask, render_template, request,url_for
from flask import request as req


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def Index():
    return render_template("index.html")

@app.route('/summarization', methods=["GET", "POST"])
def summarization():
    if req.method == "POST":
        API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        headers = {"Authorization": "Bearer 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"}
        data = request.form["data"]
        minL = 30
        maxL = int(req.form["maxl"])

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()
    
        output = query({
            "inputs": data,
            "parameters": {
                "min_length": minL,
                "max_length": int(maxL)
            }
        })[0]
        return render_template("index.html", result=output["summary_text"])#summary text is the key 
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.debug = True
    app.run(port=8081)
