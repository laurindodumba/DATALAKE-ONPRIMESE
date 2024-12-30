from flask import Flask, render_template
import pandas as pd
from minio_connection import get_minio_client
from io import BytesIO

app = Flask(__name__)

@app.route("/")
def index():
    client = get_minio_client()
    obj = client.get_object(Bucket="devlake", Key="gold/customer_feedback.csv")
    data = pd.read_csv(BytesIO(obj['Body'].read()))
    return render_template("index.html", data=data.to_html())

if __name__ == "__main__":
    app.run(debug=True)
