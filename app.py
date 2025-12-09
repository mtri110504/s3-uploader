import boto3
import sys
from datetime import datetime
import os

# Tên bucket của bạn
BUCKET_NAME = "tri-upload-demo"

def upload_file(file_path):
    s3 = boto3.client("s3")

    if not os.path.isfile(file_path):
        print("File không tồn tại:", file_path)
        return

    file_name = os.path.basename(file_path)

    # folder theo ngày: 2025/12/09/
    today = datetime.now().strftime("%Y/%m/%d")
    s3_key = f"{today}/{file_name}"

    try:
        # Upload file
        s3.upload_file(file_path, BUCKET_NAME, s3_key)
        print("Upload thành công!")
        print("Đường dẫn S3:", s3_key)

        # Tạo link tải (Presigned URL)
        url = s3.generate_presigned_url(
            "get_object",
            Params={"Bucket": BUCKET_NAME, "Key": s3_key},
            ExpiresIn=3600  # 1 giờ
        )

        print("Link tải (tồn tại 1 giờ):")
        print(url)

    except Exception as e:
        print("Lỗi:", e)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Cách dùng: python upload.py <đường_dẫn_file>")
    else:
        upload_file(sys.argv[1])
