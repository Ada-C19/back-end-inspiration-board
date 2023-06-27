from app.models.board import Board
import pytest

def test_get_boards_no_saved_boards(client):
    # Act
    response = client.get("/boards")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []


def test_get_board_not_found(client):
    # Act
    response = client.get("/boards/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"message" : "board 1 not found"}

def test_get_board_one_saved_board(client, one_board):
    # Act
    response = client.get("/boards")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 1
    assert response_body == [
        {
            "id": 1,
            "title" : "First Title",
            "owner" : "First Owner"
        }
    ]

def test_get_board_by_id(client, one_board):
    # Act
    response = client.get("/boards/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 1
    assert "board" in response_body
    assert response_body == {
        "board": {
            "id": 1,
            "title": "First Title",
            "owner": "First Owner"
        }
    }

def test_get_all_boards(client, three_boards):
    # Act
    response = client.get("/boards")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 3
    assert response_body ==[
        {
            "id": 1,
            "title": "First Title",
            "owner": "First Owner"
        },
        {
            "id": 2,
            "title": "Second Title",
            "owner": "Second Owner"
        },
        {
            "id": 3,
            "title": "Third Title",
            "owner": "Third Owner"
        },
    ]

# def test_get_cards_for_specific_board_no_cards(client, one_board):
#     # Act
#     response = client.get("/boards/1/cards")
#     response_body = response.get_json()

#     # Assert
#     assert response.status_code == 200
#     assert "cards" in response_body
#     assert len(response_body["cards"]) == 0
#     assert response_body == {
#         "id": 1,
#         "title": "First Title",
#         "owner": "First Owner",
#         "cards": []
#     }
