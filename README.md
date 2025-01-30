# 🗣️ FastAPI Chatbot

**Author**: Alyona Carolina Ivanova Araujo
**Version**: 1.0.0
**License**: MIT

## **📌 Project Overview**
This project is a **FastAPI-based chatbot API** that leverages **Natural Language Processing (NLP)** to generate responses based on predefined question-answer pairs. It uses **TF-IDF vectorization** to process and match user queries efficiently. The API is fully containerized with **Docker** and follows industry best practices for code organization, testing, and deployment.

## **🎯 Key Features**
✅ **FastAPI**: Lightweight and high-performance web framework.
✅ **NLP-based chatbot**: Uses **TF-IDF vectorization** and **cosine similarity** for response generation.
✅ **Session Management**: Keeps track of conversation states with UUID-based sessions.
✅ **Structured Logging**: Integrated **logging** for debugging and monitoring.
✅ **CI/CD Pipeline**: Automated linting, formatting, and testing using **GitHub Actions**.
✅ **Containerized Deployment**: Runs seamlessly in a **Docker** container.
✅ **Unit & Integration Tests**: Ensures API stability with **pytest** and **TestClient**.

---

## **📂 Project Structure**
.
├── README.md               # Project documentation
├── api_documentation.md    # Auto-generated API documentation
├── backend/                # Core backend API implementation
│   ├── Dockerfile          # Docker container definition
│   ├── main.py             # FastAPI application entry point
│   ├── config/             # Configuration files
│   │   ├── data_loader.py  # Loads chatbot data from JSON
│   ├── data/               # Dataset for chatbot responses
│   │   ├── kindly-bot.json # Predefined chatbot dialogues
│   ├── services/           # Business logic implementation
│   │   ├── chatbot_service.py # Core chatbot logic
│   ├── utils/              # Utility functions (session handling, logging)
│   │   ├── session_manager.py # Manages user sessions
│   ├── schemas.py          # Pydantic schemas for API validation
│   ├── test/               # Unit & Integration tests
│   │   ├── unit_test/      # Unit tests
│   │   ├── integration_test/ # Integration tests
│   ├── ci/                 # CI/CD automation scripts
│   ├── requirements.txt    # Python dependencies
└── pytest.ini              # Pytest configuration


---

## **📜 API Documentation**
The chatbot API exposes the following endpoints:

### **1️⃣ Start a new conversation**
```http
POST /api/conversation/start?language=en


**Response:**
```json
{
    "session_id": "c1091cdd-0d71-4645-9579-ce171f7393d5",
    "message": "Hello! I am a chatbot.",
    "success": true
}
```

### **2️⃣ Send a message to the chatbot**
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

## **🛠 Installation & Setup**
### **🔹 1. Clone the Repository**
```sh
git clone https://github.com/your-username/full-stack-fastapi-template.git
cd full-stack-fastapi-template
```

### **🔹 2. Create and Activate a Virtual Environment**
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### **🔹 3. Install Dependencies**
```sh
pip install -r requirements.txt
```

### **🔹 4. Run the FastAPI Server**
```sh
uvicorn backend.main:app --host 0.0.0.0 --port 8080 --reload
```
API will be available at: [http://127.0.0.1:8080/docs](http://127.0.0.1:8080/docs)

---

## **🐳 Running with Docker**
### **🔹 1. Build the Docker Image**
```sh
docker build -t fastapi-chatbot .
```
### **🔹 2. Run the Container**
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

---

## **🚀 CI/CD Pipeline**
The project includes a **CI/CD pipeline** that automates:
- **Code Formatting**: `isort` & `autopep8`
- **Linting**: `flake8`
- **Testing**: `pytest`
- **Containerization**: `Docker`
- **Deployment**: Configured for **GitHub Actions**

---

## **👨‍💻 Contributing**
Pull requests are welcome! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature-name`)
3. **Commit your changes** (`git commit -m "Add new feature"`)
4. **Push to GitHub** (`git push origin feature-name`)
5. **Submit a Pull Request**

---

## **📜 License**
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## **📞 Contact**
For any inquiries, feel free to reach out:
**Author**: Alyona Carolina Ivanova Araujo
📧 Email: [alenacivanovaa@gmail.com](mailto:alenacivanovaa@gmail.com)
🐙 GitHub: [github.com/your-username](https://github.com/your-username)
