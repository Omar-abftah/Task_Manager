Task Manager API (FastAPI)

Overview
This repository contains a simple Task Manager REST API built with FastAPI. It demonstrates a typical layered structure with routers, controllers, services, and schemas. Tasks are stored in-memory (a Python list), so data is lost when the app restarts. This makes it ideal for learning and quick prototyping.

Key features
- FastAPI app with automatic interactive docs (Swagger UI at /docs, ReDoc at /redoc)
- Layered modules: routers → controllers → services → schemas
- In-memory task storage with basic CRUD operations
- Pydantic models and enums for validation

Tech stack
- Language: Python (3.10+ recommended)
- Web framework: FastAPI
- Validation/settings: Pydantic, pydantic-settings
- ASGI server: Uvicorn (not listed in requirements.txt; see Setup)

Project structure
- main.py — FastAPI app factory and router inclusion
- config/ settings.py — App settings loaded from .env via pydantic-settings
- routers/ tasks.py — HTTP endpoints and routing
- controllers/ tasks_controller.py — Request handling, validation orchestration, HTTP exceptions
- services/ tasks_service.py — In-memory data store and business logic
- schemas/ tasks_schema.py — Pydantic models and Enums for Task data
- requirements.txt — Python dependencies (see note below)

Requirements
- Python 3.10 or newer (due to use of the | union operator in type hints)
- Pip and virtual environment tool of your choice

Environment variables
Settings are defined in config/settings.py and loaded from a .env file (via pydantic-settings). The following fields are supported:
- app_name: Name of the application (default: "Task Manager")
- app_version: Version string (default: "0.0.1")
- debug: Boolean flag to enable FastAPI debug mode (default: False)
- database_url: Database connection string (default: sqlite:///./task_manager.db)
Note: The current implementation uses in-memory storage and does not connect to a database yet. database_url is currently unused.

Example .env
APP_NAME=Task Manager
APP_VERSION=0.0.1
DEBUG=false
DATABASE_URL=sqlite:///./task_manager.db

Setup
1) Clone and enter the project
- git clone <your-fork-or-repo-url>
- cd "Task Manager"

2) Create and activate a virtual environment (examples)
- Python venv (Windows):
  - py -m venv .venv
  - .venv\Scripts\activate
- Python venv (Linux/macOS):
  - python3 -m venv .venv
  - source .venv/bin/activate

3) Install dependencies
Note: requirements.txt currently contains a shell-style command and may not be directly consumable by pip. Until that is corrected, install the packages manually:
- pip install fastapi pydantic pydantic-settings uvicorn
Alternatively, after fixing requirements.txt to list one package per line, you can run:
- pip install -r requirements.txt

Running the app
Development (auto-reload):
- uvicorn main:app --reload

Production-like (example):
- uvicorn main:app --host 0.0.0.0 --port 8000

Once running, visit:
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc
- Health check/root: http://127.0.0.1:8000/

API endpoints
Base URL: http://127.0.0.1:8000

- GET / — Returns {"message": "Hello World"}

Tasks (prefix /tasks)
- GET /tasks/show
  - Query params:
    - limit: integer (optional)
    - status: one of ["done", "not started", "in progress"] (optional)
  - Returns a list of tasks sorted by priority (high→low) then by id
- GET /tasks/show/{id}
  - Returns a single task by id
  - 404 if not found
- POST /tasks/create
  - Body (TaskCreate):
    - name: string (required)
    - priority: one of [high, medium, low] (required)
    - status: one of [done, not started, in progress] (required)
  - Returns the created task with assigned id
- PUT /tasks/update/{id}
  - Body (TaskUpdate): any subset of {name, priority, status}
  - Returns the updated task
  - 404 if not found
- DELETE /tasks/delete/{id}
  - Returns the deleted task
  - 404 if not found

Notes on data persistence
- All data is stored in-memory (services/tasks_service.py).
- Data resets on application restart. There is a database_url setting but no database integration yet. See TODOs below.

Common scripts/commands
- Run dev server: uvicorn main:app --reload
- Lint/format: TODO (no config or tooling present)
- Run tests: TODO (no tests present)

Testing
- No tests are currently present in the repository.
- TODO: Add tests (e.g., pytest + httpx/requests) and document how to run them.

Troubleshooting
- 422 Unprocessable Entity: Ensure your JSON body matches the schema and enum values exactly.
- 404 Not Found: Ensure the id exists.
- requirements.txt install fails: Manually install with pip install fastapi pydantic pydantic-settings uvicorn or correct requirements.txt to proper format.

Contributing
- Fork the repo and create a feature branch.
- Please include tests for new features where applicable. See TODO above.

License
- TODO: Add a license (e.g., MIT). If you are the repository owner, choose and add a LICENSE file, then update this section accordingly.

Roadmap / TODOs
- Replace in-memory storage with a real database using the existing database_url setting
- Add test suite and CI
- Add linting/formatting (e.g., ruff/black) and type checking (mypy/pyright)
- Containerize the app (Docker) and/or add deployment docs
