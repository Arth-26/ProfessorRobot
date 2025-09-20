from fastapi import FastAPI

from .core.database import engine
from .models.base import Base

app = FastAPI()


def init_db():
    Base.metadata.create_all(bind=engine)


@app.get('/')
def read_root():
    return {'message': 'Olá Mundo!'}


if __name__ == "__main__":
    init_db()
