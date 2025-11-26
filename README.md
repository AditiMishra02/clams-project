# 🚀 CLAMS — Cloud Log Aggregation & Monitoring System  
![CI/CD Status](https://github.com/AditiMishra02/clams-project/actions/workflows/ci.yml/badge.svg)

A lightweight, production-ready **Cloud Log Ingestion & Monitoring System** designed to collect application logs and store them securely on **AWS S3**, built with:

- **Python + Flask** (Backend API)
- **Docker** (Containerization)
- **GitHub Actions** (CI/CD)
- **AWS S3** (Storage)
- **WSL2 + Ubuntu** (Local Dev Environment)

This project demonstrates **real DevOps, Cloud & Backend Engineering skills**, showing how a modern SaaS-style log ingestion pipeline works.

---

# 📌 Table of Contents
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

# 🚀 Project Overview

**CLAMS (Cloud Log Aggregation & Monitoring System)**  
is a powerful backend service that receives logs from any application and stores them securely in **Amazon S3**.

It mimics real-world log ingestion systems like:

- AWS CloudWatch Logs  
- Datadog Log Ingestion  
- Splunk HTTP Event Collector  
- ELK Stack Log API  

Perfect for showcasing **Cloud + DevOps + Backend Engineering** skills.

---

# 🖼 Architecture Diagram

```
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
             | log-storage-bucket |
             +---------+----------+
                       |
                       v
             Logs stored securely with
             timestamps & unique IDs
```

---

# 🛠 Tech Stack

### **Backend**
- Python 3.10  
- Flask  
- Boto3  

### **Cloud**
- AWS S3  
- IAM Access Keys  

### **DevOps**
- Docker  
- GitHub Actions  
- WSL2 Ubuntu  

---

# ⭐ Features

✔ Accept logs via `POST /upload-log`  
✔ Securely stores logs in AWS S3  
✔ Auto-generated timestamped log filenames  
✔ Works with curl, scripts, apps, or any system  
✔ Fully containerized  
✔ CI/CD via GitHub Actions  
✔ Log generator provided  

---

# 📁 Folder Structure
```
clams-project/
│
├── backend/
│   ├── app.py                 # Flask API backend
│   ├── log_generator.py       # Log simulation script
│   ├── requirements.txt       # Python dependencies
│   └── Dockerfile             # Backend Docker image
│
├── .github/workflows/
│   └── ci.yml                 # CI/CD pipeline
│
├── .gitignore
└── README.md
```

---

# 🧪 How to Run Locally

### **1️⃣ Activate your virtual environment**
```bash
source venv/bin/activate
```

### **2️⃣ Install dependencies**
```bash
pip install -r backend/requirements.txt
```

### **3️⃣ Run the Flask API**
```bash
cd backend
python3 app.py
```

The API runs at:  
👉 http://127.0.0.1:5000/

---

# 📡 API Documentation

## **POST /upload-log**

### **Option A — Raw Text Log**
```bash
curl -X POST -d "User login failed" http://127.0.0.1:5000/upload-log
```

### **Option B — JSON Log**
```bash
curl -X POST -H "Content-Type: application/json" \
     -d '{"log": "Payment failed"}' \
     http://127.0.0.1:5000/upload-log
```

### **Response Example**
```json
{
  "message": "Log uploaded successfully",
  "s3_path": "logs/log_2025-11-21T10-30-00.txt"
}
```

---

# 🐳 Docker Support

### **Build Docker image**
```bash
docker build -t clams-backend .
```

### **Run container**
```bash
docker run -p 5000:5000 clams-backend
```

### **Run with AWS credentials**
```bash
docker run -p 5000:5000 \
  -e AWS_ACCESS_KEY_ID=xxxx \
  -e AWS_SECRET_ACCESS_KEY=yyyy \
  -e AWS_DEFAULT_REGION=ap-south-1 \
  -e S3_BUCKET=clams-log-bucket \
  clams-backend
```

---

# 🔄 CI/CD Pipeline

This project uses GitHub Actions to:

- ✔ Build Docker image  
- ✔ Push to GitHub Container Registry  
- ✔ Run integration tests  
- ✔ Validate Python code  

### **CI Badge**
```
![CI/CD Status](https://github.com/AditiMishra02/clams-project/actions/workflows/ci.yml/badge.svg)
```

---

# 🔥 Log Generator

Simulate logs:

```bash
python3 log_generator.py
```

Example output:
```
Sent: User logged in | Status: 200
Sent: Payment failed | Status: 200
Sent: CPU usage exceeded threshold | Status: 200
```

Logs will appear automatically in your S3 bucket.

---

# 🚀 Deployment Options

- Deploy on **AWS EC2**  
- Deploy on **AWS Lambda + API Gateway**  
- Deploy using **Docker + ECS**  
- Deploy on **Render / Railway**  
- Deploy as **Kubernetes service**  

---

# 🖼 Screenshots (Add later)

📌 *You can add screenshots of:*  
- Terminal running API  
- S3 bucket showing logs  
- Docker container  
- GitHub Actions pipeline  

---

# 🔮 Future Enhancements

- Add authentication (API keys / JWT)  
- Add UI dashboard  
- Add log search and filtering  
- Push logs to CloudWatch or OpenSearch  
- Add rate limiting  
- Add structured logs (JSON schemas)  

---

# 👩‍💻 Author — Aditi Mishra

**Aspiring DevOps + Cloud + Backend Engineer**

**Skills:**  
AWS | Docker | CI/CD | Terraform | Python  

GitHub:  
👉 **https://github.com/AditiMishra02**

---


