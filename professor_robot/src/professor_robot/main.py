from fastapi import FastAPI

from .core.database import engine
from .models.base import Base
from .routers.professor_routers import professor_router
from .routers.aluno_routers import aluno_router

app = FastAPI()

app.include_router(professor_router)
app.include_router(aluno_router)


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()
