# **Project Startup**

This guide outlines the steps to set up a new project using FastAPI.

## **Prerequisites**

Before you begin, ensure you have the following prerequisites:

- Python installed on your system
- Pip (Python package manager) installed
- Basic understanding of virtual environments (optional but recommended)

## **Setup Instructions**

### **Mac**
1. Create a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

2. Install FastAPI and Uvicorn:
    ```bash
    pip install fastapi uvicorn
    pip install "uvicorn[standard]"
    ```

### **Windows**
1. Create a virtual environment:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

2. Install FastAPI and Uvicorn:
    ```bash
    pip install fastapi uvicorn
    pip install "uvicorn[standard]"
    ```