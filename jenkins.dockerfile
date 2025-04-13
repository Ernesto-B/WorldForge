FROM jenkins/jenkins:lts

USER root

# Install Python, pip, venv, git
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv git curl unzip && \
    rm -rf /var/lib/apt/lists/*

USER jenkins

