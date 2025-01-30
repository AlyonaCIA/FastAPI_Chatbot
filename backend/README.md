# **🛠️ FastAPI Chatbot - Backend**

[![Tests](https://github.com/your-username/full-stack-fastapi-template/workflows/Test/badge.svg)](https://github.com/your-username/full-stack-fastapi-template/actions?query=workflow%3ATest)
[![Coverage](https://coverage-badge.samuelcolvin.workers.dev/your-username/full-stack-fastapi-template)](https://coverage-badge.samuelcolvin.workers.dev/your-username/full-stack-fastapi-template)

**Author**: Alyona Carolina Ivanova Araujo
**Version**: 1.0.0
**License**: MIT

---

## **📌 Overview**

This is the **backend** implementation of a **FastAPI-based chatbot** with **session-based conversation handling**, **TF-IDF vectorization**, and **natural language processing (NLP)**. The backend is fully containerized with **Docker**, ensuring smooth deployment and development.

---

## **📂 Backend Structure**

```
backend/
├── Dockerfile              # Defines the Docker container
├── main.py                 # FastAPI application entry point
├── config/
│   ├── data_loader.py      # Loads chatbot data from JSON
├── data/
│   ├── kindly-bot.json     # Predefined chatbot dialogues
├── services/
│   ├── chatbot_service.py  # Core chatbot logic
├── utils/
│   ├── session_manager.py  # Manages user sessions
├── schemas.py              # Pydantic schemas for API validation
├── test/
│   ├── unit_test/          # Unit tests
│   ├── integration_test/   # Integration tests
├── ci/                     # CI/CD automation scripts
├── requirements.txt        # Python dependencies
└── pytest.ini              # Pytest configuration
```

---

## **🔹 Prerequisites**

Ensure you have the following installed:

✅ **[Docker](https://www.docker.com/)** – For containerization
✅ **[uv](https://docs.astral.sh/uv/)** – For dependency and environment management
✅ **Python 3.10+** – Required for FastAPI

---

## **📦 Installation & Setup**

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/your-username/full-stack-fastapi-template.git
cd full-stack-fastapi-template/backend
```

### **2️⃣ Install Dependencies**
Using `uv` for dependency management:
```sh
uv sync
```

Or using `pip`:
```sh
pip install -r requirements.txt
```

### **3️⃣ Activate the Virtual Environment**
```sh
source .venv/bin/activate  # On macOS/Linux
venv\Scripts\activate      # On Windows
```

Ensure your **Python interpreter** is set to `backend/.venv/bin/python` in your **editor**.

---

## **🚀 Running the Backend**

### **With FastAPI (Development Mode)**
```sh
uvicorn backend.main:app --host 0.0.0.0 --port 8080 --reload
```
API documentation available at: [http://127.0.0.1:8080/docs](http://127.0.0.1:8080/docs)

---

## **🐳 Running with Docker**

### **1️⃣ Build the Docker Image**
```sh
docker build -t fastapi-chatbot .
```

### **2️⃣ Run the Container**
```sh
docker run -p 8080:8080 fastapi-chatbot
```
Now visit: [http://127.0.0.1:8080/docs](http://127.0.0.1:8080/docs)

---

## **🧪 Running Tests**

### **Unit Tests**
```sh
pytest backend/test/unit_test/
```

### **Integration Tests**
```sh
pytest backend/test/integration_test/
```

### **Run All Tests with CI/CD Pipeline**
```sh
bash ci/scripts/run_tests.sh
```

### **Running Tests in Docker**
If your container is already running, execute:
```sh
docker compose exec backend bash scripts/tests-start.sh
```

To stop on the first error:
```sh
docker compose exec backend bash scripts/tests-start.sh -x
```

### **Test Coverage**
A coverage report is generated at `htmlcov/index.html`. Open it in your browser to check test coverage.

---

## **📜 API Documentation**

### **1️⃣ Start a New Conversation**
```http
POST /api/conversation/start?language=en
```
**Response:**
```json
{
    "session_id": "c1091cdd-0d71-4645-9579-ce171f7393d5",
    "message": "Hello! I am a chatbot.",
    "success": true
}
```

### **2️⃣ Send a Message to the Chatbot**
```http
POST /api/conversation/message
```
**Request:**
```json
{
    "user_id": "c1091cdd-0d71-4645-9579-ce171f7393d5",
    "message": "Tell me a joke"
}
```
**Response:**
```json
{
    "session_id": "c1091cdd-0d71-4645-9579-ce171f7393d5",
    "message": "Why don’t robots ever get lost? Because they always follow the algorithm!",
    "success": true
}
```

### **3️⃣ Debug Active Sessions**
```http
GET /api/debug/sessions
```
Returns a list of active user sessions.

---

## **⚡ VS Code Debugging**

### **1️⃣ Open VS Code**
- Ensure your interpreter is set to `backend/.venv/bin/python`.
- Use the **VS Code debugger** to run and debug the backend.

### **2️⃣ Run Tests in VS Code**
- Use the **Python Test Explorer** to run tests inside VS Code.

---

## **🔧 Docker Compose Override (Development Mode)**

Modify `docker-compose.override.yml` for development-only changes:

1️⃣ **Auto-reloading FastAPI**
- Uses `uvicorn --reload` to restart on code changes.

2️⃣ **Live Code Synchronization**
- Mounts the backend directory inside the container, allowing real-time code updates without rebuilding.

### **Accessing the Container Shell**
Start the container and enter a shell session:
```sh
docker compose watch
docker compose exec backend bash
```
You should see:
```sh
root@7f2607af31c3:/app#
```
Then, manually run:
```sh
fastapi run --reload app/main.py
```
This allows **manual debugging** and **quick reloads** inside the container.

---

## **🛠 Database Migrations**

If using a database, apply schema changes with `Alembic`:

### **1️⃣ Enter the Container**
```sh
docker compose exec backend bash
```

### **2️⃣ Generate a New Migration**
```sh
alembic revision --autogenerate -m "Add new column"
```

### **3️⃣ Apply the Migration**
```sh
alembic upgrade head
```

---

## **📬 Email Templates**

Email templates are stored in `backend/email-templates/`.
For development:

1️⃣ Install the **MJML** extension in VS Code.
2️⃣ Create/edit templates in `src/`.
3️⃣ Convert `.mjml` files to `.html`.

---

## **🚀 CI/CD Pipeline**

### **🔹 GitHub Actions (Auto-Deployment)**
- **Formatting**: `isort` & `autopep8`
- **Linting**: `flake8`
- **Testing**: `pytest`
- **Docker Image Build**
- **Deployment to Production**

### **🔹 Deploy with Docker Compose**
```sh
docker-compose up --build -d
```

---

## **📞 Contact**
For any inquiries, feel free to reach out:
**Author**: Alyona Carolina Ivanova Araujo
📧 Email: [your-email@example.com](mailto:your-email@example.com)
🐙 GitHub: [github.com/your-username](https://github.com/your-username)
