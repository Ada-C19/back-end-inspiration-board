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
