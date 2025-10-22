# Flask + Redis Counter App

A simple multi-tier web application built with **Flask (Python)** and **Redis**, orchestrated using **Docker Compose**.  
It demonstrates **container communication, volumes, environment variables, and Docker networking**.

---

## Overview

This app counts how many times the main web page has been visited.

- The **Flask container** serves the web page.
- The **Redis container** stores the visit count.
- The two containers communicate over Docker's internal network.

---

## Architecture

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
