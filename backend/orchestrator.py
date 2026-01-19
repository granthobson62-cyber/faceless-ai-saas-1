import os
import boto3
import time

def run_orchestrator():
    try:
        # Initialize Wasabi S3 client with correct Singapore region endpoint
        s3 = boto3.client(
            "s3",
            endpoint_url="https://s3.ap-southeast-1.wasabisys.com",
            aws_access_key_id=os.getenv("WASABI_ACCESS_KEY"),
            aws_secret_access_key=os.getenv("WASABI_SECRET_KEY"),
            region_name=os.getenv("WASABI_REGION")  # Must match ap-southeast-1
        )

        # Get bucket from environment
        bucket = os.getenv("WASABI_BUCKET")
        if not bucket:
            raise ValueError("WASABI_BUCKET env var not set")

        # Create a unique filename in 'runs/' folder
        filename = f"runs/run-{int(time.time())}.txt"

        # DEBUG print: shows what will be uploaded
        print(f"Uploading to bucket: {bucket}, key: {filename}")

        # Upload a simple text file to Wasabi
        s3.put_object(
            Bucket=bucket,
            Key=filename,
            Body=b"AI Orchestrator ran successfully."
        )

        # Confirm success
        print(f"Upload successful: {filename}")
        return {"status": "uploaded", "file": filename}

    except Exception as e:
        print("Error uploading to Wasabi:", e)
        return {"status": "error", "error": str(e)}

    

