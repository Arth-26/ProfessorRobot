from http import HTTPStatus

from fastapi import APIRouter

from ..schemas.usuario.usuario_schema import UsuarioCreate, UsuarioResponse

usuarios_router = APIRouter()

usuarios = [

]

@usuarios_router.get("/usuarios/", tags=['Usuarios'], status_code=HTTPStatus.OK, response_model=UsuarioResponse)
def read_users():
    return usuarios
    
@usuarios_router.post("/usuarios/", tags=['Usuarios'], status_code=HTTPStatus.CREATED)
def create_user(usuario: UsuarioCreate):
    usuarios.append(usuario)
    return {'message': 'Sucess'}

# @usuarios_router.get("/usuarios/", status_code=HTTPStatus.OK)

# @usuarios_router.get("/usuarios/", status_code=HTTPStatus.OK)

