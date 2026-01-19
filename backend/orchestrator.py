import os
import boto3
import time
print("Wasabi access key prefix:", os.getenv("WASABI_ACCESS_KEY")[:4])

def run_orchestrator():
    try:
        bucket = os.getenv("WASABI_BUCKET")
        access_key = os.getenv("WASABI_ACCESS_KEY")
        secret_key = os.getenv("WASABI_SECRET_KEY")
        region = os.getenv("WASABI_REGION")

        if not bucket or not access_key or not secret_key or not region:
            raise ValueError("One or more Wasabi env vars are not set")

        # Initialize Wasabi S3 client
        s3 = boto3.client(
            "s3",
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            endpoint_url=f"https://s3.{region}.wasabisys.com",
            region_name=region,
            config=boto3.session.Config(signature_version='s3v4')  # Ensure v4 signing
        )

        # Create a unique file in 'runs/' folder
        filename = f"runs/run-{int(time.time())}.txt"
        print(f"Uploading to bucket: {bucket}, key: {filename}")

        s3.put_object(
            Bucket=bucket,
            Key=filename,
            Body=b"AI Orchestrator ran successfully."
        )
        print(f"Upload successful: {filename}")

        return {"status": "uploaded", "file": filename}

    except Exception as e:
        print("Error uploading to Wasabi:", e)
        return {"status": "error", "error": str(e)}

 
