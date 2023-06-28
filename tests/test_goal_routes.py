import pytest

def test_get_boards_no_saved_boards(client):
    # Act
    response = client.get("/boards")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_goal(client, one_board):
    # Act
    response = client.get("/boards/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
            "id": 1,
            "title": "Positive Thoughts",
            "owner": "Grace Hopper"
            }
    
def test_create_board(client):
    # Act
    response = client.post("/boards", json={
        "title": "My New Board",
        "owner": "Grace Hopper"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "board": {
            "id": 1,
            "title": "My New Board",
            "owner": "Grace Hopper"
        }
    }