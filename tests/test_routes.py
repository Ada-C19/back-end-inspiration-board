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

def test_get_card_not_found(client):
    # Act
    response = client.get("boards/1/cards")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {'message':'Board 1 not found'}

def test_update_like_on_card(client, one_card):
    # Act
    response = client.patch("cards/1/like")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body["likes_count"] == 3
    assert response_body == {
            "id" : 1,
            "message" : "Reminder to water plants",
            "likes_count" : 3
        }

