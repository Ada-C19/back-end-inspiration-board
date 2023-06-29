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

def test_create_one_card(client, one_board):
    #Act
    response = client.post("/boards/1/cards", json={
        "message": "Test message",
        "likes_count": 0
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert "card_id" in response_body
    assert response_body == {
        'card_id' : 1,
        'message' : "Test message",
        'likes_count' : 0
    }

