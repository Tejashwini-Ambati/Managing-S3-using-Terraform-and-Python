import boto3

s3 = boto3.client('s3')
bucket_name = 'devops-demo-bucket-12345'
key_name = 'uploads/region.py'
download_path = './region.py'


try:
    s3.download_file(bucket_name, key_name, download_path)
    print(f"Downloaded to {download_path}")
except Exception as e:
    print("Download failed:", e)
