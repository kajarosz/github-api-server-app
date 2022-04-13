from flask import Flask
from flask_app.api.routes import configure_routes

#  create app client for sensinf test requests
def create_client():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    return client

# path /user/<user_name>/repos
# test response status, type and data for valid user name
def test_get_user_repos_valid():
    client = create_client()
    url = '/user/kajarosz/repos'
    response =  client.get(url)
    assert response.status_code == 200
    assert b'user_repositories' in response.get_data()
    assert response.content_type == 'application/json'

# path /user/<user_name>/repos
# test response status, type and data for invalid user name
def test_get_user_repos_invalid():
    client = create_client()
    url = '/user/kajaroszzzzzzzzzz/repos'
    response =  client.get(url)
    assert response.status_code == 404
    assert b'{"error":"404 Not Found: Resource not found"}' in response.get_data()
    assert response.content_type == 'application/json'

# path /user/<user_name>/stars
# test response status, type and data for valid user name
def test_get_user_stars_valid():
    client = create_client()
    url = '/user/kajarosz/stars'
    response =  client.get(url)
    assert response.status_code == 200
    assert b'stars' in response.get_data()
    assert response.content_type == 'application/json'

# path /user/<user_name>/stars
# test response status, type and data for invalid user name
def test_get_user_stars_invalid():
    client = create_client()
    url = '/user/kajaroszzzzzzzzzz/stars'
    response =  client.get(url)
    assert response.status_code == 404
    assert b'{"error":"404 Not Found: Resource not found"}' in response.get_data()
    assert response.content_type == 'application/json'

# path /user/<user_name>/languages
# test response status, type and data for valid user name
def test_get_user_languages_valid():
    client = create_client()
    url = '/user/kajarosz/top3-languages'
    response =  client.get(url)
    assert response.status_code == 200
    assert b'top3-languages' in response.get_data()
    assert response.content_type == 'application/json'

# path /user/<user_name>/languages
# test response status, type and data for invalid user name
def test_get_user_languages_invalid():
    client = create_client()
    url = '/user/kajaroszzzzzzzzzz/top3-languages'
    response =  client.get(url)
    assert response.status_code == 404
    assert b'{"error":"404 Not Found: Resource not found"}' in response.get_data()
    assert response.content_type == 'application/json'
    
