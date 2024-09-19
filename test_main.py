from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_user_success():
    """
    Тест на успешное получение информации о пользователе.
    """
    response = client.get("/user/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Leanne Graham",
        "email": "Sincere@april.biz",
        "phone": "1-770-736-8031 x56442"
    }


def test_get_user_not_found():
    """
    Тест на получение ошибки 404 при запросе несуществующего пользователя.
    """
    response = client.get("/user/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}


def test_get_user_invalid_id():
    """
    Тест на получение ошибки 422 при запросе с невалидным ID (не числом).
    """
    response = client.get("/user/invalid_id")
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "type": "int_parsing",
                "loc": ["path", "user_id"],
                "msg": "Input should be a valid integer, unable to parse string as an integer",
                "input": "invalid_id",

            }
        ]
    }
