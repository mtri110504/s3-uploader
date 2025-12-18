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
