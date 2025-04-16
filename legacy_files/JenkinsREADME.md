# Jenkins CI/CD Pipeline Setup for WorldForge

This README documents the complete Jenkins-based CI/CD setup for the WorldForge project. It includes the purpose and structure of the Jenkins pipeline, Docker Compose setup for local development, plugin configuration, and guidance on reproducing the environment.

---

## What the Jenkins Pipeline Does

The Jenkinsfile implements a modern, industry-inspired CI/CD pipeline with the following stages:

| Stage                  | Description                                                              |
| ---------------------- | ------------------------------------------------------------------------ |
| Checkout               | Clones the Git repository                                                |
| Build                  | Creates a Python virtual environment and installs dependencies           |
| Linting (flake8)       | Runs `flake8` with strict rules to catch syntax errors and bad practices |
| Unit Testing (pytest)  | Runs tests with `pytest` and generates coverage and JUnit reports        |
| Quality (SonarQube)    | Performs static analysis using SonarQube, integrated with test coverage  |
| Performance (JMeter)   | Runs performance tests if `backend/tests/load_tests.jmx` exists          |
| Security Scan (Bandit) | Runs `bandit` to identify Python security issues and visualizes results  |

Artifacts like `coverage.xml` and `bandit-report.html` are stored and can be visualized in Jenkins.

---

## Docker-Based Local Setup

### Files Used

- `docker-compose.yml`: Defines containers for MySQL, Jenkins, SonarQube, and the backend.
- `Dockerfile.jenkins`: Custom Jenkins image with required CLI tools (like `sonar-scanner`, `jmeter`, etc.).

### Run Locally

```bash
docker compose up --build
```

This spins up:

- **Jenkins** on `http://localhost:8081`
- **SonarQube** on `http://localhost:9000`
- **MySQL** on port `8080`

---

## Jenkins Plugin Setup

Inside the Jenkins UI (`http://localhost:8081`):

1. Go to **Manage Jenkins → Plugin Manager**
2. Install the following plugins:
   - **Pipeline**
   - **JUnit**
   - **Cobertura**
   - **Warnings Next Generation** (for `bandit`/security reporting)
   - **SonarQube Scanner**
   - **Coverage**
   - **Git**
   - **GitHub Integration (optional)**

---

## Jenkins Credentials

To securely pass secrets (like the SonarQube token):

1. Go to **Manage Jenkins → Credentials**
2. Create a **Secret Text** in the global space with:
   - ID: `SONAR_TOKEN`
   - Value: (your token from SonarQube)

---

## Jenkinsfile Location

The `Jenkinsfile` resides in the `/backend` folder of the repository. Jenkins is configured to scan this path using its **Multibranch Pipeline** or **Pipeline from SCM** job type.

---

## Triggering the Pipeline

Currently, this pipeline must be run **manually** by launching Jenkins locally using Docker Compose.

In the future, this could be improved (by deploying Jenkins) to allow for GitHub webhook triggers. This is the reason I am deciding to change from Jenkins to GitHub Actions... GitHub spins a VM to run the pipeline, thus bypassing the need to deploy an instance of Jenkins or similar.

---

## Why the Switch to GitHub Actions

While Jenkins provides strong visualization and control, it requires local setup and Docker configuration. If you want:

- Fully cloud-based pipeline execution
- Native integration with GitHub
- Simpler secret and permission handling

Then GitHub Actions is ideal. The new pipeline file can be found in `.github/workflows/backend.yml`.

---

## Returning to Jenkins?

If wanting to return to Jenkins, just:

1. `docker compose up --build`
2. Reinstall required plugins if missing
3. Add your SonarQube token again
4. Re-run the pipeline via Jenkins UI

---

## Future Improvements (to Jenkins pipeline)

- Trigger on PR or push via webhook or GitHub Actions
- Add Slack or email notifications
- Push Docker image to a registry post-build
- Deploy to staging or prod after passing all checks

