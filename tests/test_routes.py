from app.models.board import Board
from app.models.card import Card
import pytest


###### BOARD TESTS ######

# @pytest.mark.skip
def test_create_board(client):
    # Act
    response = client.post("/boards", json={
        "title": "Test Board",
        "owner": "Test User",
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert "board" in response_body
    assert response_body == {
        "board": {
            "cards": [],
            "id": 1,
            "title": "Test Board",
            "owner": "Test User",
        }
    }
    new_board = Board.query.get(1)
    assert new_board
    assert new_board.title == "Test Board"
    assert new_board.owner == "Test User"
    assert new_board.cards == []


# @pytest.mark.skip
def test_get_error_to_create_board_with_missing_title(client):
    # Act
    response = client.post("/boards", json={
        "title": "Test Board"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert "details" in response_body
    assert response_body == {
        "details": "Invalid data"
    }
    assert Board.query.all() == []


# @pytest.mark.skip
def test_get_error_to_create_board_with_missing_owner(client):
    # Act
    response = client.post("/boards", json={
        "owner": "Test User"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert "details" in response_body
    assert response_body == {
        "details": "Invalid data"
    }
    assert Board.query.all() == []


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


# @pytest.mark.skip
def test_get_board_by_id(client, one_board):
    # Act
    response = client.get("/boards/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 1
    assert response_body == {
        "board": {
            "id": 1,
            "title": "Movie Lovers",
            "owner": "Amethyst"
        }
    }


# @pytest.mark.skip
def test_get_404_error_with_id_not_found(client, one_board):
    # Act
    response = client.get("/boards/3")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {
        "message": "Board 3 does not exist"
    }


# @pytest.mark.skip
def test_get_400_error_with_invalid_id(client, one_board):
    # Act
    response = client.get("/boards/h")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {
        "message": "h is not a valid type. A <class 'str'> data type was provided. Must be a valid integer data type."
    }


@pytest.mark.skip
def test_update_board(client, one_board):
    # Act
    response = client.put("/boards/1", json={
        "title": "Updated Board Title",
        "owner": "Updated Board Owner",
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert "board" in response_body
    assert response_body == {
        "board": {
            "id": 1,
            "title": "Updated Board Title",
            "owner": "Updated Board Owner",
        }
    }
    board = Board.query.get(1)
    assert board.title == "Updated Board Title"
    assert board.owner == "Updated Board Owner"


@pytest.mark.skip
def test_get_404_error_to_update_board_not_found(client, one_board):
    # Act
    response = client.put("/boards/2", json={
        "title": "Updated Board Title",
        "owner": "Updated Board Owner",
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {
        "message": "Board 2 does not exist"
    }


@pytest.mark.skip
def test_delete_board(client, one_board):
    # Act
    response = client.delete("/boards/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert "board" in response_body
    assert response_body == {
        "details": 'Board 1 successfully deleted'
    }
    assert Task.query.get(1) == None


@pytest.mark.skip
def test_get_404_error_to_delete_board_not_found(client, one_board):
    # Act
    response = client.delete("/boards/2")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {
        "message": "Board 2 does not exist"
    }


###### CARD TESTS ######

@pytest.mark.skip
def test_create_card(client):
    pass


@pytest.mark.skip
def test_get_card(client, one_card):
    # Act
    response = client.get("/cards")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 1
    assert response_body == [
        {
            "message": "Taylor Swift - Dear John!!! Get out my face, you stupid, man",
            "likes_count": 0
        }
    ]


def test_get_card_by_id(client, one_card):
    # Act
    response = client.get("/cards/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 1
    assert response_body == {
        "card": {
            "message": "Taylor Swift - Dear John!!! Get out of my face, you stupid, man",
            "likes_count": 0
        }
    }
