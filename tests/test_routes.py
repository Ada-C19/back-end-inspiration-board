#  Routes for Board

from app.models.board import Board
import pytest

# @pytest.mark.skip(reason="Feature not yet built")
def test_get_board_no_board_saved(client):
    response = client.get("/boards")
    response_body = response.get_json()

    assert response.status.code == 200
    assert response_body ==[]

@pytest.mark.skip(reason="Feature not yet built")
def test_create_board(client):
    pass

# @pytest.mark.skip(reason="Feature not yet built")
def test_get_one_saved_board(client):
    response = client.get("/boards/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id": 3,
        "owner": "Amber",
        "title": "The Keep on Keepin On Board"  
    }

@pytest.mark.skip(reason="Feature not yet built")
def test_delete_board(client):
    pass

@pytest.mark.skip(reason="Feature not yet built")
def test_delete_board_not_found(client):
    pass


# @pytest.mark.skip(reason="Feature not yet built")
def test_create_card(client, three_saved_cards):
    test_data = {"message": "May the Force be with you.", "likes_count": 0}

    response = client.post("/cards", json=test_data)

    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == "Card successfully created"


# @pytest.mark.skip(reason="Feature not yet built")
def test_create_card_for_one_board(client, three_saved_cards_and_two_boards):
    test_data = {"id": 3}

    response = client.post("boards/2/cards", json=test_data)

    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == {"id": 2, "card_id": 3}


# @pytest.mark.skip(reason="Feature not yet built")
def test_get_all_cards_for_one_board(client, three_saved_cards_and_two_boards):
    response = client.get("boards/1/cards")

    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "title": "Shakespeare Quotes",
        "cards": [{"id": 1, "message": "To be, or not to be, that is the question",
                  "likes_count": 5}, {"id": 2, "message": "Romeo, Romeo! Wherefore art thou Romeo?",
                  "likes_count": 3}]
    }


# @pytest.mark.skip(reason="Feature not yet built")
def test_get_cards_for_all_boards(client, three_saved_cards_and_two_boards):
    response = client.get("/cards")

    response_body = response.get_json()

    assert response.status_code == 200
    assert len(response_body) == 3

