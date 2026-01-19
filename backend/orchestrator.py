import os
import boto3
import time

def run_orchestrator():
    try:
        s3 = boto3.client(
            "s3",
            endpoint_url="https://s3.wasabisys.com",
            aws_access_key_id=os.getenv("WASABI_ACCESS_KEY"),
            aws_secret_access_key=os.getenv("WASABI_SECRET_KEY"),
            region_name=os.getenv("WASABI_REGION")
        )

        bucket = os.getenv("WASABI_BUCKET")
        if not bucket:
            raise ValueError("WASABI_BUCKET env var not set")
filename = f"runs/run-{int(time.time())}.txt"  # "runs/" is the folder prefix
      print(f"Uploading to bucket: {bucket}, key: {filename}")

s3.put_object(Bucket=os.getenv("WASABI_BUCKET"), Key=filename, Body=b"AI Orchestrator ran successfully.")


        print(f"Upload successful: {filename}")
        return {"status": "uploaded", "file": filename}

    except Exception as e:
        print("Error uploading to Wasabi:", e)
        return {"status": "error", "error": str(e)}

    except Exception as e:
        print("Error uploading to Wasabi:", e)
       
