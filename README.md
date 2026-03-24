# 🚀 CI/CD Flask App with Docker & AWS EC2

This project demonstrates a complete **CI/CD pipeline** using modern DevOps tools to automatically deploy a Flask web application to a cloud server.

---

## 🧱 Tech Stack

- Python (Flask)
- Docker
- GitHub Actions
- AWS EC2
- SSH

---

## ⚙️ Project Overview

This project automates the process of:

- Writing and updating application code  
- Pushing changes to GitHub  
- Automatically building and deploying the application to an EC2 server  
- Running the app inside a Docker container  

---

## 🔄 CI/CD Workflow

    Developer → GitHub → GitHub Actions → SSH → AWS EC2 → Docker → Live App

---

## 🌐 Application Features

- Displays dynamic content using Flask  
- Shows version (via environment variables)  
- Displays build timestamp  
- Fully containerized  

---

## 🐳 Docker Usage

### Build Image

    docker build -t cicd-app .

### Run Container

    docker run -d -p 80:5000 --name myapp cicd-app

---

## ☁️ Deployment (AWS EC2)

- Hosted on an Ubuntu EC2 instance  
- Application runs inside a Docker container  
- Accessible via public IP address  

---

## 🔐 Environment Variables

- `APP_VERSION` → dynamically passed to the app  
- Used to track different builds  

---

## 📂 Project Structure

    cicd-app/
    ├── app.py
    ├── Dockerfile
    ├── requirements.txt
    ├── templates/
    │   └── index.html
    └── .github/
        └── workflows/
            └── deploy.yml

---

## 📌 What I Learned

- CI/CD pipeline setup  
- Docker containerization  
- AWS EC2 deployment  
- SSH-based automation  
- Git & GitHub workflows  
- Debugging real-world deployment issues  

---

## 🧠 Key Skills Demonstrated

- DevOps fundamentals  
- Cloud deployment  
- Automation  
- Linux server management  
- Version control & CI/CD  

---

## 📷 How to Verify

1. Open the app using the EC2 public IP  
2. Push a change to GitHub  
3. GitHub Actions will automatically deploy  
4. Refresh the page to see updates  

---

## 🎯 Purpose

This project was built to gain hands-on experience with **real-world DevOps workflows** and end-to-end application deployment.
