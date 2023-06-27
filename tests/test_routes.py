from app.models.board import Board
from app.models.card import Card
import pytest


# BOARD TESTS
# @pytest.mark.skip(reason="No way to test this feature yet")
def test_create_board(client):
    # Act
    response = client.post("/boards", json={
        "title": "Test Board",
        "owner": "Test User",
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert "board" in response_body
    assert response_body == [{
        "board": {
            "id": 1,
            "board": "Test Board",
            "owner": "Test User",
        }
    }]
    new_board = Board.query.get(1)
    assert new_board
    assert new_board.title == "Test Board"
    assert new_board.owner == "Test User"


# @pytest.mark.skip
def test_get_boards_no_saved_board(client):
    # Act
    response = client.get("/boards")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []


# @pytest.mark.skip
def test_get_board_one_saved_board(client, one_board):
    # Act
    response = client.get("/boards")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 1
    assert response_body == [{
        "board": {
            "id": 1,
            "title": "Movie Lovers",
            "owner": "Amethyst"
        }
    }]


# @pytest.mark.skip
def test_get_board_by_id(client, one_board):
    # Act
    response = client.get("/boards/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 1
    assert response_body == {
        "board": {
            "id": 1,
            "title": "Movie Lovers",
            "owner": "Amethyst"
        }
    }


# @pytest.mark.skip
def test_get_404_error_with_id_not_found(client, one_board):
    # Act
    response = client.get("/boards/3")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {
        "message": "Board 3 does not exist"
    }


# @pytest.mark.skip
def test_get_400_error_with_invalid_id(client, one_board):
    # Act
    response = client.get("/boards/h")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {
        "message": "h is not a valid type. A <class 'str'> data type was provided. Must be a valid integer data type."
    }


# CARD TESTS
# @pytest.mark.skip
def test_get_cards_no_saved_card(client, one_board):
    # Act
    response = client.get("/boards/1/cards")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []
