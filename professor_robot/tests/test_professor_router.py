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
    '''DEVE RETORNAR STATUS 201 CREATED E MENSAGEM DE SUCESSO E DEVE MOSTRAR
    O NOVO PROFESSOR CRIADO'''

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
