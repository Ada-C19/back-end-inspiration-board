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
    response = client.get("/board/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"message" : "Board 1 not found"}
