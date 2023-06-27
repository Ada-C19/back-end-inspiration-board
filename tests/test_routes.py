from app.models.board import Board
import pytest

def test_create_board_no_owner(client):
    response = client.post('/boards', json = {
        "title": "stacy"
    })
    response_body = response.get_json()

    assert response_body == {"message": "Board input data incomplete"}
    assert response.status_code == 400

def test_create_board_no_title(client):
    response = client.post('/boards', json = {
    "owner": "stacy"
    })
    response_body = response.get_json()

    assert response_body == {"message": "Board input data incomplete"}
    assert response.status_code == 400

def test_create_board_success(client):
    response = client.post('/boards', json = {
        "owner": "Lindsay",
        "title": "capstone"
    })
    response_body = response.get_json()

    assert response_body == "Board 1 successfully created."
    assert response.status_code == 201

def test_create_board_no_data(client):
    response = client.post('/boards')
    response_body = response.get_json()

    assert response_body == {"message": "Board input data incomplete"}
    assert response.status_code == 400

def test_get_all_boards_with_no_records(client):
    response = client.get('/boards')
    response_body = response.get_json()

    assert response_body  == []
    assert response.status_code == 200

def test_get_all_boards_with_two_boards(client, two_saved_boards):
    response = client.get('/boards')
    response_body = response.get_json()

    assert response_body == [{"id" : 1, "owner" : "Lindsay", "title" : "Shroomies"}, 
    {"id": 2, "owner": "Stacy", "title":"idk"}]
    assert response.status_code == 200
