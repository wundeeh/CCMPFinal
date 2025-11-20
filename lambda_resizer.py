import boto3
from PIL import Image
import io
import os

s3 = boto3.client('s3')
OUTPUT_BUCKET = os.environ["OUTPUT_BUCKET"]

def lambda_handler(event, context):
    try:
        input_item = event.get('Payload', event)
        bucket = input_item["bucket"]
        key = event["key"]

        # Download image
        obj = s3.get_object(Bucket=bucket, Key=key)
        img = Image.open(io.BytesIO(obj["Body"].read()))
        img.thumbnail((200, 200))

        # Convert to JPEG in memory
        buffer = io.BytesIO()
        img.save(buffer, "JPEG")
        buffer.seek(0)

        output_key = f"thumbnail-{os.path.basename(key)}"

        # Upload resized image
        s3.put_object(
            Bucket=OUTPUT_BUCKET,
            Key=output_key,
            Body=buffer,
            ContentType="image/jpeg"
        )

        return {
            "status": "SUCCESS",
            "thumbnailKey": output_key
        }

    except Exception as e:
        return {
            "status": "FAILURE",
            "errorMessage": str(e)
        }
