
def run_orchestrator():
    import os
    import time
    import boto3
    from botocore.client import Config

    print("Orchestrator started")
    print("Wasabi access key prefix:", os.getenv("WASABI_ACCESS_KEY")[:4])

    s3 = boto3.client(
        "s3",
        endpoint_url="https://s3.ap-southeast-1.wasabisys.com",
        aws_access_key_id=os.getenv("WASABI_ACCESS_KEY"),
        aws_secret_access_key=os.getenv("WASABI_SECRET_KEY"),
        region_name="ap-southeast-1",
        config=Config(
    signature_version="s3v4",
    s3={"addressing_style": "path"}
)

    )

    bucket = os.getenv("WASABI_BUCKET")
    filename = f"runs/test-{int(time.time())}.txt"
    content = b"Wasabi upload test"

    try:
        s3.put_object(
            Bucket=bucket,
            Key=filename,
            Body=content
        )
        print("Upload successful:", filename)
        return {"status": "ok", "file": filename}

    except Exception as e:
        print("Wasabi upload failed:", str(e))
        return {"status": "error", "error": str(e)}

     

 
