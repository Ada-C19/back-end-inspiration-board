from app.models.board import Board
from app.models.card import Card
from app.routes import validate_model, post_to_slack
from werkzeug.exceptions import HTTPException
import pytest


def test_create_board_no_owner(client):
    response = client.post('/boards', json = {
        "title": "stacy"
    })
    response_body = response.get_json()

    assert response_body == {"message": "Board input data incomplete"}
    assert response.status_code == 400

def test_create_board_no_title(client):
    response = client.post('/boards', json = {
    "owner": "stacy"
    })
    response_body = response.get_json()

    assert response_body == {"message": "Board input data incomplete"}
    assert response.status_code == 400

def test_create_board_success(client):
    response = client.post('/boards', json = {
        "owner": "Lindsay",
        "title": "capstone"
    })
    response_body = response.get_json()

    assert response_body == "Board 1 successfully created."
    assert response.status_code == 201

def test_create_board_no_data(client):
    response = client.post('/boards')
    response_body = response.get_json()

    assert response_body == {"message": "Board input data incomplete"}
    assert response.status_code == 400

def test_get_all_boards_with_no_records(client):
    response = client.get('/boards')
    response_body = response.get_json()

    assert response_body  == []
    assert response.status_code == 200

def test_get_all_boards_with_two_boards(client, two_saved_boards):
    response = client.get('/boards')
    response_body = response.get_json()

    assert response_body == [{"id" : 1, "owner" : "Lindsay", "title" : "Shroomies"}, 
    {"id": 2, "owner": "Stacy", "title":"idk"}]
    assert response.status_code == 200

def test_create_card_for_board_1(client, two_saved_boards):
    response = client.post('/boards/1/cards', json = {
        "message": "card 1 message"
    })
    response_body = response.get_json()
    board_response = client.get('/boards/1/cards')
    board_response_body = board_response.get_json()

    assert board_response_body == [{'board': 'Shroomies', 'id': 1, "message": "card 1 message", "likes": 0}]
    assert response_body == "Card was successfully created"
    assert response.status_code == 201

def test_create_card_for_board_1_over_40_characters(client, two_saved_boards):
    response = client.post('/boards/1/cards', json = {
        "message": "card 1 message jdhfjkdshfjhghskfjhahfjkshgjrkhsfkgjrsskjdfhasjkhfjkadhfjkhad"
    })
    response_body = response.get_json()

    board_response = client.get('/boards/1/cards')
    board_response_body = board_response.get_json()

    assert board_response_body == []
    assert response_body == {"message": "Message was too long, keep it under 40 characters please"}
    assert response.status_code == 400

def test_get_all_cards_from_board_1_with_no_cards(client, two_saved_boards):
    response = client.get('/boards/1/cards')
    response_body = response.get_json()

    assert response_body == []
    assert response.status_code == 200

def test_get_all_cards_from_board_one_with_two_cards(client, one_saved_boards_with_two_cards):
    response = client.get('/boards/1/cards')
    response_body = response.get_json()

    assert response_body == [{'board': 'Shroomies', 'id': 1, 'message': 'card 1 message', 'likes': 0},
        {'board': 'Shroomies', 'id': 2, 'message': 'card 2 message', 'likes': 0}]
    assert response.status_code == 200

def test_delete_card(client, one_saved_boards_with_two_cards):
    response = client.delete('/cards/1')
    response_body = response.get_json()

    card_response = client.get('/boards/1/cards')
    card_response_body = card_response.get_json()

    assert card_response_body == [{'board': 'Shroomies', 'id': 2, 'message': 'card 2 message', 'likes': 0}]
    assert response_body == "Card successfully deleted"
    assert response.status_code == 201

def test_card_like_increases_by_1(client, one_saved_boards_with_two_cards):
    response = client.patch('/cards/1')
    response_body = response.get_json()

    card_response = client.get('/boards/1/cards')
    card_response_body = card_response.get_json()
    print(card_response_body)
    assert card_response_body == [{'board': 'Shroomies', 'id': 2, 'message': 'card 2 message', 'likes': 0},
        {'board': 'Shroomies', 'id': 1, 'message': 'card 1 message', 'likes': 1}]
    assert response_body == {'board': 'Shroomies', 'id': 1, 'message': 'card 1 message', 'likes': 1}
    assert response.status_code == 200


def test_validate_model_returns_model(two_saved_boards):
    model_id = 1
    model = Board

    output = validate_model(model, model_id)

    assert output == Board.query.get(model_id)

def test_validate_model_returns_invalid_id(two_saved_boards):
    with pytest.raises(HTTPException):
        result = validate_model(Board, "cat")

def test_validate_model_returns_not_found(two_saved_boards):
    with pytest.raises(HTTPException):
        result = validate_model(Board, 3)

def test_post_to_slack_success(client, one_saved_boards_with_two_cards):
    # Set Up
    card_1 = Card(message = "card 1 message")
    board_1 = Board(owner = "Lindsay", title = "Shroomies", cards = [card_1])

    # Act
    response = post_to_slack(card_1)
    
    # Assert
    assert response.json()['message']['text'] == 'Card with message \"card 1 message\" for board \"Shroomies\" was created!'
    assert response.status_code == 200