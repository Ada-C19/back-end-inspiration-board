from app.models.card import Card
from datetime import datetime
import freezegun
import pytest

def test_get_cards_no_saved_cards(client):
    response = client.get("/cards")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []

def test_get_cards_one_saved_card(client, one_board, one_card):
    response = client.get("/cards")
    response_body = response.get_json()

    assert response.status_code == 200
    assert len(response_body) == 1
    assert response_body == [
        {
            "id": 1,
            "message": "Test Message",
            "date_created": "Thu, 01 Jun 2023 12:00:00 GMT",
            "likes_count": 0,
            "board_id": 1
        }
    ]

def test_get_cards_three_saved_cards(client, one_board, three_cards):
    response = client.get("/cards")
    response_body = response.get_json()

    assert response.status_code == 200
    assert len(response_body) == 3
    assert response_body == [
        {
            "id": 1,
            "message": "Test Message 1",
            "date_created": "Thu, 01 Jun 2023 12:00:00 GMT",
            "likes_count": 0,
            "board_id": 1
        },
        {
            "id": 2,
            "message": "Test Message 2",
            "date_created": "Thu, 01 Jun 2023 12:00:00 GMT",
            "likes_count": 0,
            "board_id": 1
        },
        {
            "id": 3,
            "message": "Test Message 3",
            "date_created": "Thu, 01 Jun 2023 12:00:00 GMT",
            "likes_count": 0,
            "board_id": 1
        }
    ]
    

def test_get_card_by_id(client, one_board, one_card):
    response = client.get("/cards/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert "card" in response_body
    assert response_body == {
        "card": {
            "id": 1,
            "message": "Test Message",
            "date_created": "Thu, 01 Jun 2023 12:00:00 GMT",
            "likes_count": 0,
            "board_id": 1
        }
    }
    

def test_get_card_by_id_no_card(client):
    response = client.get("/cards/1")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {
        "error": "Card #1 not found"
    }

def test_get_card_by_id_invalid_id(client):
    response = client.get("/cards/one")
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == {
        "error": "'one' is not a valid id"
    }

def test_create_card(client, one_board):
    with freezegun.freeze_time("2023-06-01 12:00:00"):
        response = client.post("/boards/1/cards", json={
            "message": "Test Message",
        })
        response_body = response.get_json()
        print(response_body)

        assert response.status_code == 201
        assert "card" in response_body
        assert response_body == {
            "card": {
                "id": 1,
                "message": "Test Message",
                "date_created": "Thu, 01 Jun 2023 12:00:00 GMT",
                "likes_count": 0,
                "board_id": 1
            }
        }

        new_card = Card.query.get(1)
        assert new_card
        assert new_card.message == "Test Message"
        assert new_card.date_created == datetime(2023, 6, 1, 12, 0, 0)
        assert new_card.likes_count == 0
        assert new_card.board_id == 1


def test_update_card_message(client, one_board, one_card):
    response = client.patch("/cards/1", json={
        "message": "New Message",
    })
    response_body = response.get_json()

    assert response.status_code == 200
    assert "card" in response_body
    assert response_body == {
        "card": {
            "id": 1,
            "message": "New Message",
            "date_created": "Thu, 01 Jun 2023 12:00:00 GMT",
            "likes_count": 0,
            "board_id": 1
        }
    }

    updated_card = Card.query.get(1)
    assert updated_card
    assert updated_card.message == "New Message"
    assert updated_card.date_created == datetime(2023, 6, 1, 12, 0, 0)
    assert updated_card.likes_count == 0
    assert updated_card.board_id == 1


def test_update_card_likes(client, one_board, one_card):
    response = client.patch("/cards/1", json={
        "likes_count": 1,
    })
    response_body = response.get_json()

    assert response.status_code == 200
    assert "card" in response_body
    assert response_body == {
        "card": {
            "id": 1,
            "message": "Test Message",
            "date_created": "Thu, 01 Jun 2023 12:00:00 GMT",
            "likes_count": 1,
            "board_id": 1
        }
    }

    updated_card = Card.query.get(1)
    assert updated_card
    assert updated_card.message == "Test Message"
    assert updated_card.date_created == datetime(2023, 6, 1, 12, 0, 0)
    assert updated_card.likes_count == 1
    assert updated_card.board_id == 1


def test_update_card_not_found(client):
    response = client.patch("/cards/1", json={
        "message": "New Message", 
    })
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {
        "error": "Card #1 not found"
    }

def test_update_card_invalid_id(client):
    response = client.patch("/cards/one", json={
        "message": "New Message", 
    })
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == {
        "error": "'one' is not a valid id"
    }

def test_delete_card(client, one_board, one_card):
    response = client.delete("/cards/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert "details" in response_body
    assert response_body == {
        "details": f'Card #1 successfully deleted'
    }

    assert Card.query.get(1) is None

def test_delete_card_not_found(client):
    response = client.delete("/cards/1")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {
        "error": "Card #1 not found"
    }

def test_delete_card_invalid_id(client):
    response = client.delete("/cards/one")
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == {
        "error": "'one' is not a valid id"
    }