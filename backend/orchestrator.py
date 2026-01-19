import os
import boto3
from botocore.client import Config

def run_orchestrator():
    try:
        s3 = boto3.client(
            "s3",
            aws_access_key_id=os.getenv("WASABI_ACCESS_KEY"),
            aws_secret_access_key=os.getenv("WASABI_SECRET_KEY"),
            endpoint_url="https://s3.ap-southeast-1.wasabisys.com",
            config=Config(
                signature_version="s3v4",
                s3={
                    "addressing_style": "path",
                    "payload_signing_enabled": False
                }
            )
        )

        response = s3.list_buckets()
        bucket_names = [b["Name"] for b in response["Buckets"]]

        return {
            "status": "ok",
            "buckets": bucket_names
        }

    except Exception as e:
        return {
            "status": "error",
            "error": str(e)
        }

