import json
import boto3
import base64

def lambda_handler(event, context):
    """A function to serialize target data from S3"""
    
    # Get the s3 address from the Step Function event input
    key = event["s3_key"]## TODO: fill in
    bucket = event["s3_bucket"]## TODO: fill in
    
    # Download the data from s3 to /tmp/image.png
    s3_client = boto3.client("s3")
    ## TODO: fill in
    local_file_path = '/tmp/image.png'  # Destination file path in /tmp directory
    s3_client.download_file(bucket, key, local_file_path)
    
    # We read the data from a file
    with open("/tmp/image.png", "rb") as f:
        image_data = base64.b64encode(f.read())

    # Pass the data back to the Step Function
    print("Event:", event.keys())
    return {
            "image_data": image_data,
            "s3_bucket": bucket,
            "s3_key": key,
            "inferences": []
        }
    
