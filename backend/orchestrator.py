import os
import uuid
import boto3
from botocore.client import Config

# ===========================
# Wasabi / S3 configuration
# ===========================
WASABI_BUCKET = os.getenv("WASABI_BUCKET")
WASABI_ENDPOINT = "https://s3.ap-southeast-1.wasabisys.com"
ACCESS_KEY = os.getenv("WASABI_ACCESS_KEY")
SECRET_KEY = os.getenv("WASABI_SECRET_KEY")

# Initialize S3 client
s3_client = boto3.client(
    "s3",
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    endpoint_url=WASABI_ENDPOINT,
    config=Config(
        signature_version="s3v4",
        s3={
            "addressing_style": "path",
            "payload_signing_enabled": False
        }
    )
)

# ===========================
# Orchestrator function
# ===========================
def run_orchestrator():
    """
    Main orchestrator: simulate AI video creation, upload to Wasabi.
    Returns the uploaded file URL.
    """
    try:
        # ===========================
        # Simulate video creation
        # ===========================
        video_content = b"This is a dummy AI-generated video content."
        filename = f"runs/video_{uuid.uuid4().hex}.mp4"

        print(f"[Orchestrator] Created video: {filename}")

        # ===========================
        # Upload to Wasabi
        # ===========================
        print(f"[Orchestrator] Uploading to bucket: {WASABI_BUCKET}, key: {filename}")
        s3_client.put_object(
            Bucket=WASABI_BUCKET,
            Key=filename,
            Body=video_content,
            ContentType="video/mp4"
        )

        # Generate file URL
        file_url = f"{WASABI_ENDPOINT}/{WASABI_BUCKET}/{filename}"
        print(f"[Orchestrator] Uploaded successfully: {file_url}")

        return {
            "status": "ok",
            "file_url": file_url
        }

    except Exception as e:
        print(f"[Orchestrator] Error: {str(e)}")
        return {
            "status": "error",
            "error": str(e)
        }

