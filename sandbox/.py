.
├── README.md
├── api_documentation.md
├── backend
│   ├── Dockerfile
│   ├── README.md
│   ├── __init__.py
│   ├── config/               # Configuración de la API
│   │   ├── __init__.py
│   │   ├── settings.py       # ⚠️ Reemplaza `data_loader.py` con algo más general
│   ├── data/                 # Datos de entrenamiento o modelos
│   │   ├── __init__.py
│   │   └── kindly - bot.json
│   ├── main.py               # Entrada principal de la API
│   ├── schemas/              # 📌 Define Pydantic models aquí
│   │   ├── __init__.py
│   │   ├── chatbot_schemas.py
│   ├── routers/              # 📌 Maneja endpoints de forma modular
│   │   ├── __init__.py
│   │   ├── chatbot_routes.py
│   ├── services/             # Lógica de negocio
│   │   ├── __init__.py
│   │   ├── chatbot_service.py
│   ├── tests/                # 📌 Pruebas renombradas correctamente
│   │   ├── __init__.py
│   │   ├── test_chatbot.py
│   ├── utils/                # Funciones auxiliares
│   │   ├── __init__.py
│   │   └── session_manager.py
├── ci/                       # CI/CD scripts
│   ├── deployment.md
│   ├── requirements/
│   │   └── validation_requirements.txt
│   ├── run_local.sh
│   └── scripts/
│       ├── apply_formatting.sh
│       ├── handle_messages.sh
│       ├── run_linting.sh
│       └── validate_formatting.sh
├── pytest.ini
├── requirements.txt
└── .dockerignore             # 📌 Agrega esto para optimizar Docker
