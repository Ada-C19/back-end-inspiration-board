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
