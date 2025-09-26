from typing import Optional

from .usuario_schema import UsuarioBase, UsuarioResponse, UsuarioUpdate


class ProfessorBase(UsuarioBase):
    tipo: Optional[str] = 'Professor'
    formacao: Optional[str] = None
    experiencia: Optional[str] = None


class ProfessorCreate(ProfessorBase):
    senha: str


class ProfessorUpdate(UsuarioUpdate):
    formacao: Optional[str] = None
    experiencia: Optional[str] = None


class ProfessorResponse(UsuarioResponse):
    formacao: Optional[str] = None
    experiencia: Optional[str] = None
