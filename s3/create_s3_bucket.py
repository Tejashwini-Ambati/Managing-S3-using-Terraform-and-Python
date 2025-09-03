import boto3

s3 = boto3.client('s3')
bucket_name = 'devops-demo-bucket-12345'

s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'}
)

print(f"Bucket {bucket_name} created.")
