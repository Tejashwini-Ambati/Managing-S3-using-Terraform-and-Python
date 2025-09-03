import boto3

s3 = boto3.client('s3')
bucket_name = 'devops-demo-bucket-12345'
file_path = './region.py'
key_name = 'uploads/region.py'

try:
    s3.upload_file(file_path, bucket_name, key_name)
    print(f"Uploaded {file_path} to s3://{bucket_name}/{key_name}")
except Exception as e:
    print("Upload failed:", e)
