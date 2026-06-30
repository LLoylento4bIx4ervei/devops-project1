# Devops Project 1: Контейнеризация Flask-приложения с Nginx и CI


[![Build Docker Image](https://github.com/LLoylento4bIx4ervei/devops-project1/actions/workflows/build.yml/badge.svg)](https://github.com/LLoylento4bIx4ervei/devops-project1/actions/workflows/build.yml)


## Используемый стек
- Python 3.11 + Flask
- Nginx как reverse proxy
- Docker, Docker Compose
- GitHub Actions (CI)

Краткое описание: приложение слушает порт 5000, Nginx проксирует внешние запросы на порт 80. В Docker-версии оба компонента запущены в отдельных контейнерах.


## Как запустить с Docker Compose
```bash
docker compose up -d
