provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "example" {
  bucket = "my-unique-s3-bucket-name-12345"
  acl    = "private"
}
