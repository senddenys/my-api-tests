def test_get_post(session, base_url):
    response = session.get(f"{base_url}/posts/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "title" in data
    assert "body" in data

def test_create_post(session, base_url):
    payload = {
        "title": "my test post",
        "body": "some content",
        "userId": 1
    }
    response = session.post(f"{base_url}/posts", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "my test post"

def test_delete_post(session, base_url):
    response = session.delete(f"{base_url}/posts/1")
    assert response.status_code == 200
