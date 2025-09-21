import uuid
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class UsuarioBase(BaseModel):
    nome: str
    sobrenome: str
    email: EmailStr
    ativo: Optional[bool] = True
    tipo: str


class UsuarioCreate(UsuarioBase):
    senha: str


class UsuarioUpdate(BaseModel):
    nome: Optional[str] = None
    sobrenome: Optional[str] = None
    email: Optional[EmailStr] = None
    senha: Optional[str] = None
    ativo: Optional[bool] = None


class UsuarioResponse(UsuarioBase):
    id: uuid.UUID
    data_cadastro: datetime
    ultimo_login: Optional[datetime] = None
