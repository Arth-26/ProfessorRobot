from http import HTTPStatus

from fastapi.testclient import TestClient

from src.professor_robot.main import app

client = TestClient(app)


def test_request_get_read_root():
    '''DEVE RETORNAR UMA STRING "OLÁ MUNDO"'''

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}
