"""Setup configuration for FastAPI Chatbot."""
from setuptools import setup, find_packages

setup(
    name="fastapi-chatbot",
    version="1.0.0",
    description="A production-ready chatbot API built with FastAPI",
    author="Alyona Carolina Ivanova Araujo",
    author_email="alenacivanovaa@gmail.com",
    packages=find_packages(),
    python_requires=">=3.11",
    install_requires=[
        "fastapi~=0.109.0",
        "uvicorn~=0.27.0",
        "pydantic~=2.6.0",
        "pydantic-settings~=2.1.0",
        "scikit-learn~=1.4.0",
        "python-dotenv~=1.0.0",
        "cachetools~=6.1.0",
    ],
    extras_require={
        "dev": [
            "pytest~=8.0.0",
            "pytest-cov~=4.1.0",
            "black~=24.1.0",
            "isort~=5.13.0",
            "flake8~=7.0.0",
            "mypy~=1.8.0",
        ]
    }
)
