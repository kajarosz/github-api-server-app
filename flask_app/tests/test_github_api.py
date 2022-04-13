from flask import Flask
from flask_app.request_data.github_api import github_details, github_languages, github_stars, github_repos, github_languages

# test if function returns list object if username is valid
def test_github_details_valid():
    result = github_details('kajarosz')
    assert isinstance(result, list)

# test if function returns json data if username is valid
def test_github_repos_valid():
    result = github_repos('kajarosz')
    assert isinstance(result, dict)

# test if function returns None if username is not valid
def test_github_repos_invalid():
    result = github_repos('kajaroszzzzzzzzzz')
    assert result == None

# test if function returns json data if username is valid
def test_github_stars_valid():
    result = github_stars('kajarosz')
    assert isinstance(result, dict)

# test if function returns None if username is not valid
def test_github_stars_invalid():
    result = github_stars('kajaroszzzzzzzzzz')
    assert result == None

# test if function returns json data if username is valid
def test_github_languages_valid():
    result = github_languages('kajarosz')
    assert isinstance(result, dict)

# test if function returns None if username is not valid
def test_github_languages_invalid():
    result = github_languages('kajaroszzzzzzzzzz')
    assert result == None