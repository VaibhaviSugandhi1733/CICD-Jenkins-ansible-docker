
# 🚀 CI/CD Pipeline with Jenkins + Docker + Ansible on AWS EC2

This project implements a fully automated **CI/CD pipeline** that:
- Pulls the latest source code from GitHub
- Builds and pushes a Docker image to Docker Hub
- Generates an `inventory.ini` dynamically with the EC2 IP
- Runs an Ansible playbook to deploy the Docker container to the remote EC2 instance

---

## 📦 Tech Stack

- **CI Tool**: Jenkins
- **Containerization**: Docker
- **Configuration Management**: Ansible
- **Cloud Provider**: AWS EC2 (Ubuntu)
- **Version Control**: Git & GitHub
- **Image Hosting**: Docker Hub

---

## 🌐 Pipeline Overview

```mermaid
graph TD
    A[GitHub Push] --> B[Jenkins Build Trigger]
    B --> C[Docker Build]
    C --> D[Docker Push to Docker Hub]
    D --> E[Generate Dynamic Ansible Inventory]
    E --> F[Ansible Playbook Execution]
    F --> G[App Deployed on EC2]
````

---

## 🧱 Project Structure

```
.
├── Dockerfile
├── Jenkinsfile
├── app.py                 # Flask app
├── requirements.txt
├── ansible/
│   ├── inventory.ini      # Dynamically generated
│   └── deploy.yml         # Ansible playbook for deployment
└── README.md
```

---

## 📋 Prerequisites

* Jenkins installed with required plugins:

  * Docker Pipeline
  * SSH Agent
  * Pipeline
* AWS EC2 Ubuntu instance with:

  * Port 22 (SSH) and 80 (HTTP) open
  * Your public key added to `~/.ssh/authorized_keys`
* DockerHub account
* Jenkins credentials set for:

  * DockerHub (`dockerhub-creds`)
  * SSH key access to EC2

---

## 🔧 Jenkinsfile Pipeline Steps

1. **Checkout**: Pulls latest code from GitHub
2. **Build**: Builds Docker image using `Dockerfile`
3. **Login & Push**: Pushes image to Docker Hub
4. **Inventory**: Generates `inventory.ini` with EC2 IP
5. **Deploy**: Runs `ansible-playbook` to start container on EC2

---

## 📜 Example Ansible Playbook (`ansible/deploy.yml`)

```yaml
- name: Deploy app from Docker Hub to remote EC2
  hosts: all
  become: true
  vars:
    docker_image: "vaibhavisugandhi1733/myflaskapp5:latest"
    app_name: myapp
    container_port: 5000
    host_port: 80

  tasks:
    - name: Install Docker and prerequisites
      ...
    - name: Pull image and run container
      ...
    - name: Harden SSH access
      ...
```

(Refer to the full file in `ansible/deploy.yml`)

---

## 🧪 How to Run This Pipeline

1. 🔧 Configure your Jenkins job with the GitHub repo.
2. 🔑 Add your DockerHub and SSH credentials in Jenkins Credentials Manager.
3. 🖥️ Trigger the pipeline — Jenkins:

   * Builds Docker image
   * Pushes to DockerHub
   * Runs Ansible to deploy the app on EC2

---

## ✅ Result

* Flask app accessible at: `http://<EC2-IP>`
* No manual SSH or configuration required
* Secure, automated, reproducible deployments

---

## 📌 Author

**Vaibhavi Sugandhi**
🔗 [Portfolio](https://vaibhavisugandhi.netlify.app)
🔗 [LinkedIn](https://www.linkedin.com/in/vaibhavisugandhi)

---

## 📎 License

This project is licensed under the MIT License.

```


