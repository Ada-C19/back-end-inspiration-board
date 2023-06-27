from app.models.board import Board
import pytest


# BOARD TESTS
# @pytest.mark.skip
def test_get_boards_no_saved_board(client):
    # Act
    response = client.get("/boards")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []


# @pytest.mark.skip
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
            "title": "Movie Lovers",
            "owner": "Amethyst"
        }
    ]


def test_get_board_by_id(client, one_board):
    # Act
    response = client.get("/boards/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 1
    assert response_body == [
        {
            "id": 1,
            "title": "Movie Lovers",
            "owner": "Amethyst"
        }
    ]


def test_get_404_error_with_id_not_found(client, one_board):
    # Act
    response = client.get("/boards/3")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {
        "message": "Board 3 does not exist"
    }


def test_get_400_error_with_invalid_id(client, one_board):
    # Act
    response = client.get("/boards/h")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {
        "message": "h is not a valid type. A <class 'str'> data type was provided. Must be a valid integer data type."
    }
