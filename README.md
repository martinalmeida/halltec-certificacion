# Halltec Certificación API

Este proyecto utiliza **FastAPI** configurado en un **Virtual Environment** para proporcionar una API que consume a API-FACTUS para la certificación de Halltec.

## Requisitos
- Python 3.9+
- FastAPI
- Uvicorn

## Instalación
1. Clona el repositorio:
   ```bash
   git clone https://github.com/martinalmeida/halltec-certificacion
   ```

2. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

3. Inicia el servidor:
    ```bash
    uvicorn app.main:app --reload
    ```