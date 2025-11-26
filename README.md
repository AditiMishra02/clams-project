# 🚀 CLAMS — Cloud Log Aggregation & Monitoring System  
![CI/CD Status](https://github.com/AditiMishra02/clams-project/actions/workflows/ci.yml/badge.svg)

A lightweight, production-ready **Cloud Log Ingestion & Monitoring System** designed to collect application logs and store them securely on **AWS S3**, built with:

- **Python + Flask** (Backend API)
- **Docker** (Containerization)
- **GitHub Actions** (CI/CD)
- **AWS S3** (Storage)
- **WSL2 + Ubuntu** (Local Dev Environment)

This project demonstrates **real DevOps, Cloud & Backend Engineering skills**, showing how a modern SaaS-style log collection pipeline works.

---

# 📌 **Table of Contents**

1. [Project Overview](#-project-overview)  
2. [Architecture Diagram](#-architecture-diagram)  
3. [Tech Stack](#-tech-stack)  
4. [Features](#-features)  
5. [Folder Structure](#-folder-structure)  
6. [How to Run Locally](#-how-to-run-locally)  
7. [API Documentation](#-api-documentation)  
8. [Docker Support](#-docker-support)  
9. [CI/CD Pipeline](#-cicd-pipeline)  
10. [Log Generator](#-log-generator)  
11. [Deployment Options](#-deployment-options)  
12. [Screenshots](#-screenshots)  
13. [Future Enhancements](#-future-enhancements)  
14. [Author](#-author)

---

# 🚀 **Project Overview**

**CLAMS (Cloud Log Aggregation & Monitoring System)**  
is a simple but powerful backend service that receives logs from applications and stores them securely in **Amazon S3**.

It simulates real-world systems like:

- AWS CloudWatch Logs  
- Datadog Log Ingestion  
- ELK Stack Ingestion APIs  
- Splunk HTTP Event Collector  

This makes it an impressive DevOps + Cloud + Backend project for your resume.

---

# 🖼 **Architecture Diagram**

# 🚀 CLAMS — Cloud Log Aggregation & Monitoring System  
![CI/CD Status](https://github.com/AditiMishra02/clams-project/actions/workflows/ci.yml/badge.svg)

A lightweight, production-ready **Cloud Log Ingestion & Monitoring System** designed to collect application logs and store them securely on **AWS S3**, built with:

- **Python + Flask** (Backend API)
- **Docker** (Containerization)
- **GitHub Actions** (CI/CD)
- **AWS S3** (Storage)
- **WSL2 + Ubuntu** (Local Dev Environment)

This project demonstrates **real DevOps, Cloud & Backend Engineering skills**, showing how a modern SaaS-style log collection pipeline works.

---

# 📌 **Table of Contents**

1. [Project Overview](#-project-overview)  
2. [Architecture Diagram](#-architecture-diagram)  
3. [Tech Stack](#-tech-stack)  
4. [Features](#-features)  
5. [Folder Structure](#-folder-structure)  
6. [How to Run Locally](#-how-to-run-locally)  
7. [API Documentation](#-api-documentation)  
8. [Docker Support](#-docker-support)  
9. [CI/CD Pipeline](#-cicd-pipeline)  
10. [Log Generator](#-log-generator)  
11. [Deployment Options](#-deployment-options)  
12. [Screenshots](#-screenshots)  
13. [Future Enhancements](#-future-enhancements)  
14. [Author](#-author)

---

# 🚀 **Project Overview**

**CLAMS (Cloud Log Aggregation & Monitoring System)**  
is a simple but powerful backend service that receives logs from applications and stores them securely in **Amazon S3**.

It simulates real-world systems like:

- AWS CloudWatch Logs  
- Datadog Log Ingestion  
- ELK Stack Ingestion APIs  
- Splunk HTTP Event Collector  

This makes it an impressive DevOps + Cloud + Backend project for your resume.

---

# 🖼 **Architecture Diagram**


            +----------------------+
            |   Frontend / Apps    |
            |  (Send Logs via API) |
            +----------+-----------+
                       |
                       | HTTP POST /upload-log
                       v
             +---------+----------+
             |   Flask API (WSL)  |
             |  /upload-log route |
             +---------+----------+
                       |
                       | boto3
                       v
             +---------+----------+
             |       AWS S3       |
             |  log-storage-bucket|
             +---------+----------+
                       |
                       v
            Logs stored securely with
            timestamps & unique IDs

---

# 🛠 **Tech Stack**

### **Backend**
- Python 3.10  
- Flask  
- Boto3 (AWS SDK)

### **Cloud**
- AWS S3  
- IAM Access Keys  
- Free Tier compliant

### **DevOps**
- Docker (Containerization)  
- GitHub Actions (CI/CD)  
- WSL2 Ubuntu (Local Development)

---

# ⭐ **Features**

✔ Accepts logs from any app via `POST /upload-log`  
✔ Stores logs in AWS S3 with unique timestamp file names  
✔ Fully containerized with Docker  
✔ GitHub Actions CI/CD pipeline  
✔ Secure environment variable handling (no AWS keys in repo)  
✔ Log generator for demonstration  
✔ Works on free AWS tier  

---

# 📁 **Folder Structure**

clams-project/
│
├── backend/
│ ├── app.py # Flask API (main backend)
│ ├── log_generator.py # Simulates real logs
│ ├── requirements.txt # Python dependencies
│ └── Dockerfile # Backend Docker image
│
├── .github/workflows/
│ └── ci.yml # CI/CD pipeline
│
├── .gitignore
└── README.md


---

# 🧪 **How to Run Locally**

### **1️⃣ Activate your virtual environment**

```bash
source venv/bin/activate
2️⃣ Install dependencies
pip install -r backend/requirements.txt

3️⃣ Run the Flask API
cd backend
python3 app.py


Runs at:

http://127.0.0.1:5000/

📡 API Documentation
POST /upload-log
Request

Option A — Raw Text Log

curl -X POST -d "User login failed" http://127.0.0.1:5000/upload-log


Option B — JSON Log

curl -X POST -H "Content-Type: application/json" \
     -d '{"log": "Payment failed"}' \
     http://127.0.0.1:5000/upload-log

Response
{
  "message": "Log uploaded successfully",
  "s3_path": "logs/log_2025-11-21T10-30-00.txt"
}

🐳 Docker Support
Build the Docker image
docker build -t clams-backend .

Run the container
docker run -p 5000:5000 clams-backend

Run with AWS credentials
docker run -p 5000:5000 \
  -e AWS_ACCESS_KEY_ID=xxxx \
  -e AWS_SECRET_ACCESS_KEY=yyyy \
  -e AWS_DEFAULT_REGION=ap-south-1 \
  -e S3_BUCKET=clams-log-bucket \
  clams-backend

🔄 CI/CD Pipeline

This project uses GitHub Actions to:

✔ Build Docker image
✔ Push image to GitHub Container Registry
✔ Run integration tests
✔ Validate code

CI badge:

🔥 Log Generator

Simulate real-time logs:

python3 log_generator.py


You will see:

Sent: User logged in | Status: 200
Sent: Payment failed | Status: 200
Sent: CPU usage exceeded threshold | Status: 200


logs will appear inside AWS S3 automatically.


👩‍💻 Author
Aditi Mishra

Aspiring DevOps + Cloud + Backend Engineer

AWS | Docker | CI/CD | Terraform | Python

GitHub: @AditiMishra02
