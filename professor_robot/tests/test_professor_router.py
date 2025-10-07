from http import HTTPStatus
import pytest
from fastapi.testclient import TestClient

from src.professor_robot.main import app
from src.professor_robot.routers.professor_routers import read_professores, create_professor, update_professor, delete_professor
from src.professor_robot.routers.professor_routers import professores

client = TestClient(app)

@pytest.fixture(autouse=True)
def clear_professores():
    professores.clear()


def test_request_post_create_professor():
    '''DEVE RETORNAR STATUS 201 CREATED E MENSAGEM DE SUCESSO'''

    json_body = {
        "nome": "Arthur",
        "sobrenome": "Gomes",
        "email": "art@example.com",
        "pais": "Brasil",
        "estado": "Paraiba",
        "sobre_mim": "Sou Eu",
        "formacao": "Gadruação",
        "experiencia": "Tenho muita experiência",
        "senha": "123456"
    }

    response = client.post('/professores/', json=json_body)

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {'message': 'Success'}
    assert len(professores) == 1
    assert professores[0].nome == "Arthur"
    assert professores[0].email == "art@example.com"
    assert professores[0].tipo == "Professor"
    assert professores[0].ativo == True


def test_request_patch_update_professor():
    '''DEVE RETORNAR STATUS 200 OK E MENSAGEM DE SUCESSO. SE NÃO ACHAR O PROFESSOR
    RETORNA STATUS 404 NOT FOUND E MENSAGEM DE NÃO ENCONTRADO'''

    nome1 = 'Arthur'
    nome2 = 'Lucas'

    json_body = {
        "sobrenome": "Alves",
    }

    response1 = client.patch(f'/professores/{nome1}', json=json_body)
    response2 = client.patch(f'/professores/{nome2}', json=json_body)

    assert response1.status_code == HTTPStatus.OK
    assert response1.json() == {'message': 'Professor atualizado com sucesso'}
    assert professores[0].sobrenome == "Alves"

    assert response2.status_code == HTTPStatus.NOT_FOUND
    assert response2.json() == {"detail": "Not Found"}
