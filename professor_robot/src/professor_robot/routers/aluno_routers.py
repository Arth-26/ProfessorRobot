from http import HTTPStatus
from typing import List

from fastapi import APIRouter

from ..schemas.usuario.aluno_schema import (
    AlunoCreate,
    AlunoUpdate,
    AlunoResponse
)

aluno_router = APIRouter(
    prefix="/alunos",
    tags=["Alunos"],
)

alunos = [

]


@aluno_router.get("/", status_code=HTTPStatus.OK, response_model=List[AlunoResponse])
def read_users():
    return alunos


@aluno_router.post("/", status_code=HTTPStatus.CREATED)
def create_user(aluno: AlunoCreate):
    alunos.append(aluno)
    return {'message': 'Success'}


@aluno_router.patch("/{nome}", status_code=HTTPStatus.OK)
def update_user(nome: str, aluno: AlunoUpdate):
    for i, aluno_obj in enumerate(alunos):
        if aluno_obj.nome == nome:
            update_data = aluno.dict(exclude_unset=True)
            alunos[i] = aluno_obj.copy(update=update_data)
            return {'message': 'Aluno atualizado com sucesso'}

    return {'message': 'Aluno não encontrado'}


@aluno_router.delete("/{nome}", status_code=HTTPStatus.OK)
def update_user(nome: str):
    for i, aluno_obj in enumerate(alunos):
        if aluno_obj.nome == nome:
            alunos.remove(aluno_obj)
            return {'message': 'Aluno removido com sucesso'}

    return {'message': 'Aluno não encontrado'}
