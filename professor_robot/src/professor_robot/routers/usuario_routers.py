from http import HTTPStatus
from typing import List

from fastapi import APIRouter

from ..schemas.usuario.usuario_schema import UsuarioCreate, UsuarioBase, UsuarioUpdate

usuarios_router = APIRouter()

usuarios = [

]

@usuarios_router.get("/usuarios/", tags=['Usuarios'], status_code=HTTPStatus.OK, response_model=List[UsuarioBase])
def read_users():
    return usuarios
    
@usuarios_router.post("/usuarios/", tags=['Usuarios'], status_code=HTTPStatus.CREATED)
def create_user(usuario: UsuarioCreate):
    usuarios.append(usuario)
    return {'message': 'Sucess'}

@usuarios_router.patch("/usuarios/{nome}", tags=['Usuarios'], status_code=HTTPStatus.OK)
def update_user(nome: str, usuario: UsuarioUpdate):
    print(usuario)
    for i, usuario_obj in enumerate(usuarios):
        if usuario_obj.nome == nome:
            update_data = usuario.dict(exclude_unset=True)
            usuarios[i] = usuario_obj.copy(update=update_data)
            return {'message': 'Usuário atualizado com sucesso'}
    
    return {'message': 'Usuário não encontrado'}

@usuarios_router.delete("/usuarios/{nome}", tags=['Usuarios'], status_code=HTTPStatus.OK)
def update_user(nome: str):
    for i, usuario_obj in enumerate(usuarios):
        if usuario_obj.nome == nome:
            usuarios.remove(usuario_obj)
            return {'message': 'Usuário removido com sucesso'}
    
    return {'message': 'Usuário não encontrado'}

# @usuarios_router.get("/usuarios/", status_code=HTTPStatus.OK)

