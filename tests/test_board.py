from app.models.board import Board
from datetime import datetime
import freezegun
import pytest

def test_get_boards_no_saved_boards(client):
    response = client.get("/boards")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []

def test_get_boards_one_saved_board(client, one_board):
    response = client.get("/boards")
    response_body = response.get_json()

    assert response.status_code == 200
    assert len(response_body) == 1
    assert response_body == [
        {
            "id": 1,
            "title": "Test Board",
            "owner": "Test Owner",
            "description": "Test Description",
            "theme": "Test Theme",
            "date_created": "Thu, 01 Jun 2023 12:00:00 GMT",
            "cards": []
        }
    ]

def test_get_boards_three_saved_boards(client, three_boards):
    response = client.get("/boards")
    response_body = response.get_json()

    assert response.status_code == 200
    assert len(response_body) == 3
    assert response_body == [
        {
            "id": 1,
            "title": "Test Board 1",
            "owner": "Test Owner 1",
            "description": "Test Description 1",
            "date_created": "Thu, 01 Jun 2023 12:00:00 GMT",
            "theme": "Test Theme 1",
            "cards": []
        },
        {
            "id": 2,
            "title": "Test Board 2",
            "owner": "Test Owner 2",
            "description": "Test Description 2",
            "date_created": "Thu, 01 Jun 2023 12:00:00 GMT",
            "theme": "Test Theme 2",
            "cards": []
        },
        {
            "id": 3,
            "title": "Test Board 3",
            "owner": "Test Owner 3",
            "description": "Test Description 3",
            "date_created": "Thu, 01 Jun 2023 12:00:00 GMT",
            "theme": "Test Theme 3",
            "cards": []
        }
    ]

def test_get_board_by_id(client, one_board):
    response = client.get("/boards/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "board": {
            "id": 1,
            "title": "Test Board",
            "owner": "Test Owner",
            "description": "Test Description",
            "date_created": "Thu, 01 Jun 2023 12:00:00 GMT",
            "theme": "Test Theme",
            "cards": []
        }
    }

def test_get_board_by_id_no_board(client):
    response = client.get("/boards/1")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {
        "error": "Board #1 not found"
    }

def test_get_board_by_id_invalid_id(client):
    response = client.get("/boards/one")
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == {
        "error": "'one' is not a valid id"
    }

def test_create_board(client):
    with freezegun.freeze_time("2023-06-01 12:00:00"):
        response = client.post("/boards", json={
            "title": "Test Board",
            "owner": "Test Owner",
            "description": "Test Description",
            "date_created": datetime.now(),
            "theme": "Test Theme"
        })
        response_body = response.get_json()

        assert response.status_code == 201
        assert "board" in response_body
        assert response_body == {
            "board": {
                "id": 1,
                "title": "Test Board",
                "owner": "Test Owner",
                "description": "Test Description",
                "date_created": "Thu, 01 Jun 2023 12:00:00 GMT",
                "theme": "Test Theme",
                "cards": []
            }
        }

        new_board = Board.query.get(1)
        assert new_board
        assert new_board.title == "Test Board"
        assert new_board.owner == "Test Owner"
        assert new_board.description == "Test Description"
        assert new_board.date_created == datetime(2023, 6, 1, 12, 0, 0)
        assert new_board.theme == "Test Theme"

def test_update_board(client, one_board):
    response = client.patch("/boards/1", json={
        "title": "New Title", 
        "description": "New Description",
        "theme": "New Theme"
    })
    response_body = response.get_json()

    assert response.status_code == 200
    assert "board" in response_body
    assert response_body == {
        "board": {
            "id": 1,
            "title": "New Title",
            "owner": "Test Owner",
            "description": "New Description",
            "date_created": "Thu, 01 Jun 2023 12:00:00 GMT",
            "theme": "New Theme",
            "cards": []
        }
    }

    updated_board = Board.query.get(1)
    assert updated_board
    assert updated_board.title == "New Title"
    assert updated_board.owner == "Test Owner"
    assert updated_board.description == "New Description"
    assert updated_board.date_created == datetime(2023, 6, 1, 12, 0, 0)
    assert updated_board.theme == "New Theme"
    assert updated_board.cards == []

def test_update_board_not_found(client):
    response = client.patch("/boards/1", json={
        "title": "New Title", 
        "description": "New Description",
        "theme": "New Theme"
    })
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {
        "error": "Board #1 not found"
    }

def test_update_board_invalid_id(client):
    response = client.patch("/boards/one", json={
        "title": "New Title", 
        "description": "New Description",
        "theme": "New Theme"
    })
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == {
        "error": "'one' is not a valid id"
    }

def test_delete_board(client, one_board):
    response = client.delete("/boards/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert "details" in response_body
    assert response_body == {
        "details": f'Board #1 successfully deleted'
    }

    assert Board.query.get(1) is None

def test_delete_board_not_found(client):
    response = client.delete("/boards/1")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {
        "error": "Board #1 not found"
    }

def test_delete_board_invalid_id(client):
    response = client.delete("/boards/one")
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == {
        "error": "'one' is not a valid id"
    }

def test_create_board_must_contain_title(client):
    response = client.post("/boards", json={
        "owner": "Test Owner",
        "description": "Test Description",
        "date_created": "Thu, 01 Jun 2023 12:00:00 GMT",
        "theme": "Test Theme"
    })
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == {
        "error": "missing required values", 
        "details": ["title"]
    }

def test_create_board_must_contain_owner(client):
    response = client.post("/boards", json={
        "title": "Test Title",
        "description": "Test Description",
        "date_created": "Thu, 01 Jun 2023 12:00:00 GMT",
        "theme": "Test Theme"
    })
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == {
        "error": "missing required values", 
        "details": ["owner"]
    }

def test_create_board_must_contain_description(client):
    response = client.post("/boards", json={
        "title": "Test Title",
        "owner": "Test Owner",
        "date_created": "Thu, 01 Jun 2023 12:00:00 GMT",
        "theme": "Test Theme"
    })
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == {
        "error": "missing required values", 
        "details": ["description"]
    }

def test_create_board_does_not_need_theme_or_time(client):
    with freezegun.freeze_time("2023-06-01 12:00:00"):
        response = client.post("/boards", json={
            "title": "Test Title",
            "owner": "Test Owner",
            "description": "Test Description",
        })
        response_body = response.get_json()

        assert response.status_code == 201
        assert "board" in response_body
        assert response_body == {
            "board": {
                "id": 1,
                "title": "Test Title",
                "owner": "Test Owner",
                "description": "Test Description",
                "date_created": "Thu, 01 Jun 2023 12:00:00 GMT",
                "cards": [],
                "theme": None
            }
        }

        new_board = Board.query.get(1)
        assert new_board
        assert new_board.title == "Test Title"
        assert new_board.owner == "Test Owner"
        assert new_board.description == "Test Description"
        assert new_board.date_created == datetime(2023, 6, 1, 12, 0, 0)
        assert new_board.theme == None

def test_get_all_cards_for_board_id(client, one_board, three_cards):
    response = client.get("/boards/1/cards")
    response_body = response.get_json()

    assert response.status_code == 200
    assert len(response_body) == 3
    assert response_body == [
        {
            "id": 1,
            "message": "Test Message 1",
            "likes_count": 0,
            "date_created": "Thu, 01 Jun 2023 12:00:00 GMT",
            "board_id": 1
        },
        {
            "id": 2,
            "message": "Test Message 2",
            "likes_count": 0,
            "date_created": "Thu, 01 Jun 2023 12:00:00 GMT",
            "board_id": 1
        },
        {
            "id": 3,
            "message": "Test Message 3",
            "likes_count": 0,
            "date_created": "Thu, 01 Jun 2023 12:00:00 GMT",
            "board_id": 1
        }
    ]