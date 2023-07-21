# Mystical Mycology Muse

The Mystical Mycology Muse server is to be used with the [M^3 Dashboard](https://github.com/lindsaybolz/front-end-inspiration-board)

## Quick Start

1. Clone this repository. **You do not need to fork it first.**
    - `git clone https://github.com/lindsaybolz/back-end-inspiration-board.git`

1. Create and activate a virtual environment
    - `python3 -m venv venv`
    - `source venv/bin/activate`
1. Install the `requirements.txt`
    - `pip install -r requirements.txt`
1. Create a `.env` file with your API keys
    ```bash
    # .env

    # SQLALCHEMY_DATABASE_URI 
    SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://postgres:postgres@localhost:5432/inspiration_board_development

    # SQLALCHEMY_TEST_DATABASE_URI
    SQLALCHEMY_TEST_DATABASE_URI=postgresql+psycopg2://postgres:postgres@localhost:5432/inspiration_board_test

    # SLACK_API_KEY
    SLACK_API_KEY=Bearer "replace_with_your_api_key"
    ```
1. Create Databases on personal psql:
   ```
   $ psql -U postgres
   > CREATE DATABASE inspiration_board_test;
   > CREATE DATABASE inspiration_board_development;
   ```
2. Create flask database connection
   ```
   $ flask db init
   $ flask db migrate
   $ flask db upgrade
   ```
3. Run the server
    - `flask run`

## Endpoints

| Route | Query Parameter(s) | Query Parameter(s) Description |
|--|--|--|
|`POST` `/boards`| `owner` & `title` | Owner and title of board strings in json ex: `{"id": 1, "owner": "Lindsay", "title": "Fungi's 101"}` |
|`GET` `/boards` | None | Returns list of boards as dictionaries `[{"id": 1, "owner": "Lindsay", "title": "Fungi's 101"}, {...}]`|
|`DELETE` `/boards/<board_id>` | None | Returns: `Board successfully deleted`|
|`POST` `/boards/<board_id>/cards` | `message` | Returns: `{"id": 1 "owner": Stacy "title": "Fungi's 101"}`|
|`GET` `/boards/<board_id>/cards` | None | Returns list of cards for `<board_id>`: `[{'id':  1, message': "I like fungi" 'likes': 1 'board': "Fungi's 101"}, {...}]`.  This also posts a message to slack.|
|`DELETE` `/cards/<card_id>` | None | Returns: `Card successfully deleted`|
|`PATCH` `/cards/<card_id>` | None | Returns: dictionary of the card that was changed with updated like count by +1: `{'id':  1,'message': "I like fungi" 'likes': 2, 'board': "Fungi's 101"}`|

