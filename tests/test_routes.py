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


def test_create_board_invalid_data(client):
    response = client.post("/boards", json={
        "title": "Inspiration Board"
    })

    response_body = response.get_json()
    assert response.status_code == 400
    assert response_body == {
        "details": "Invalid data"
    }
    assert Board.query.get(1) == None



def test_delete_board(client, one_board):
    response = client.delete("/boards/1")
    response_data = response.get_json()

    assert response.status_code == 200
    assert response_data == {
        "details": "Board 1 \"Inspiration Board\" successfully deleted"
    }
    assert Board.query.get(1) == None
    

def test_delete_board_not_found(client):
    response = client.delete("/boards/1")
    response_data = response.get_json()

    assert response.status_code == 404
    assert response_data == {
        "message": "Board 1 not found"
    }


# @pytest.mark.skip(reason="still writing test")
def test_post_card_to_board(client, one_board, one_card):
    response = client.post("boards/1/cards", json={"message": one_card.message})
    response_data = response.get_json()

    assert response.status_code == 201
    assert response_data == "Write unit tests successfully posted on Inspiration Board"


