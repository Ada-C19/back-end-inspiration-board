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

def test_delete_card(client, one_card):
    #Act
    response = client.delete("/cards/1")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 200
    assert "details" in response_body
    assert response_body == {
        "details": "Card 1 successfully deleted"
    }
    assert Card.query.get(1) == None
