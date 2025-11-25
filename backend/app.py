from flask import Flask, request, jsonify
import boto3
import os
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Initialize S3 client
s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("access_key"),
    aws_secret_access_key=os.getenv("access_key")
)

BUCKET = os.getenv("S3_BUCKET")


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "CLAMS API is running"})


# ============================
# FIXED /upload-log ENDPOINT
# ============================
@app.route("/upload-log", methods=["POST"])
def upload_log():

    # Accept raw request body OR form data
    raw_body = request.data
    form_body = request.form.get("log")

    # Decide which one to use
    if raw_body:
        try:
            log_message = raw_body.decode("utf-8")
        except:
            log_message = str(raw_body)
    elif form_body:
        log_message = form_body
    else:
        return jsonify({"error": "No log data received"}), 400

    # Generate filename for S3
    filename = f"log_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.txt"

    # Upload log to S3
    s3.put_object(
        Bucket=BUCKET,
        Key=filename,
        Body=log_message
    )

    return jsonify({"message": "Log uploaded successfully"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


