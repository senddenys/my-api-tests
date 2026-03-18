import pytest

def test_get_user(session, base_url):
    response = session.get(f"{base_url}/users/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "name" in data
    assert "email" in data

def test_get_user_not_found(session, base_url):
    response = session.get(f"{base_url}/users/999")
    assert response.status_code == 404

@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_multiple_users(session, base_url, user_id):
    response = session.get(f"{base_url}/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["id"] == user_id