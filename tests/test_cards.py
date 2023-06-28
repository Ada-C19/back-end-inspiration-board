from app.models.board import Board
from app.models.card import Card
import pytest

def test_get_cards_no_saved_cards(client):
    # Act
    response = client.get("/cards")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []


def test_get_card_not_found(client):
    # Act
    response = client.get("/cards/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"message" : "card 1 not found"}

def test_get_card_one_saved_card(client, one_card):
    # Act
    response = client.get("/cards")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 1
    assert response_body == [
        {
        "id": 1,
        "likes_count": 0,
        "message": "First Message"
    }

    ]

def test_get_card_by_id(client, one_card):
    # Act
    response = client.get("/cards/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 1
    assert "card" in response_body
    assert response_body == {
        "card": {
            "id": 1,
            "likes_count": 0,
            "message": "First Message"
        }
    }

def test_get_all_cards(client, three_cards):
    # Act
    response = client.get("/cards")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 3
    assert response_body ==[
        {
            "id": 1,
            "likes_count": 0,
            "message": "First Message"
        },
        {
            "id": 2,
            "likes_count": 0,
            "message": "Second Message"
        },
        {
            "id": 3,
            "likes_count": 0,
            "message": "Third Message"
        },
    ]

def test_delete_card(client, one_card):
    # Act
    response = client.delete("/cards/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert "details" in response_body
    assert response_body == {
        "details": f'Card 1 "First Message" successfully deleted'}


    response = client.get("/cards/1")
    assert response.status_code == 404
    assert Card.query.get(1) == None

def test_create_card(client):
    # Act
    response = client.post("/cards", json={
        "message": "First Message",
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert "cards" in response_body
    assert response_body == {
        "cards": {
            "id": 1,
            "likes_count": 0,
            "message": "First Message"
        }
    }


