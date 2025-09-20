import uuid

from sqlalchemy import UUID, Boolean, Column, DateTime, String
from sqlalchemy.sql import func

from ..base import Base


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nome = Column(String(50), nullable=False)
    sobrenome = Column(String(100), nullable=False)
    email = Column(String(255), nullable=False, unique=True, index=True)
    senha = Column(String(255), nullable=False)
    data_cadastro = Column(DateTime, default=func.now())
    ultimo_login = Column(DateTime, onupdate=func.now())
    ativo = Column(Boolean, default=True)
    tipo = Column(String(50))

    __mapper_args__ = {
        "polymorphic_identity": "usuario",
        "polymorphic_on": tipo
    }
