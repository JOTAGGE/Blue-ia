from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2
import pymongo

app = FastAPI()

# Conexão com PostgreSQL
def get_postgres_connection():
    return psycopg2.connect(
        host="YOUR_POSTGRES_HOST",
        database="YOUR_DB_NAME",
        user="YOUR_USER",
        password="YOUR_PASSWORD"
    )

# Conexão com MongoDB
def get_mongo_connection():
    return pymongo.MongoClient("YOUR_MONGO_CONNECTION_STRING")

# Modelo de exemplo
class Item(BaseModel):
    name: str
    description: str

# Rota simples de teste
@app.get("/")
async def read_root():
    return {"message": "Welcome to Blue!"}

@app.post("/add_item")
async def add_item(item: Item):
    # Exemplo de inserção no PostgreSQL
    conn = get_postgres_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO items (name, description) VALUES (%s, %s)", (item.name, item.description))
    conn.commit()
    return {"status": "Item added successfully"}

