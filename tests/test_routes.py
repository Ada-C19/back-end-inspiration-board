import pytest
from app.models.board import Board
from app.models.card import Card

def test_get_cards_no_saved_cards(client, one_board):
    #Act
    response = client.get("boards/1/cards")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 200
    assert response_body == []

def test_create_one_card(client):
    #Act
    response = client.post("/boards/1/cards", json={
        "message": "Test message",
        "likes count": 0
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert "message" in response_body
    # assert response_body == {
    #     "id": 1,
    #     "message": "Test message",
    #     "likes count": 0,
    #     "board id": 1,
    #     "board": "Board Title"
    # }
    assert response_body == {"id": 1, "card_id": 1}
