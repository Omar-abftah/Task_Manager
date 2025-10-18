# generate_readme.py
from datetime import datetime
from config.settings import settings

def generate_readme():
    content = f"""# {settings.app_name}

Version: **{settings.app_version}**
Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## 🧠 About
A simple task manager built with FastAPI and Pydantic.

## ⚙️ Features
- Add, update, and delete tasks
- Filter by status
- PostgreSQL backend
- API docs at `/docs`

## 🚀 How to Run
```bash
uvicorn main:app --reload