from flask import Flask, render_template
import boto3
import json
import os

app = Flask(__name__)

# Replace with your AWS credentials and region
AWS_ACCESS_KEY = 'Your_key'
AWS_SECRET_KEY = 'Your_key'
AWS_REGION = 'ap-south-1'
BUCKET_NAME = 'productdown'
FILE_NAME = 'productdown.json'  # Replace with your JSON file name

# Initialize S3 client
s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY,
                  aws_secret_access_key=AWS_SECRET_KEY,
                  region_name=AWS_REGION)

@app.route('/')
def index():
    try:
        # Fetch JSON file from S3 bucket
        obj = s3.get_object(Bucket=productdown, Key=productdown.json)
        data = obj['Body'].read().decode('utf-8')
        products = json.loads(data)

        return render_template('index.html', products=products)
    
    except Exception as e:
        return f'Failed to fetch data: {str(e)}'

if __name__ == '__main__':
    app.run(debug=True)
