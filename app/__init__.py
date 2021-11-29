from databases import Database
from sqlalchemy import MetaData, create_engine
import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

database_user = os.getenv("DATABASE_USER")
database_password = os.getenv("DATABASE_PASSWORD")
database_host = os.getenv("DATABASE_HOST")
database_name = os.getenv("DATABASE_NAME")

database = Database(
    f"postgresql://{database_user}:{database_password}@{database_host}/{database_name}"
)
metadata = MetaData(
    create_engine(
        f"postgresql://{database_user}:{database_password}@{database_host}/{database_name}",
        echo=True,
    )
)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.state.database = database


@app.on_event("startup")
async def startup() -> None:
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()


from app.views import noticia, pessoa
