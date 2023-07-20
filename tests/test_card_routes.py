from app.models.card import Card
from app.models.board import Board
import pytest
import json


def test_delete_card(client, another_card):
    response = client.delete(f"/cards/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == "Card successfully deleted"
    assert Card.query.get(1) == None

def test_like_card(client, another_card):
    response = client.patch(f"cards/1/like")
    card = Card.query.get(1)

    assert response.status_code == 200
    assert card.likes_count == 1

    data = json.loads(response.data)
    
    assert data["likes_count"] == 1


def test_card_belongs_to_board(client, another_card, another_board):
    print(another_card, another_board)
    assert another_card.board_id == another_board.id


