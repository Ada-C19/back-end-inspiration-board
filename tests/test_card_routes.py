import pytest

def test_get_cards_no_saved_cards(client, one_board):
    # Act
    response = client.get("/boards/1/cards")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_card(client, one_board, one_card):
    response = client.get("/boards/1/cards")
    response_body = response.get_json()

    assert response_body == [{'id': 1, 'likes_count': None, 'message': "You're awesome!"}]
