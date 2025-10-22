# 🐳 Flask + Redis Counter App

A simple multi-tier web application built with **Flask (Python)** and **Redis**, orchestrated using **Docker Compose**.  
It demonstrates **container communication, volumes, environment variables, and Docker networking**.

---

## 🧠 Overview

This app counts how many times the main web page has been visited.

- The **Flask container** serves the web page.
- The **Redis container** stores the visit count.
- The two containers communicate over Docker's internal network.

---

## 🏗️ Architecture

```text
        +----------------------+
        |   Flask Web (App)    |
        |  - Python + Flask    |
        |  - Connects to Redis |
        +----------+-----------+
                   |
                   |
          Docker Network (bridge)
                   |
                   v
        +----------------------+
        |      Redis DB        |
        |  - Stores counter    |
        +----------------------+
---

--Run it locally:
bash:
git clone https://github.com/solj1z/flask-redis-counter.git
cd flask-redis-counter
docker compose up
Then open http://localhost:5000

--Development Mode (Auto Reload):
The Flask service uses a volume to sync code changes instantly without rebuilding:

volumes:
  - .:/app
environment:
  - FLASK_ENV=development
