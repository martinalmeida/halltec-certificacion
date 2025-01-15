![Github Banner](https://media1.giphy.com/media/h6rSTGtHbULzOBirkc/giphy.gif?cid=6c09b952wt3n3yufcs3ssq91iuz91dcohmdkduumkgrsxukc&ep=v1_internal_gif_by_id&rid=giphy.gif&ct=s)

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

## Generar Factura en Factus
1. En **Postman** consume al end-point GET **http://127.0.0.1:8000/get-token** para obtener el token de autenticación.

2. Pasamos el token en los headers al end-poin GET **http://127.0.0.1:8000/get-range** para obtener los rangos de usuarios configurados dentro de Factus.

3. De la misma forma anterior al end-poin GET **http://127.0.0.1:8000/get-municipality** para obtener los municipios dentro de Factus.

4. Igualmente al end-poin GET **http://127.0.0.1:8000/get-tribute** para obtener los productos tributarios dentro de Factus.

5. De nuevo al end-poin GET **http://127.0.0.1:8000/get-measures** para obtener las unidades de medidas dentro de Factus.

6. Con el token en los headers, en el end-poin POST **http://127.0.0.1:8000/create-invoice** procedemos a crear la factura dentro de Factus.