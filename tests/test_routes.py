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
