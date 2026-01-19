def run_orchestrator():
    import os
    import boto3
    from botocore.client import Config

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

    try:
        buckets = s3.list_buckets()
        return {
            "status": "ok",
            "buckets": [b["Name"] for b in buckets["Buckets"]]
        }
    except Exception as e:
        return {"status": "error", "error": str(e)}


