# FastAPI DevSecOps laboratory

Intentionally vulnerable local classroom app with synthetic data. Fork this repository and build the Jenkinsfile progressively with your instructor.

Required locally: Docker with Compose v2, Git, browser and GitHub account. All Python and security tools run in containers.

## Run the app

```bash
docker build -t classroom-app:manual .
docker run --rm --name classroom-manual -p 127.0.0.1:8000:8000 classroom-app:manual
```

Open http://localhost:8000. Stop with Ctrl+C.

## Start Jenkins

```bash
docker compose up -d --build
docker compose exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

Open http://localhost:8080, complete setup and create a Pipeline from SCM job pointing at your fork, branch `*/main`, script `Jenkinsfile`.

The initial stages only check out code and verify Docker. Add Trivy dependency SCA, Bandit SAST, image build, Trivy image scan, application startup and ZAP Baseline in that order.

Commit and push after each change, then trigger Jenkins manually. Open archived artifacts to review findings. Follow the instructor's guide for remediation and enforcement.

This Docker-in-Docker classroom setup uses a privileged Docker service. Use one lab pipeline job per Jenkins instance. The security.py token and password functions are source-analysis examples; only SQL lookup is used by the web routes.

```bash
docker compose down
```

Named volumes preserve Jenkins history. Adding `-v` deletes stored Jenkins and nested Docker data.
