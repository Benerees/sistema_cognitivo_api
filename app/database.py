from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_USERNAME = os.getenv("MONGO_USERNAME")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
MONGO_HOST = os.getenv("MONGO_HOST")
MONGO_PORT = os.getenv("MONGO_PORT")
MONGO_DB = os.getenv("MONGO_DB")

MONGO_URI = f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/"

try:
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=3000)
    db = client["tdc_workshop"]
    collection = db["event_logs"]
    client.admin.command("ping")
    print("===========================================================")
    print("✅ Conectado com sucesso ao MongoDB!")
except ConnectionFailure as e:
    print("===========================================================")
    print("❌ Falha ao conectar ao MongoDB:", e)
