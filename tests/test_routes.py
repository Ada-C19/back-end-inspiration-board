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
    

def test_get_cards_one_saved_card(client, one_card, one_board_belongs_to_one_card):
    # Act
    response = client.get("/boards/1/cards")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 1

    card = response_body[0]
    assert card['message'] == 'Reminder to water plants'
    assert card['likes_count'] == 2



    