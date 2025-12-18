# Python S3 File Upload

## 📌 Description
This project demonstrates how to upload files to **Amazon S3 using Python** and the **boto3 AWS SDK**.  
It is designed for beginners learning AWS, Cloud Engineering, or backend development.

---

## 🛠 Tech Stack
- Python 3.x
- Amazon S3
- AWS IAM
- boto3 (AWS SDK for Python)

---

## 🏗 Architecture
Python Script (Local / EC2) → Amazon S3

---

## ⚙ Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/python-s3-file-upload.git
cd python-s3-file-upload
```
---
### 2. Install dependencies
```bash
pip install boto3
```
---

## 🔐 AWS Configuration
### Option 1: Using AWS Access Key

### Configure credentials:
```bash
aws configure
```
### You will be asked to provide:

- AWS Access Key ID
- AWS Secret Access Key
- Default region (e.g. ap-southeast-1)

### Option 2: Using IAM Role (Recommended for EC2)
Attach an IAM Role with permissions:
- s3:PutObject
- s3:GetObject
