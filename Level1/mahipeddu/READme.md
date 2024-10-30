# Docker Installation on Ubuntu 24.04

Installation of docker on ubuntu 24.04 LTS using the terminal

## Prerequisites
- Ubuntu 24.04 installed
- User with sudo privileges

## Step 1: Update Package Repository
Start by updating the package index:
```bash
sudo apt update
```

## Step 2: Install Packages
Install necessary packages:
```bash
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common
```

## Step 3: Add Docker Key
Add Docker's official GPG key:
```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```

## Step 4: Install Docker
Set up the Docker repository and install Docker:
```bash
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io
```

## Step 5: Verify Installation
Verify that Docker is installed correctly:
```bash
docker --version
```