from dotenv import load_dotenv
load_dotenv()  # <--- WAJIB

import boto3, os

print("KEY:", os.getenv("R2_ACCESS_KEY_ID"))
print("SECRET:", os.getenv("R2_SECRET_ACCESS_KEY"))
print("ENDPOINT:", os.getenv("R2_ENDPOINT"))
print("R2_BUCKET_PUBLIC_URL:", os.getenv("R2_BUCKET_PUBLIC_URL"))


s3 = boto3.client(
    "s3",
    endpoint_url=os.getenv("R2_ENDPOINT"),
    aws_access_key_id=os.getenv("R2_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("R2_SECRET_ACCESS_KEY"),
    region_name="auto",
)

bucket = os.getenv("R2_BUCKET_NAME")

# Test upload
s3.put_object(
    Bucket=bucket,
    Key="test-upload.txt",
    Body=b"hello from python",
)

print("Upload success!")

# Test download
obj = s3.get_object(Bucket=bucket, Key="test-upload.txt")
print("Downloaded:", obj["Body"].read())