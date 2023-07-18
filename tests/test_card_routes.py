from app.models.card import Card
from app.models.board import Board
import pytest
import json
def test_delete_card(client, one_card):



    # Act
    response = client.delete(f"/cards/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == "Card successfully deleted"

    assert Card.query.get(1) == None

def test_like_card(client, one_card):
    response = client.patch(f"cards/1/like")
    card = Card.query.get(1)
    assert response.status_code == 200
    assert card.likes_count == 1
    data = json.loads(response.data)
    assert data["likes_count"] == 1


def test_card_belongs_to_board(client, one_card, one_board):
    print(one_card, one_board)
    assert one_card.board_id == one_board.id
