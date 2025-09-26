from typing import Optional

from .usuario_schema import UsuarioBase, UsuarioResponse, UsuarioUpdate


class AlunoBase(UsuarioBase):
    tipo: Optional[str] = 'Aluno'
    data_nascimento: str


class AlunoCreate(AlunoBase):
    senha: str


class AlunoUpdate(UsuarioUpdate):
    pass


class AlunoResponse(UsuarioResponse):
    data_nascimento: str
    nivel: int
    xp: int
