import boto3
import os
import time

def run_orchestrator():
    print("AI Orchestrator running...")

    s3 = boto3.client(
        "s3",
        aws_access_key_id=os.getenv("WASABI_ACCESS_KEY"),
        aws_secret_access_key=os.getenv("WASABI_SECRET_KEY"),
        endpoint_url="https://s3.wasabisys.com"
    )

    s3.put_object(
        Bucket=os.getenv("WASABI_BUCKET"),
        Key="test.txt",
        Body=b"Hello from AI orchestrator!"
    )

    time.sleep(2)
    print("Upload complete")
