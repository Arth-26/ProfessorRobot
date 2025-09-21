from fastapi import FastAPI

from .core.database import engine
from .models.base import Base
from .routers.usuario_routers import usuarios_router

app = FastAPI()

app.include_router(usuarios_router)


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()
