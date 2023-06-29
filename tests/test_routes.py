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

