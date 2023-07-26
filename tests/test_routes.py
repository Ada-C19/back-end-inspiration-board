from app.models.board import Board
from app.models.card import Card
import pytest

# @pytest.mark.skip(reason="No way to test this feature yet")
def test_create_board(client):
    #Act
    response = client.post("/boards", json={
        "title": "Life Goals",
        "owner": "Angie",
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
            "board_id": 1,
            "title": "Life Goals",
            "owner": "Angie"
    }

# @pytest.mark.skip(reason="No way to test this feature yet")
def test_create_board_no_owner_returns_error(client):
    # Act
    response = client.post("/boards", json={
        "title": "Life Goals"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {
        "details": "Invalid data"
    }
    assert Board.query.all() == []

# @pytest.mark.skip(reason="No way to test this feature yet")
def test_create_board_no_title_returns_error(client):
    # Act
    response = client.post("/boards", json={
        "owner": "Angie"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {
        "details": "Invalid data"
    }
    assert Board.query.all() == []

# @pytest.mark.skip(reason="No way to test this feature yet")
def test_get_all_boards(client, one_board):
    # Act
    response = client.get("/boards")
    response_body = response.get_json()

    # Assert 
    assert response.status_code == 200
    assert len(response_body) == 1
    assert response_body == [{
        "board_id": 1,
        "title": "Life Goals",
        "owner": "Angie"
    }]

# @pytest.mark.skip(reason="No way to test this feature yet")
def test_get_one_board_no_id_returns_error(client):
    # Act
    response = client.get("/boards/100")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"message": "Board 100 not found"}

# @pytest.mark.skip(reason="No way to test this feature yet")
def test_get_one_board(client, three_boards):
    # Act 
    response = client.get("/boards/3")
    response_body = response.get_json()

    #Assert 
    assert response.status_code == 200
    assert response_body == { 
        "board_id": 3, 
        "title": "Self-Improvement", 
        "owner": "Alejandra"
    }

# @pytest.mark.skip(reason="No way to test this feature yet")
def test_delete_board_by_id(client, three_boards):
    # Act 
    response = client.delete("/boards/1")
    response_body = response.get_json()

    # Assert 
    assert response.status_code == 200
    assert response_body == {
        "message": "Board 1 successfully deleted"
    }
    assert Board.query.get(1) == None

# @pytest.mark.skip(reason="No way to test this feature yet")
def test_add_card_to_board(client, one_board):
    # Act 
    response = client.post("/boards/1/cards", json={
        "board_id": 1, "card_id": 1, "likes_count": 0, "message": "Hello World!"
    })
    response_body = response.get_json()

    # Assert 
    assert response.status_code == 201
    assert response_body == {
        "board_id": 1,
        "card_id": 1,
        "likes_count": 0,
        "message": "Hello World!" 
    }

# @pytest.mark.skip(reason="No way to test this feature yet")
def test_get_cards_of_one_board(client, three_cards):
    # Act
    response = client.get("/boards/1/cards")
    response_body = response.get_json()

    # Assert 
    assert response.status_code == 200
    assert response_body == [
        {"board_id": 1, "card_id": 1, "likes_count": 0, "message": "Good things are coming!"}, 
        {"board_id": 1, "card_id": 2, "likes_count": 5, "message": "You are doing great!"}, 
        {"board_id": 1, "card_id": 3, "likes_count": 14, "message": "Don't forget to drink lots of water!"},
    ]

# @pytest.mark.skip(reason="No way to test this feature yet")
def test_update_likes_card(client, one_card):
    # Act 
    response = client.put("/cards/1/like", json={"likes_count": 1})
    response_body = response.get_json()
    # Assert 
    card = Card.query.get(1)
    assert response.status_code == 200
    assert response_body == {
        "board_id": 1,
        "card_id": 1,
        "likes_count": 1,
        "message": "Good things are coming!"
    }
    assert card.likes_count == 1

# @pytest.mark.skip(reason="No way to test this feature yet")
def test_update_likes_card_no_id_returns_error(client):
    # Act 
    response = client.put("/cards/1/like")
    response_body = response.get_json()
    # Assert 
    assert response.status_code == 404
    assert response_body == {"message": "Card 1 not found"}

# @pytest.mark.skip(reason="No way to test this feature yet")
def test_delete_one_card(client, one_card):
    # Act
    response = client.delete("/cards/1")
    response_body = response.get_json()

    # Assert 
    assert response.status_code == 200
    assert response_body == {"message": "Card 1 successfully deleted"}
    assert Card.query.all() == []

# @pytest.mark.skip(reason="No way to test this feature yet")
def test_delete_card_no_id_returns_error(client):
    # Act
    response = client.delete("/cards/100")
    response_body = response.get_json()
    # Assert
    assert response.status_code == 404
    assert response_body == {"message": "Card 100 not found"}
    assert Card.query.all() == []