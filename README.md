# 🗳️ DevOps Voting App 2

A full stack voting application built as a hands-on DevOps learning project.
Built by Haneef Olajobi as part of a junior DevOps engineering roadmap.

> "Like sending someone a fully charged, ready-to-use device instead of instructions on how to build one." — Haneef on Docker 🐳

---

## 🧠 Project Overview

This project was built to get real, hands-on experience with core DevOps tools — not just watch tutorials.
The goal was to take an app from idea to a fully containerised, infrastructure-as-code project with a CI/CD pipeline.

The app lets users vote for their favourite DevOps tool:

- 🐍 Python
- 🌐 JavaScript
- 🏗️ Terraform
- 🐳 Docker

Votes are stored in an AWS S3 bucket (LocalStack for local development).

---

## 🏆 What This Project Covers

| DevOps Skill | How It's Used |
|---|---|
| Docker | App containerised and pushed to DockerHub |
| CI/CD (GitHub Actions) | Auto builds and pushes Docker image on every push |
| Terraform | Provisions S3 bucket as Infrastructure as Code |
| AWS S3 (LocalStack) | Stores votes as JSON |
| Python Flask | Backend web framework |
| Git & GitHub | Version control and pipeline trigger |

---

## 🧩 Architecture

```
Browser (port 5000)
        ↓
Flask Python Backend
        ↓
AWS S3 Bucket (LocalStack locally / real AWS in production)
        ↓
votes.json stored in bucket
```

### CI/CD Flow

```
Push code to GitHub
        ↓
GitHub Actions wakes up
        ↓
✅ Downloads code
✅ Logs into DockerHub
✅ Builds Docker image
✅ Pushes to DockerHub automatically
        ↓
Done in ~25 seconds ⚡
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python Flask | Backend web framework |
| HTML/CSS/JavaScript | Frontend UI |
| Docker | Containerisation |
| DockerHub | Container registry |
| LocalStack | Local AWS S3 emulation |
| Terraform | Infrastructure as Code |
| boto3 | AWS SDK for Python |
| GitHub Actions | CI/CD pipeline |
| Git | Version control |

---

## 📁 Project Structure

```
voting-app2/
├── .github/
│   └── workflows/
│       └── pipeline.yml    # CI/CD pipeline
├── files/
│   ├── app.py              # Flask backend
│   ├── index.html          # Frontend UI
│   ├── requirements.txt    # Python dependencies
│   ├── Dockerfile          # Container recipe
│   └── terraform/
│       └── main.tf         # Infrastructure as Code
└── README.md
```

---

## 🚀 How to Run Locally

### Prerequisites

- Docker installed
- Python 3.12+
- LocalStack
- Terraform

### Step 1 — Start LocalStack (fake AWS)

```bash
localstack start
```

### Step 2 — Provision infrastructure with Terraform

```bash
cd files/terraform
terraform init
terraform apply
```

Type `yes` when prompted. This creates the S3 bucket automatically.

### Step 3 — Run the app

```bash
cd ..
pip install flask flask-cors boto3
python app.py
```

Visit `http://localhost:5000` in your browser and start voting! 🗳️

---

## 🐳 Docker

### Build the image

```bash
docker build -t voting-app2 .
```

### Run the container

```bash
docker run -d -p 5000:5000 --name voting-containers voting-app2
```

### Pull from DockerHub (run anywhere!)

```bash
docker run -p 5000:5000 olajobihaneef/voting-app2
```

### Useful Docker commands

```bash
docker ps                       # see running containers
docker stop voting-containers   # stop the container
docker start voting-containers  # start it again
docker logs voting-containers   # see app logs
docker rm voting-containers     # delete the container
docker images                   # see all images
```

---

## 🏗️ Terraform

### What it does

Instead of manually creating the S3 bucket by clicking in the AWS console, Terraform creates it automatically from code.

### The three commands

```bash
terraform init     # download AWS provider plugin
terraform plan     # preview what will be created
terraform apply    # actually create the infrastructure
terraform destroy  # delete everything
```

---

## 🔄 CI/CD Pipeline

Every push to `main` triggers the pipeline automatically:

1. GitHub Actions spins up a fresh Ubuntu machine
2. Checks out the code
3. Logs into DockerHub using stored secrets
4. Builds the Docker image
5. Pushes it to DockerHub

### Secrets required

Add these in GitHub → Repo → Settings → Secrets and variables → Actions:

- `DOCKER_USERNAME` → your DockerHub username
- `DOCKER_TOKEN` → your DockerHub access token (Read/Write/Delete)

---

## 📊 How Votes Are Stored

Votes are stored as a JSON file in the S3 bucket:

```json
{
  "Python": 45,
  "JavaScript": 16,
  "Terraform": 33,
  "Docker": 29
}
```

Check current votes anytime:

```bash
awslocal s3 cp s3://voting-app2/votes.json -
```

---

## 🐳 DockerHub

Image available at: `olajobihaneef/voting-app2`

```bash
docker run -p 5000:5000 olajobihaneef/voting-app2
```

---

## 👨‍💻 Author

**Haneef Olajobi** — Junior DevOps Engineer

- GitHub: [haneeo3](https://github.com/haneeo3)
- DockerHub: [olajobihaneef](https://hub.docker.com/u/olajobihaneef)
- Project: Part of a hands-on DevOps learning roadmap covering Linux, Docker, Terraform, CI/CD and AWS
