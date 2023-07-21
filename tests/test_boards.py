from app.models.board import Board
from app.models.card import Card
import pytest

def test_get_boards_no_saved_boards(client):
    # Act
    response = client.get("/boards")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []


def test_get_board_not_found(client):
    # Act
    response = client.get("/boards/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"message" : "board 1 not found"}

def test_get_board_one_saved_board(client, one_board):
    # Act
    response = client.get("/boards")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 1
    assert response_body == [
        {
            "id": 1,
            "title" : "First Title",
            "owner" : "First Owner"
        }
    ]

def test_get_board_by_id(client, one_board):
    # Act
    response = client.get("/boards/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 1
    assert "board" in response_body
    assert response_body == {
        "board": {
            "id": 1,
            "title": "First Title",
            "owner": "First Owner"
        }
    }

def test_get_all_boards(client, three_boards):
    # Act
    response = client.get("/boards")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 3
    assert response_body ==[
        {
            "id": 1,
            "title": "First Title",
            "owner": "First Owner"
        },
        {
            "id": 2,
            "title": "Second Title",
            "owner": "Second Owner"
        },
        {
            "id": 3,
            "title": "Third Title",
            "owner": "Third Owner"
        },
    ]

def test_delete_board(client, one_board):
    # Act
    response = client.delete("/boards/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert "details" in response_body
    assert response_body == {
        "details": f'Board 1 "First Title" successfully deleted'}


    response = client.get("/boards/1")
    assert response.status_code == 404
    assert Board.query.get(1) == None

def test_create_board(client):
    # Act
    response = client.post("/boards", json={
        "title": "First Title",
        "owner": "First Owner"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert "board" in response_body
    assert response_body == {
        "board": {
            "id": 1,
            "title": "First Title",
            "owner": "First Owner"
        }
    }


def test_post_card_to_goal_by_goal_id(client, one_board, one_card):
    # Act
    response = client.post("/boards/1/card", json=
        {
            "message": "First Message",
        })

    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert "id" in response_body["card"]
    assert "card" in response_body
    assert len(response_body) == 1
    assert response_body == {
        "card": {
            "id": 2,
            "message": "First Message",
            "likes_count": 0
        }

    }