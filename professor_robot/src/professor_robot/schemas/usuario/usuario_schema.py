import uuid
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class UsuarioBase(BaseModel):
    nome: str
    sobrenome: str
    email: EmailStr
    ativo: Optional[bool] = True
    pais: str
    estado: str
    foto_perfil: Optional[str] = None
    sobre_mim: Optional[str] = None


class UsuarioCreate(UsuarioBase):
    senha: str


class UsuarioUpdate(BaseModel):
    nome: Optional[str] = None
    sobrenome: Optional[str] = None
    email: Optional[EmailStr] = None
    senha: Optional[str] = None
    ativo: Optional[bool] = None
    pais: Optional[str] = None
    estado: Optional[str] = None
    foto_perfil: Optional[str] = None
    sobre_mim: Optional[str] = None


class UsuarioResponse(UsuarioBase):
    id: uuid.UUID
    data_cadastro: datetime
    ultimo_login: Optional[datetime] = None
