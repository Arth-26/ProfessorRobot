from http import HTTPStatus
from typing import List

from fastapi import APIRouter

from ..schemas.usuario.professor_schema import (
    ProfessorCreate,
    ProfessorResponse,
    ProfessorUpdate,
)

professor_router = APIRouter(
    prefix="/professores",
    tags=["Professores"],
)

professores = [

]


@professor_router.get("/", status_code=HTTPStatus.OK, response_model=List[ProfessorResponse])
def read_professores():
    return professores


@professor_router.post("/", status_code=HTTPStatus.CREATED)
def create_professor(professor: ProfessorCreate):
    professores.append(professor)
    return {'message': 'Success'}


@professor_router.patch("/{nome}", status_code=HTTPStatus.OK)
def update_professor(nome: str, professor: ProfessorUpdate):
    for i, professor_obj in enumerate(professores):
        if professor_obj.nome == nome:
            update_data = professor.dict(exclude_unset=True)
            professores[i] = professor_obj.copy(update=update_data)
            return {'message': 'Professor atualizado com sucesso'}

    return {'message': 'Professor não encontrado'}


@professor_router.delete("/{nome}", status_code=HTTPStatus.OK)
def delete_professor(nome: str):
    for i, professor_obj in enumerate(professores):
        if professor_obj.nome == nome:
            professores.remove(professor_obj)
            return {'message': 'Professor removido com sucesso'}

    return {'message': 'Professor não encontrado'}
