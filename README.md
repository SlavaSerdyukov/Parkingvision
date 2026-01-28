# ParkingVision 🚗📊

**Production-ready ML pipeline for parking occupancy prediction**

ParkingVision is an end-to-end machine learning project that predicts short-term parking availability using historical occupancy data.
The project is designed as a **real-world, production-style system**, demonstrating clean architecture, testability, packaging, Dockerization, and CI/CD.

This repository is intentionally built **beyond notebooks** — as a deployable, maintainable ML application.

## 🧠 Design & Interview Notes

**ParkingVision** was built as a **production-style ML system**, not a notebook demo.

### Key design decisions:

* **Simple ML model (linear regression)** used intentionally as a baseline
  → focus is on system design, not model complexity
* **Strict separation of concerns**
  data providers, ML logic, pipeline orchestration, CLI
* **CLI-first interface**
  easy to run locally, in Docker, and in CI
* **Mock-driven testing**
  deterministic tests and graceful handling of missing data
* **Dockerized & CI-ready**
  reproducible environment and automated validation

### What this demonstrates:

* ML engineering mindset
* Clean Python architecture
* Testable ML pipelines
* Production readiness over academic complexity

The system is designed to be **extended** (new models, APIs, persistence) without refactoring the core.


---

## ✨ Key Highlights

* 🧠 **ML-driven forecasting** (time-based regression)
* 🏗 **Clean architecture** with strict separation of concerns
* 🧪 **Fully tested** pipeline (unit + integration)
* 🖥 **CLI-first interface** (`parkingvision run ...`)
* 📦 **Proper Python packaging** (`pyproject.toml`, src-layout)
* 🐳 **Dockerized** for reproducible execution
* 🔄 **CI/CD ready** (GitHub Actions)
* 🧩 **Mock-friendly design** for deterministic testing

---

## 🧠 Machine Learning Approach

* **Problem**
  Predict parking availability *N minutes ahead* using historical data.

* **Model**
  Linear regression on time-based features.

* **Input**

  * Timestamp
  * Historical available spots

* **Output**

  * Point prediction for future availability
  * Graceful handling of insufficient data

The ML layer is intentionally simple to keep focus on **engineering quality**, not leaderboard chasing.

---

## 🏛 Architecture Overview

```
parkingvision/
│
├── src/
│   └── parkingvision/
│       ├── cli.py
│       ├── app/
│           ├── run_pipeline.py
│           └── api/
│           │    ├── base.py
│           │    └── mock.py
│           └── predictor.py
│   
│
├── tests/
│   ├── test_api.py
│   ├── test_pipeline.py
│   └── test_predictor.py
│
├── Dockerfile
├── pyproject.toml
└── README.md
```

**Design principles:**

* Single Responsibility Principle
* Dependency inversion
* Test isolation via mocks
* CLI as the main user interface
* src-layout for safe packaging

---

## 🚀 Usage

### Install locally (editable mode)

```bash
pip install -e .
```

### Run via CLI

```bash
parkingvision run \
  --city test \
  --parking "Mock Parking" \
  --use-mock
```

### Show help

```bash
parkingvision --help
```

---

## 🧪 Testing

```bash
pytest
```

Tests cover:

* ML predictor behavior
* Pipeline orchestration
* Mock API integration
* Edge cases (no historical data)

All tests are deterministic and CI-friendly.

---

## 🐳 Docker

### Build image

```bash
docker build -t parkingvision .
```

### Run container

```bash
docker run --rm parkingvision --help
```

```bash
docker run --rm parkingvision run \
  --use-mock \
  --city test \
  --parking "Mock Parking"
```

---

## 🔄 CI/CD

The project includes **GitHub Actions workflows**:

* **CI**

  * Editable install
  * Test execution
  * Import & packaging validation

* **Docker build**

  * Validates Dockerfile on every push to `main`

This ensures the project stays deployable and reproducible.

---

## 🛠 Tech Stack

* Python 3.11+
* NumPy
* pandas
* scikit-learn
* matplotlib
* pytest
* Docker
* GitHub Actions

---

## 🎯 Why This Project Exists

This project demonstrates:

* How to structure ML code **for production**
* How to test ML pipelines properly
* How to package and distribute Python applications
* How ML, backend engineering, and DevOps intersect

It is designed as a **strong portfolio project**, not a toy demo.

---

## 👤 Author

**Slava Serdiukov**
Machine Learning / Backend Engineering Portfolio Project

---

⭐ *If you’re reviewing this repository as part of a technical interview — start with the tests and the CLI.*
