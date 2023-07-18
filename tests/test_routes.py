import pytest
from app.models.board import Board
from app.models.card import Card

def test_get_boards_no_saved_boards(client):
    response = client.get("/boards")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []


def test_get_board_one_saved_board(client, one_board):
    response = client.get("/boards")
    response_body = response.get_json()

    assert response.status_code == 200 
    assert len(response_body) == 1
    assert response_body == [
        {
            "id": 1,
            "title": "Inspiration Board",
            "owner": "Kunzite",
        }
    ]


def test_get_specific_board(client, one_board):
    response = client.get("/boards/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert len(response_body) == 1
    assert response_body == {
        "board": {
            "id": 1,
            "title": "Inspiration Board",
            "owner": "Kunzite",
        },
    }


def test_get_board_not_found(client):
    response = client.get("/boards/1")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {"message": "Board 1 not found"}


def test_create_board(client):
    response = client.post("/boards", json={
        "title": "Inspiration Board",
        "owner": "Kunzite"
    })

    response_body = response.get_json()
    assert "board" in response_body
    assert len(response_body) == 1
    assert response.status_code == 201

