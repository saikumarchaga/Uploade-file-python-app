from flask import Flask, request, render_template
import boto3
import os

app = Flask(__name__)

# Configure S3 bucket details
S3_BUCKET = "your-s3-bucket-name"
S3_REGION = "your-region"

# AWS Client
s3 = boto3.client("s3", region_name=S3_REGION)

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files["file"]
        if file:
            s3.upload_fileobj(file, S3_BUCKET, file.filename)
            return f"File {file.filename} uploaded successfully to S3 bucket {S3_BUCKET}!"
    return render_template("upload.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

