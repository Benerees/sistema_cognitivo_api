# sistema_cognitivo_api
API de consulta de dados para o sistema cognitivo


python -m venv .venv
.venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

http://localhost:8000/docs

