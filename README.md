# Upload Files to Amazon S3 Using Python

📘 **Mini Project Guide: Upload Files to Amazon S3 Using Python**

---

## 🎯 Objectives
- Build a Python program to upload any type of file (images, PDFs, etc.) to Amazon S3
- Automatically organize uploaded files by date (YYYY/MM/DD)
- Generate temporary download links using Presigned URLs

---

## 🛠 Tech Stack
- Python 3.x
- Amazon S3
- AWS IAM
- boto3 (AWS SDK for Python)
- AWS CLI

---

## 🟦 PART 1 — Project Setup

### 1. Create Project Directory
```bash
mkdir s3-uploader
cd s3-uploader
```

---

### 2. Create and Activate Python Virtual Environment
Create virtual environment
```bash
python3 -m venv venv
```
Why use a virtual environment?
- Isolates project dependencies
- Prevents conflicts with system Python packages
- Easy to remove when no longer needed

Activate virtual environment
```bash
source venv/bin/activate
```
When you see (venv) in the terminal, the environment is active.

---

### 3. Install boto3 (AWS SDK for Python)
```bash
pip install boto3
```

---

### 4. Install AWS CLI (if not installed)
```bash
brew install awscli
```

---

### 5. Configure AWS CLI
```bash
aws configure
```

Provide the following information:
- AWS Access Key ID
- AWS Secret Access Key
- Default region (e.g. ap-southeast-1)
- Output format: json

---

## 🟦 PART 2 — Create Amazon S3 Bucket

### Bucket name:
```text
tri-upload-demo
```

Recommended bucket configuration:

- Public access: ❌ Disabled
- Block all public access: ✅ Enabled
- File access via Presigned URLs (more secure than public access)

---

## 🟦 PART 3 — Python Upload Script

### Create the file upload3.py:
```python
import boto3
import os
from datetime import datetime

s3 = boto3.client("s3")
BUCKET_NAME = "tri-upload-demo"

def upload_file(file_path):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    today = datetime.now().strftime("%Y/%m/%d")
    file_name = os.path.basename(file_path)
    s3_key = f"{today}/{file_name}"

    s3.upload_file(file_path, BUCKET_NAME, s3_key)

    url = s3.generate_presigned_url(
        "get_object",
        Params={"Bucket": BUCKET_NAME, "Key": s3_key},
        ExpiresIn=3600
    )

    print("✅ Upload successful!")
    print("📂 S3 Object Key:", s3_key)
    print("🔗 Download link (expires in 1 hour):")
    print(url)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python upload3.py <path-to-file>")
    else:
        upload_file(sys.argv[1])
```

---

## 🟦 PART 4 — Run the Upload Script

### Upload a file example
```bash
python upload3.py ~/Downloads/Gemini.png
```

### Output includes:

- S3 object key
- Temporary download link (Presigned URL)

---

## 📂 Project Structure
```
s3-uploader/
├── upload3.py
├── venv/
└── README.md
```

---

## 🎯 What You Will Learn
- How Amazon S3 works
- Uploading files to S3 using boto3
- Managing AWS credentials securely
- Generating Presigned URLs for private objects
- Organizing cloud storage by date

---

## 🚀 Possible Enhancements
- Upload multiple files at once
- Validate file size and file type
- Upload via API Gateway + AWS Lambda
- Build a web interface for file uploads
- Enable S3 encryption (SSE-S3 or SSE-KMS)

---

## 👤 Author
Tri Bui
Cloud / Backend Learner
