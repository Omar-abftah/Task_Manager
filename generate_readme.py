from datetime import datetime
from config.settings import settings

def generate_readme():
    content = f"""# {settings.app_name}
    
    **Version:** {settings.app_version}  
    **Last Updated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
    **Debug Mode:** {"Enabled" if settings.debug else "Disabled"}
    
    ---
    
    ## 🧠 About
    A simple task manager built with **FastAPI** and **Pydantic** for learning and reviewing backend development basics.
    
    ---
    
    ## ⚙️ Features
    - Add, update, and delete tasks  
    - Filter and sort by status or priority  
    - In-memory storage (currently)  
    - Ready to switch to **PostgreSQL** backend  
    - Auto-generated API docs at `/docs` and `/redoc`
    
    ---
    
    ## 🚀 How to Run
    
    ### 1️⃣ Create a virtual environment
    ```bash
    python -m venv venv
    source venv/bin/activate   # on macOS/Linux
    venv\\Scripts\\activate    # on Windows
    """
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)

    print("✅ README.md has been generated successfully!")
if __name__ == "main":
    generate_readme()