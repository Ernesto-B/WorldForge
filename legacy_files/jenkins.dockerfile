FROM jenkins/jenkins:lts

USER root

RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv git curl unzip && \
    rm -rf /var/lib/apt/lists/*

# Install JMeter with root privileges
RUN curl -L https://downloads.apache.org//jmeter/binaries/apache-jmeter-5.6.3.tgz -o /tmp/jmeter.tgz \
 && mkdir -p /opt/jmeter \
 && tar -xzf /tmp/jmeter.tgz -C /opt/jmeter --strip-components=1 \
 && ln -s /opt/jmeter/bin/jmeter /usr/bin/jmeter \
 && rm /tmp/jmeter.tgz

USER jenkins

